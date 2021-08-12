import plotly.express as px


def create_viz(df):
    # Creating the OHLC figure object with the graph_objects module
    fig = px.sunburst(df, path=["quotename", "basename"], values="volume", hover_data=["basesymbol"])

    # Updating the title & format
    fig.update_layout(title_text="Cryptocurrency Market Snapshot", title_font_size=40)

    return fig
