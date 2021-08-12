import plotly.graph_objects as go


def create_viz(df):
    # Creating the figure object with the graph_objects module
    data = [go.Bar(name=fiatpair, x=df["closetime"], y=df["volume"]) for fiatpair, df in df.groupby(by="pair")]

    fig = go.Figure(data)
    fig.update_layout(barmode="stack", title="Volume by BTC-Fiat pair for 2015-2020", xaxis_title="Date")

    # Return the viz figure
    return fig

    # Additional Options for bar graph manipulation

    # Example updating the layout of the figure data structure
    #  fig.update_layout(title_text="Quote Volume by BTC-Fiat pair for 2018-2020", title_font_size=30)

    # Example updating the trace of the figure data structure
    #  fig.update_traces(y=df["quotevolume"], selector=dict(type="bar"))

    # Example updating the figure trace conditionally with the for_each_trace() method
    # fig.for_each_trace(
    #     lambda trace: trace.update(marker_color="pink") if trace.name == "btcusd" else (),
    # )

    # Example updating the figure axes (x & y)
    #  fig.update_xaxes(showgrid=False)
    #  fig.update_yaxes(showgrid=False)

    # Example updating the figure through the property assignment feature
    #  fig.data[0].marker.line.width = 1
    #  fig.data[0].marker.line.color = "black"
