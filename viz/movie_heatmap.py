import plotly.graph_objects as go


def create_viz(df):
    ######
    # Performing any necessary data manipulation on the movies dataset
    ######

    # This section does the following:
    # 1. Sets an index with the columns that will be unchanged
    # 2. splits the column that will be changed (genre) and explodes the dataframe to create a row for each genre
    # 3. Resets the index after the new dataframe has been instantiated
    df = df.set_index(["idx", "title", "ReleaseYear", "RunTime", "Rating", "NumberOfVotes"])\
            .apply(lambda i: i.str.split(',').explode()).reset_index()

    # Creating a variable vote number condition and filtering on the condition
    df["VolumeMin"] = df.groupby(["genres", "ReleaseYear"])["NumberOfVotes"].transform('mean')

    # Apply Variable Vote Filter
    df = df[df["NumberOfVotes"] > df["VolumeMin"]].reset_index(drop=True)

    # Creating a rank for each movie in the dataframe
    df["Rank"] = df.groupby(["genres", "ReleaseYear"])["Rating"].rank("first", ascending=False)

    # Filter dataframe to the top 10 Action movies only
    df = df[(df["Rank"] <= 10) & (df["genres"] == "Action")
            & (df["ReleaseYear"] >= 2010) & (df["ReleaseYear"] < 2020)].reset_index(drop=True)

    ######
    # Creating the initial visualization
    ######
    fig = go.Figure(data=go.Heatmap(
        z=df["NumberOfVotes"].tolist(),
        x=df["ReleaseYear"].tolist(),
        y=df["Rank"].tolist(),
        ids=df["title"].tolist()
    ))

    # Loop to create all annotations
    for y in df["Rank"].unique():
        for x in df["ReleaseYear"].unique():
            # Creating a title string object to push to the annotation
            title_text = df.loc[(df["Rank"] == y) & (df["ReleaseYear"] == x)]["title"].reset_index(drop=True)[0]
            # Add the title as a cartesian annotation
            fig.add_annotation(x=x, y=y,
                               text=title_text,
                               showarrow=False)

    fig.update_traces(text=df["title"])
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(title_text="Top Ranked IMDb Movies by Genre & Decade")

    return fig
