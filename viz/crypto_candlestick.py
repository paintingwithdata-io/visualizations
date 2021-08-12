import plotly.graph_objects as go


def create_viz(df):
    # Creating the OHLC figure object with the graph_objects module
    fig = go.Figure(
        data=[go.Candlestick(x=df["closetime"],
                             open=df["openprice"],
                             high=df["highprice"],
                             low=df["lowprice"],
                             close=df["closeprice"])],
        layout_title_text="BTC-USD Price Candlestick Chart",
        layout_title_font_size=40)

    return fig
