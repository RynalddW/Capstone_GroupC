# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:28:48 2020

@author: 100008706
"""
import pandas as pd
import dash
import dash_core_components as dcc 	#This library will give us the dashboard elements (pie charts, scatter plots, bar graphs etc)
import dash_html_components as html 	#This library allows us to arrange the elements from dcc in a page as is done using html/css (how the internet generally does it)
import plotly.express as px



#Create the Das server and plost using plotly express
def get_dash(server):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, 
                    server=server,
                    routes_pathname_prefix='/dashapp/',
                    external_stylesheets=external_stylesheets
                    )
    
    
    dfslist = data()
     
    styles = get_styles()
    
    fig = px.scatter_matrix(dfslist, dimensions=["TG", "Weight on Bit (WOB)", "Torque (TRQ)","(Rate of Penetration) ROP" ], color="(Rate of Penetration) ROP",  title="Temperature, Torque and Weight-on-Bit versus ROP(Rate of Penetration)", width=1600, height=1000)
    
    fig.update_xaxes(
            rangeslider_visible=True,
            tickformatstops = [
            dict(dtickrange=[None, 100]),
            dict(dtickrange=[100, 500]),
            dict(dtickrange=[500, 1000]),
            dict(dtickrange=[1000, 1500]),
            dict(dtickrange=[1500, 3000]),
            dict(dtickrange=[3000, 5000])
        ]
    )
  
        
    app.layout = html.Div([
        html.H5("A Graphical representation of the 3 Input variables versus ROP(Rate of Penetration"),
        html.A("Go to Home Page", href="/", style=styles["button_styles"]),
        html.Div("", id='my-output',
                 style=styles["text_styles"] ),
        dcc.Graph(
            id='Solar',
            figure = fig
        ),
          
    ])

    return app    
    
#Function to read the input Data File
def data():
         
    
    dfslist = pd.read_csv('MU_1X_Drilling_Data.csv')
     
    return dfslist


#To make things look pretty   
def get_styles():
    """
    Very good for making the thing beautiful.
    """
    base_styles = {
        "text-align": "center",
        "border": "1px solid #ddd",
        "padding": "7px",
        "border-radius": "2px",
    }
    text_styles = {
        "background-color": "#eef",
        "margin": "auto",
        "width": "70%"
    }
    text_styles.update(base_styles)

    button_styles = {
        "text-decoration": "none",
    }
    button_styles.update(base_styles)

    fig_style = {
        "padding": "10px",
        "width": "80%",
        "margin": "auto",
        "margin-top": "5px"
    }
    fig_style.update(base_styles)
    return {
        "text_styles" : text_styles,
        "base_styles" : base_styles,
        "button_styles" : button_styles,
        "fig_style": fig_style,
    } 
