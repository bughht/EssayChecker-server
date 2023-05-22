import pandas as pd
import base64
import pickle
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px
from ocr import getText
import numpy as np
import cv2 as cv
# from AutoChecker import autochecker

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

database_path = "web/database/data.csv"
database = pd.read_csv(database_path)


# def decode_img(img_raw):
#     # NOTE: decode the image from base64 loaded from POST json file
#     return pickle.loads(base64.b64decode(img_raw))

def Writing_Recognization(img):
    # TODO: recognize the writing in the image
    content = getText(img)
    #TOPIC = ""
    #ESSAY = ""
    # return TOPIC, ESSAY
    return content


def Marking_Commenting(TOPIC, ESSAY):
    # TODO: Mark and Comment the essay with AutoChecker
    result = {}
    return result


@app.route('/')
def index():
    # TODO: index page for the website
    return render_template('index.html', name="hello world")


@app.route('/api/data_upload', methods=['POST'])
def data_upload():
    json_out = {}
    df = pd.read_csv('web/database/data.csv')
    try:
        # img_raw = request.form.get("image")
        # img = decode_img(img_raw)
        # json_out["ID"] = new_id()
        # json_out["status"] = "success"

        # TODO: load the json file
        data_dict = request.form.to_dict()

        Essay = data_dict['essay']
        Topic = data_dict['topic']
        Content_Mark = float(data_dict['Content_Mark'])
        Content_Comment = data_dict['Content_Comment']
        Statement_Mark = float(data_dict['Statement_Mark'])
        Statement_Comment = data_dict['Statement_Comment']
        Organization_Mark = float(data_dict['Organization_Mark'])
        Organization_Comment = data_dict['Organization_Comment']
        Readability_Mark = float(data_dict['Readability_Mark'])
        Readability_Comment = data_dict['Readability_Comment']
        Grammar_Mark = float(data_dict['Grammar_Mark'])
        Grammar_Comment = data_dict['Grammar_Comment']
        Overall_Mark = (Content_Mark + Statement_Mark +
                        Organization_Mark + Readability_Mark + Grammar_Mark)/5.0
        Overall_Comment = data_dict['Overall_Comment']

        # TODO: save the result to database
        df2 = pd.DataFrame({
            "Topic": [Topic],
            "Essay": [Essay],
            "Content_Mark": [Content_Mark],
            "Content_Comment": [Content_Comment],
            "Statement_Mark": [Statement_Mark],
            "Statement_Comment": [Statement_Comment],
            "Organization_Mark": [Organization_Mark],
            "Organization_Comment": [Organization_Comment],
            "Readability_Mark": [Readability_Mark],
            "Readability_Comment": [Readability_Comment],
            "Grammar_Mark": [Grammar_Mark],
            "Grammar_Comment": [Grammar_Comment],
            "Overall_Mark": [Overall_Mark],
            "Overall_Comment": [Overall_Comment
                                ]})
        print(df2)
        df = pd.concat([df, df2], ignore_index=True)
        df.to_csv("web/database/data.csv", index=False)

    except Exception as e:
        json_out["status"] = "fail"
        json_out["error"] = str(e)

    return jsonify(json_out)


@app.route('/history', methods=['GET'])
def history():
    # TODO: return the history result from the database
    df = pd.read_csv('web/database/data.csv')
    col_Overall = df.loc[:, 'Overall_Mark']
    col_Readability = df.loc[:, 'Readability_Mark']
    col_Content = df.loc[:, 'Overall_Mark']
    col_Statement = df.loc[:, 'Statement_Mark']
    col_Organization = df.loc[:, 'Organization_Mark']
    col_Grammar = df.loc[:, 'Grammar_Mark']
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=col_Overall.values,
        mode='lines+markers',
        name='Overall'))

    fig.add_trace(go.Scatter(
        y=col_Readability.values,
        mode='lines+markers',
        name='Readability'))

    fig.add_trace(go.Scatter(
        y=col_Content.values,
        mode='lines+markers',
        name='Content'))

    fig.add_trace(go.Scatter(
        y=col_Statement.values,
        mode='lines+markers',
        name='Statement'))

    fig.add_trace(go.Scatter(
        y=col_Organization.values,
        mode='lines+markers',
        name='Organization'))

    fig.add_trace(go.Scatter(
        y=col_Grammar.values,
        mode='lines+markers',
        name='Grammar'))

    fig.update_layout(
        xaxis_title="ID",
        yaxis_title="Mark",
    )
    graphJSON = json.dumps(
        fig, cls=plotly.utils.PlotlyJSONEncoder, ensure_ascii=False)

    table = df.to_html(justify='center')
    headings = ["ID", "   Content   ", " Statement ",
                "Organization", "Readability", "  Grammar  ", "  Overall  "]
    data = df.loc[:, ["Content_Mark", "Statement_Mark", "Organization_Mark",
                      "Readability_Mark", "Grammar_Mark", "Overall_Mark"]].values
    data = np.vstack([np.arange(1, len(data)+1), data.T]).T.astype(int)

    theadings = ["ID", "Topic"]

    ttable = []
    table = df.loc[:, ["Topic"]].values
    for i, tline in enumerate(table):
        ttable.append([i+1, tline[0]])

    return render_template('history.html', graphJSON=graphJSON, headings=headings, data=data, theadings=theadings, ttable=ttable)


@app.route('/history/<int:id>', methods=['GET'])
def history_id(id):
    # TODO: return the history result of id from the database
    df = pd.read_csv('web/database/data.csv')
    topic = df.loc[id-1, ["Topic"]].values[0]
    essay = df.loc[id-1, ["Essay"]].values[0]
    df_chart = pd.DataFrame({
        'Criteria': ['Readability', 'Content', 'Statement', 'Organization', 'Grammar', 'Overall'], 'Mark': df.loc[id-1, ['Readability_Mark', 'Content_Mark', 'Statement_Mark', 'Organization_Mark', 'Grammar_Mark', 'Overall_Mark']].values,
        'Type': ['Criteria', 'Criteria', 'Criteria', 'Criteria', 'Criteria', 'Overall']
    })
    fig = px.bar(df_chart, x='Criteria', y='Mark', color='Type')
    fig.update_traces(
        width=0.4)
    fig.update_yaxes(
        range=(0, 100)
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    table_comment = (df.loc[id-1, ["Content_Comment", "Statement_Comment", "Organization_Comment",
                                   "Readability_Comment", "Grammar_Comment", "Overall_Comment"]].to_frame()).to_html(justify='center', header=False)
    return render_template('history_id.html', id=id, topic=topic, essay=essay, table_comment=table_comment, graphJSON=graphJSON)


if __name__ == '__main__':
    print(database)
    app.run(host="0.0.0.0", port=8088, debug=True)
