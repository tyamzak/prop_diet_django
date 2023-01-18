import json

import dash_html_components as html
import dash_core_components as dcc
from dash import Dash
from dash.dependencies import Output, Input

from dash.testing.plugin import *
from .. import BaseDashView


def test_rdrh001_request_hooks(dash_duo):
    app = Dash(__name__)

    app.index_string = """<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
        </head>
        <body>
            <div>Testing custom DashRenderer</div>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                <script id="_dash-renderer" type"application/json">
                    const renderer = new DashRenderer({
                        request_pre: (payload) => {
                            var output = document.getElementById('output-pre')
                            var outputPayload = document.getElementById('output-pre-payload')
                            if(output) {
                                output.innerHTML = 'request_pre changed this text!';
                            }
                            if(outputPayload) {
                                outputPayload.innerHTML = JSON.stringify(payload);
                            }
                        },
                        request_post: (payload, response) => {
                            var output = document.getElementById('output-post')
                            var outputPayload = document.getElementById('output-post-payload')
                            var outputResponse = document.getElementById('output-post-response')
                            if(output) {
                                output.innerHTML = 'request_post changed this text!';
                            }
                            if(outputPayload) {
                                outputPayload.innerHTML = JSON.stringify(payload);
                            }
                            if(outputResponse) {
                                outputResponse.innerHTML = JSON.stringify(response);
                            }
                        }
                    })
                </script>
            </footer>
            <div>With request hooks</div>
        </body>
    </html>"""

    app.layout = html.Div(
        [
            dcc.Input(id="input", value="initial value"),
            html.Div(
                html.Div(
                    [
                        html.Div(id="output-1"),
                        html.Div(id="output-pre"),
                        html.Div(id="output-pre-payload"),
                        html.Div(id="output-post"),
                        html.Div(id="output-post-payload"),
                        html.Div(id="output-post-response"),
                    ]
                )
            ),
        ]
    )

    @app.callback(Output("output-1", "children"), [Input("input", "value")])
    def update_output(value):
        return value

    class DashView(BaseDashView):
        dash = app

    dash_duo.start_server(DashView)

    _in = dash_duo.find_element("#input")
    dash_duo.clear_input(_in)

    _in.send_keys("fire request hooks")

    dash_duo.wait_for_text_to_equal("#output-1", "fire request hooks")
    dash_duo.wait_for_text_to_equal("#output-pre", "request_pre changed this text!")
    dash_duo.wait_for_text_to_equal("#output-post", "request_post changed this text!")

    assert json.loads(dash_duo.find_element("#output-pre-payload").text) == {
        "output": "output-1.children",
        "outputs": {"id": "output-1", "property": "children"},
        "changedPropIds": ["input.value"],
        "inputs": [{"id": "input", "property": "value", "value": "fire request hooks"}],
    }

    assert json.loads(dash_duo.find_element("#output-post-payload").text) == {
        "output": "output-1.children",
        "outputs": {"id": "output-1", "property": "children"},
        "changedPropIds": ["input.value"],
        "inputs": [{"id": "input", "property": "value", "value": "fire request hooks"}],
    }

    assert json.loads(dash_duo.find_element("#output-post-response").text) == {
        "output-1": {"children": "fire request hooks"}
    }

    dash_duo.percy_snapshot(name="request-hooks render")


def test_rdrh002_with_custom_renderer_interpolated(dash_duo):

    renderer = """
        <script id="_dash-renderer" type="application/javascript">
            console.log('firing up a custom renderer!')
            const renderer = new DashRenderer({
                request_pre: () => {
                    var output = document.getElementById('output-pre')
                    if(output) {
                        output.innerHTML = 'request_pre was here!';
                    }
                },
                request_post: () => {
                    var output = document.getElementById('output-post')
                    if(output) {
                        output.innerHTML = 'request_post!!!';
                    }
                }
            })
        </script>
    """

    class CustomDash(Dash):
        def interpolate_index(self, **kwargs):
            return """<!DOCTYPE html>
            <html>
                <head>
                    <title>My App</title>
                </head>
                <body>

                    <div id="custom-header">My custom header</div>
                    {app_entry}
                    {config}
                    {scripts}
                    {renderer}
                    <div id="custom-footer">My custom footer</div>
                </body>
            </html>""".format(
                app_entry=kwargs["app_entry"],
                config=kwargs["config"],
                scripts=kwargs["scripts"],
                renderer=renderer,
            )

    app = CustomDash()

    app.layout = html.Div(
        [
            dcc.Input(id="input", value="initial value"),
            html.Div(
                html.Div(
                    [
                        html.Div(id="output-1"),
                        html.Div(id="output-pre"),
                        html.Div(id="output-post"),
                    ]
                )
            ),
        ]
    )

    @app.callback(Output("output-1", "children"), [Input("input", "value")])
    def update_output(value):
        return value

    class DashView(BaseDashView):
        dash = app

    dash_duo.start_server(DashView)

    input1 = dash_duo.find_element("#input")
    dash_duo.clear_input(input1)

    input1.send_keys("fire request hooks")

    dash_duo.wait_for_text_to_equal("#output-1", "fire request hooks")
    assert dash_duo.find_element("#output-pre").text == "request_pre was here!"
    assert dash_duo.find_element("#output-post").text == "request_post!!!"

    dash_duo.percy_snapshot(name="request-hooks interpolated")
