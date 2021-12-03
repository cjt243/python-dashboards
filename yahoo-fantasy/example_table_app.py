# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

theme = dbc.themes.FLATLY

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


# def generate_table(dataframe, max_rows=10):
#     return dbc.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ],bordered=True,dark=True,hover=True,responsive=True,striped=True)


app = dash.Dash(__name__,external_stylesheets=[theme])

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, dark=True, responsive=True)
])

if __name__ == '__main__':
    app.run_server(debug=True)
