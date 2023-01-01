from dash import Dash, dcc, html, Input, Output
from decimal import Decimal
import pandas as pd



df = pd.read_csv(r'Normdist3.csv', delimiter = ';', encoding= 'utf-8-sig')

df = pd.DataFrame(df)

df = df.astype(str)

df = df.set_index('number')


def fact(x):
    number = Decimal(1)
    for i in range(1, int(x + 1)):
        number *= i
    return Decimal(number)


app3 = Dash()

app3.layout = html.Div(style={'backgroundColor': '#41B3A3', 'minHeight': '100vh'}, children=[

    html.H1('For calculating the probabilities for different kinds of distributions',
            style={'textAlign': 'center', 'margin-top': '0px', 'margin-bottom': '0px', 'margin-right': '0px',
                   'margin-left': '0px', 'font-family': 'Times New Roman'}),
    html.Div([

        html.Div([
            html.H2('Discrete Ditributions'),

            html.H3('Binomial distribution'),
            dcc.Input(id='first', type='number', value='', placeholder='Number',
                      style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
            dcc.Input(id='second', type='number', value='', placeholder='Success',
                      style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
            dcc.Input(id='third', type='number', value='', placeholder='Probability', min=0, max=1,
                      style={'border': '1px solid black', 'width': '180px', 'height': '40px'}),
            html.Div(id='output', children=['Your value:'], style={'margin-top': '10px'}),

            html.H3('Puasson Distribution'),
            dcc.Input(id='first1', type='number', value='', placeholder='Number',
                      style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
            dcc.Input(id='second1', type='number', value='', placeholder='Success',
                      style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
            dcc.Input(id='third1', type='number', value='', placeholder='Probability', min=0, max=1,
                      style={'border': '1px solid black', 'width': '180px', 'height': '40px'}),
            html.Div(id='output1', children=['Your value:'], style={'margin-top': '10px'}),

            html.H3('Geometrical distribution'),
            dcc.Input(id='second2', type='number', value='~', placeholder='Number of Success',
                      style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
            dcc.Input(id='third2', type='number', value='', placeholder='Probability', min=0, max=1,
                      style={'border': '1px solid black', 'width': '180px', 'height': '40px'}),
            html.Div(id='output2', children=['Your value:'], style={'margin-top': '10px'}),

            html.H3('Negative Binomial Distribution'),
            dcc.Input(id='first3', type='number', value='', placeholder='Number of success',
                      style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
            dcc.Input(id='second3', type='number', value='~', placeholder='Number of last attempt',
                      style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
            dcc.Input(id='third3', type='number', value='', placeholder='Probability', min=0, max=1,
                      style={'border': '1px solid black', 'width': '180px', 'height': '40px'})]),
        html.Div(id='output3', children=['Your value:'], style={'margin-top': '10px'}), ],
        style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top', 'margin': '0px'}
    ),

    html.Div([
        html.H2('Not discrete Distributions'),

        html.H3('Exponential Distribution'),
        dcc.Input(id='erst', value='', type='number', placeholder='Upper limit',
                  style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
        dcc.Input(id='zweit', value='~', type='number', placeholder='Lower limit',
                  style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
        dcc.Input(id='dritte', value='', type='number', placeholder='Lambda',
                  style={'border': '1px solid black', 'width': '180px', 'height': '40px'}),
        html.Div(id='erstoutput', children=['Your value:'], style={'margin-top': '10px'}),

        html.H3('Normal Standard distribution'),
        ('X <='),
        dcc.Input(id='norm1', type='number', value='', placeholder='Upper', min=-3, max=3,
                  style={'border': '1px solid black', 'width': '180px', 'height': '40px'}),
        html.Div(id='normout', children=['Your value:'], style={'margin-top': '10px', 'margin-bottom': '10px'}),
        ('X >='),
        dcc.Input(id='norm2', type='number', value='', placeholder='Lower', min=-3, max=3,
                  style={'border': '1px solid black', 'width': '180px', 'height': '40px'}),
        html.Div(id='normout2', children=['Your value:'], style={'margin-top': '10px'}),

        html.H3('Uniform distribution'),
        dcc.Input(id='upperint', type='text', value='', placeholder='Upper limit',
                  style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
        dcc.Input(id='lowerint', type='text', value='', placeholder='Lower limit',
                  style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
        dcc.Input(id='beg_of_inter', type='text', value='', placeholder='Beg of interval',
                  style={'border': '1px solid black', "margin-right": "15px", 'width': '180px', 'height': '40px'}),
        dcc.Input(id='end_of_inter', type='text', value='', placeholder='End of interval',
                  style={'border': '1px solid black', 'width': '180px', 'height': '40px', 'margin-top': '10px'}),
        html.Div(id='unioutput', children=['Your value:'], style={'margin-top': '10px'})],
        style={'width': '50%', 'display': 'inline-block', 'vertical-align': 'top', 'margin': 0})

])


@app3.callback(
    Output('output', 'children'),
    Input('first', 'value'),
    Input('second', 'value'),
    Input('third', 'value'))
def count_binom_prob(n, k, p):
    nD = Decimal(n)
    kD = Decimal(k)
    pD = Decimal(str(p))
    C = fact(nD) / (fact(nD - kD) * fact(kD))
    final = C * (pD ** kD) * ((1 - pD) ** (nD - kD))
    return f"Your value: {str(final.quantize(Decimal('1.0000')))}"


@app3.callback(
    Output('output1', 'children'),
    Input('first1', 'value'),
    Input('second1', 'value'),
    Input('third1', 'value'))
def count_puasson_prob(n, k, p):
    nD = Decimal(n)
    kD = Decimal(k)
    pD = Decimal(str(p))
    lam = nD * pD
    final = (1 / lam.exp()) * (lam ** kD) / fact(kD)
    return f"Your value: {str(final.quantize(Decimal('1.0000')))}"


@app3.callback(
    Output('output2', 'children'),
    Input('second2', 'value'),
    Input('third2', 'value'))
def count_geometrical_prob(k, p):
    kD = Decimal(k)
    pD = Decimal(str(p))
    final = (pD ** kD) * (1 - pD)
    return f"Your value: {str(final.quantize(Decimal('1.0000')))}"


@app3.callback(
    Output('output3', 'children'),
    Input('first3', 'value'),
    Input('second3', 'value'),
    Input('third3', 'value'))
def count_negative_geometrical_prob(n, k, p):
    nD = Decimal(n)
    kD = Decimal(k)
    pD = Decimal(str(p))
    C = fact(nD + kD - 1) / (fact(kD) * fact(nD - 1))
    final = C * (pD ** nD) * ((1 - pD) ** kD)
    return f"Your value:{str(final.quantize(Decimal('1.0000')))}"


@app3.callback(
    Output('erstoutput', 'children'),
    Input('erst', 'value'),
    Input('zweit', 'value'),
    Input('dritte', 'value'))
def count_exp_dist(upper, lower, param):
    upD = Decimal(upper)
    loD = Decimal(lower)
    parD = Decimal(param)
    final = (-1 * parD * upD).exp() - (-1 * parD * loD).exp()
    return f'Your value: {str(final.quantize(Decimal(1.0000)))}'


@app3.callback(
    Output('normout', 'children'),
    Input('norm1', 'value'))
def count_normal_dist(up1):
    up = str(up1)
    if float(up) >= 0:
        if len(up) == 4:
            for_row = up[0:-1]
            for_col = '0.0' + up[-1]
            return f"Your value: {df.loc[for_row, for_col]}"
        elif len(up) == 3:
            for_row = up
            return f"Your value: {df.loc[for_row, '0.00']}"
        elif len(up) == 1:
            for_row = up + '.0'
            return f"Your value: {df.loc[for_row, '0.00']}"
    elif float(up) < 0:
        if len(up) == 5:
            for_row = up[1:-1]
            for_col = '0.0' + up[-1]
            return f"Your value: {str(1 - Decimal(df.loc[for_row, for_col]))}"
        elif len(up) == 4:
            for_row = up[1:]
            return f"Your value: {str(1 - Decimal(df.loc[for_row, '0.00']))}"
        elif len(up) == 2:
            for_row = up[1:] + '.0'
            return f"Your value: {str(1 - Decimal(df.loc[for_row, '0.00']))}"


@app3.callback(
    Output('normout2', 'children'),
    Input('norm2', 'value'))
def count_normal_dist2(low1):
    low = str(low1)
    if float(low) >= 0:
        if len(low) == 4:
            for_row = low[:-1]
            for_col = '0.0' + low[-1]
            return f"Your value: {str(1 - Decimal(df.loc[for_row, for_col]))}"
        elif len(low) == 3:
            for_row = low
            return f"Your value: {str(1 - Decimal(df.loc[for_row, '0.00']))}"
        elif len(low) == 1:
            for_row = low + '.0'
            return f"Your value: {str(1 - Decimal(df.loc[for_row, '0.00']))}"
    elif float(low) < 0:
        if len(low) == 5:
            for_row = low[1:-1]
            for_col = '0.0' + low[-1]
            return f"Your value: {df.loc[for_row, for_col]}"
        elif len(low) == 4:
            for_row = low[1:]
            return f"Your value: {df.loc[for_row, '0.00']}"
        elif len(low) == 2:
            for_row = low[1:] + '.0'
            return f"Your value: {df.loc[for_row, '0.00']}"


@app3.callback(
    Output('unioutput', 'children'),
    Input('upperint', 'value'),
    Input('lowerint', 'value'),
    Input('beg_of_inter', 'value'),
    Input('end_of_inter', 'value'))
def count_uniform(up, low, beg, enda):
    upD = Decimal(up)
    loD = Decimal(low)
    begD = Decimal(beg)
    endaD = Decimal(enda)
    integral = 1 / (upD - loD)

    if begD <= endaD:
        ans = integral * min(endaD, upD) - integral * max(loD, begD)
        return f"Your value: {str(ans.quantize(Decimal('1.000')))}"
    else:
        ans = 'End of the interval cannot be more than the beggining of the interval'
        return ans


if __name__ == '__main__':
    app3.run_server(debug=False, port=4200)
