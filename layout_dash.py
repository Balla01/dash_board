#!/usr/bin/env python
# coding: utf-8

# In[2]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State#, Event
import random
import plotly
import plotly.express as px
import dash_bootstrap_components as dbc


# In[2]:


app = dash.Dash(__name__)
app.css.append_css({
"external_url": "  https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
})

# Bootstrap Javascript.
app.scripts.append_script({
"external_url": "https://code.jquery.com/jquery-3.2.1.slim.min.js"
})
app.scripts.append_script({
"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
})


# In[5]:


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App
df = px.data.gapminder()
print(df.columns)

# Build the layout to define what will be displayed on the page
app.layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.H1("The Title of Our App")
       ], width=8)
    ], justify="center")])


# In[3]:


app.layout = html.Div([
    html.H1('SALES DASHBOARD'),
    html.Div(children='''
        Supermarket Shop.
    ''')])


# In[6]:


if __name__ == '__main__':
    app.run_server(debug=True,port=4050)


# In[3]:


import pandas as pd
df=pd.read_csv(r'C:\Users\sairaj\Downloads\Sales.csv')


# In[4]:


df.head(3)


# In[48]:


df['YEAR']=df['YEAR'].astype(str)
df['MONTH']=df['MONTH'].astype(str)


# In[67]:


def building(a,b):
    df1=df.loc[df['YEAR']==a]
    df2=df1.loc[df['MONTH']==b]
    return df2


# In[72]:


z=building('2022','2')


# In[63]:


pivot_7 = pd.pivot_table(df,index=['PRODUCT'],aggfunc= 'sum')
pivot_7['PRODUCT'] = pivot_7.index


# In[73]:


fig4 = px.bar(z, x="TOTAL SELLING VALUE", y="PRODUCT", orientation='h')


# In[74]:


fig4


# In[ ]:





# In[56]:


df1


# In[ ]:





# In[ ]:





# In[41]:


pivot_1 = pd.pivot_table(df,index=['MONTH'],aggfunc= 'sum')
pivot_6 = pd.pivot_table(df,index=['YEAR'],aggfunc= 'sum')


# In[46]:


pivot_1['MONTH'] = pivot_1.index


# In[112]:


pivot_3 = pd.pivot_table(df,index=['CATEGORY'],aggfunc= 'sum')

pivot_3['CATEGORY'] = pivot_3.index


# In[113]:


fig3 = px.treemap(pivot_3,path=[px.Constant("Category"), 'CATEGORY'],values='TOTAL SELLING VALUE')


# In[114]:


fig3


# In[43]:


pivot_6


# In[49]:


pivot = pd.pivot_table(df,index=['DAY'],aggfunc= 'sum')


# In[50]:


pivot


# In[51]:


pivot['DAY'] = pivot.index


# In[52]:


pivot


# In[81]:


pivot = pd.pivot_table(df,index=['DAY'],aggfunc= 'sum')
pivot['DAY'] = pivot.index


# In[82]:


pivot


# In[94]:


fig6 = px.area(pivot, x='DAY', y='TOTAL SELLING VALUE')


# In[95]:


fig6


# In[9]:


pivot_1 = pd.pivot_table(df,index=['CATEGORY'],aggfunc= 'sum')


# In[10]:


pivot_1


# In[14]:


pivot_4 = pd.pivot_table(df,index=['SALE TYPE'],aggfunc= 'sum')
pivot_5 = pd.pivot_table(df,index=['PAYMENT MODE'],aggfunc= 'sum')


# In[15]:


pivot_4['SALE TYPE'] = pivot_4.index
pivot_5['PAYMENT MODE'] = pivot_5.index


# In[16]:


pivot_4


# In[19]:


fig1 = px.pie(pivot_4, values='TOTAL SELLING VALUE', names='SALE TYPE',hole=.3)


# In[20]:


fig1 


# In[31]:


pivot_5


# In[34]:


fig2 = px.pie(pivot_5, values='TOTAL SELLING VALUE', names='PAYMENT MODE',hole=.3)


# In[35]:


fig2


# In[ ]:





# In[8]:


df['CATEGORY'].unique()


# In[6]:


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App

# Build the layout to define what will be displayed on the page
app.layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.H1("The Title of Our App")
       ], width=12)
    ], justify="center"),
    
    dbc.Row([
        dbc.Col([
             html.Div([
                 html.Div([
            html.Label('Dropdown'),
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'Deaths', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'Cases', 'value': 'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container'),

    ],className='row'),  
                 
            
        ], width=6),
        
        dbc.Col([
            html.Label('Radio Items'),
            dcc.Graph(id='linechart'),
        ], width=6)
        ]),
        
    
    dbc.Row([
        dbc.Col([
            html.Label('Slider'),
            dcc.Slider(min=0, max=10, step=1, value=5),
        ], width=6),
        dbc.Col([
            html.Label('Text Input'),
            html.Br(),
            dcc.Input(value='Initial text', type='text'),
        ], width=6)
    ])
])

# callback is used to create app interactivity
#@callback()
@app.callback(
    Output('dd-output-container', 'children'),
    Input('linedropdown', 'value')
)
def  update_table(input_value):
    return html.Div(
        [
            dcc.Graph(
                id='plots',
                figure=go.Figure(
                    data = [go.Scatter(x = df[input_value],y = df['SELLING PRICE'],mode = 'markers',name = 'sales_price')],
                    
                    ))
        ],className = "Big_Div")           


# Run the App
if __name__ == '__main__':
    app.run_server(port=8001)


# In[ ]:





# In[ ]:





# In[39]:


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App

# Build the layout to define what will be displayed on the page
app.layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.H1("Customer Sales Analysis")
       ], width=12)
    ], justify="center"),
    
    dbc.Row([
       dbc.Col([
           html.H2("Total Sales 4014119$")
       ], width=4),
        dbc.Col([
           html.H2("Total profit 68907.92$")
       ], width=4),
        dbc.Col([
           html.H2("Total profit% 17.16")
       ], width=4)
    ]),
    
    
    dbc.Row([
        dbc.Col([
             html.Div([
                 html.Div([
            html.Label('Dropdown'),
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'Deaths', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'Cases', 'value': 'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container'),

    ],className='row'),  
                 
            
        ], width=6),
        
        dbc.Col([
            html.Label('Radio Items'),
            dcc.Graph(id='linechart'),
        ], width=6)
        ]),
        
    
    dbc.Row([
        dbc.Col([
            
            
            html.Div([
                 html.Div([
            html.Label('Dropdown'),
            dcc.Dropdown(id='linedropdown01',
                options=[
                         {'label': 'Deaths', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'Cases', 'value': 'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container01'),

    ],className='row'), 
            
            
            
        ], width=6),
        dbc.Col([
            
            html.Div([
                 html.Div([
            html.Label('Dropdown'),
            dcc.Dropdown(id='linedropdown@9',
                options=[
                         {'label': 'Deaths', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'Cases', 'value': 'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container@9'),
            
            
        ], width=6)
    ])
])

# callback is used to create app interactivity
#@callback()
@app.callback(
    Output('dd-output-container', 'children'),
    Input('linedropdown', 'value')
)
def  update_table(input_value):
    return dcc.Graph(figure=px.pie(pivot_4, values=input_value, names='SALE TYPE',hole=.3))   
            
                
@app.callback(
    Output('dd-output-container01', 'children'),
    Input('linedropdown01', 'value')
)
def  update_table(input_value):
    return dcc.Graph(figure=px.pie(pivot_5, values=input_value, names='PAYMENT MODE',hole=.3)) 

# Run the App
if __name__ == '__main__':
    app.run_server(port=8001)


# In[ ]:


def  update_table(input_value):
    return html.Div(
        [
            dcc.Graph(
                id='plots',
                figure=px.pie(pivot_4, values=input_value, names='SALE TYPE',hole=.3)   
            )
        ],className = "Big_Div")           


# # maincode

# In[111]:


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Incorporate data into App

# Build the layout to define what will be displayed on the page
app.layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.H1("Customer Sales Analysis")
       ], width=12)
    ], justify="center"),
    
    dbc.Row([
       dbc.Col([
           html.H2("Total Sales 4014119$")
       ], width=4),
        dbc.Col([
           html.H2("Total profit 68907.92$")
       ], width=4),
        dbc.Col([
           html.H2("Total profit% 17.16")
       ], width=4)
    ]),
    
    
    dbc.Row([
        dbc.Col([
             html.Div([
                 html.Div([
            html.Label('Sales Type'),
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'TOTAL BUYING VALUE', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'TOTAL SELLING VALUE', 'value': 'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container'),

    ],className='row'),  
                 
            
        ], width=6),
        
        dbc.Col([
            
            html.Div([
                 html.Div([
            html.Label('select year'),
             dcc.RadioItems(id='linedropdown@1',
                options=['2021','2022'],
                value='2021'
               
            ),
            ],className='six columns'),
                
                html.Div([
            html.Label('select month'),
            dcc.Dropdown(id='linedropdown@2',
                options=[
                         {'label': 'JAN', 'value': '1'},
                         {'label': 'FEB', 'value': '2'},
                    {'label': 'MAR', 'value': '3'},
                    {'label': 'APR', 'value': '4'},
                    {'label': 'MAY', 'value': '5'},
                    {'label': 'JUN', 'value': '6'},
                    {'label': 'JUL', 'value': '7'},
                    {'label': 'AUG', 'value': '8'},
                    {'label': 'SEP', 'value': '9'},
                    {'label': 'OCT', 'value': '10'},
                    {'label': 'NUV', 'value': '11'},
                    {'label': 'DEC', 'value': '12'}
                    
                ],
                value='1',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
                
               html.Div(id='dd-output-container@1'),

    ],className='row'),
            
            
        ], width=6)
        ]),
        
    
    dbc.Row([
        dbc.Col([
            
            
            html.Div([
                 html.Div([
            html.Label('Payment Type'),
                     html.Br(),
            dcc.Dropdown(id='linedropdown01',
                options=[
                         {'label': 'TOTAL BUYING VALUE', 'value':'TOTAL BUYING VALUE'},
                         {'label': 'TOTAL SELLING VALUE','value':'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container01'),

    ],className='row'), 
            
            
            
        ], width=4),
        dbc.Col([
            
            html.Div([
                 html.Div([
            html.Label('Day Statistics'),
                     html.Br(),
            dcc.Dropdown(id='linedropdown@9',
                options=[
                         {'label': 'TOTAL BUYING VALUE', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'TOTAL SELLING VALUE', 'value': 'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container@9'),

    ],className='row'),
            
            
        ], width=4),
        
        dbc.Col([
            html.Label('Different Categories'),
            dcc.Graph(
        id='PAYMENT MODE',
        figure=fig3),
        ], width=4)
    ])
])

# callback is used to create app interactivity
#@callback()
@app.callback(
    Output('dd-output-container', 'children'),
    Input('linedropdown', 'value')
)
def  update_table(input_value):
    return dcc.Graph(figure=px.pie(pivot_4, values=input_value, names='SALE TYPE',hole=.3))   
            
                
@app.callback(
    Output('dd-output-container01', 'children'),
    Input('linedropdown01', 'value')
)
def  update_table(input_value):
    return dcc.Graph(figure=px.pie(pivot_5, values=input_value, names='PAYMENT MODE',hole=.3)) 


@app.callback(
    Output('dd-output-container@1', 'children'),
    Input('linedropdown@1', 'value'),
    Input('linedropdown@2', 'value')
)
def building(a,b):
    df1=df.loc[df['YEAR']==a]
    df2=df1.loc[df['MONTH']==b]
    return dcc.Graph(figure=px.bar(df2, x="TOTAL SELLING VALUE", y="PRODUCT", orientation='h'))
    #return df2
    
@app.callback(
    Output('dd-output-container@9', 'children'),
    Input('linedropdown@9', 'value')
)
def  update_table(input_value):
    return dcc.Graph(figure=px.area(pivot, x='DAY', y=input_value)) 
    


# Run the App
if __name__ == '__main__':
    app.run_server(port=8001)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




