import pandas as pd
import dash
from dash import dcc, html

try:
    df = pd.read_excel(r'C:\Users\coses\Agent-zero-data\tmp\GitTest\Hello-Agent\Hello-Agent\export.xls', skiprows=7).dropna()
except Exception as e:
    raise SystemExit(f"Data error: {e}")

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Data Dashboard'),
    dcc.Graph(
        figure={
            'data': [{
                'x': df.columns,
                'y': df.iloc[i],
                'type': 'line',
                'name': f'Series {i+1}'
            } for i in range(min(10, len(df)))]
        }
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)
