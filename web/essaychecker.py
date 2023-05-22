import pandas as pd
import numpy as np
import os
import json
from flask import Flask, jsonify
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

essay = []
topic = []
mark_content = []
mark_statement = []
mark_organization = []
mark_readability = []
mark_grammar = []
mark_overall = []

comment_content = []
comment_statement = []
comment_organization = []
comment_readability = []
comment_grammar = []
comment_overall = []

df=pd.DataFrame(columns=["Topic","Essay","Mark_Content","Comment_Content","Mark_Statement","Comment_Statement","Mark_Organization","Comment_Organization","Mark_Readability","Comment_Readability","Mark_Grammar","Content_Grammar","Mark_Overall","Comment_Overall"])
df.to_csv("web/database/essaychecker.csv",index=False,encoding='utf-8')

path_essay = "web/database/example_data/essay0.txt"
path_topic = "web/database/example_data/topic0.txt"

data_essay = open(path_essay, "r").readlines()
data_topic = open(path_topic, "r").readlines()

essay.append("".join(data_essay))
topic.append("".join(data_topic))

json0 = json.loads("""{
"Content": {
    "Mark": 90,
    "Comment": "You have chosen a significant experience that demonstrates your personal growth and passion for helping others. You have also provided vivid details and emotions that make your essay engaging and memorable. However, you could improve your content by adding some reflection on how this experience has influenced your goals, values, or beliefs."
  },
  "Statement": {
    "Mark": 85,
    "Comment": "You have a clear and concise statement that summarizes the main idea of your essay: 'Rather than being an innocent victim, like the current patient was, I am now the rescuer.' However, you could improve your statement by placing it at the beginning of your essay, rather than at the end. This would help to capture the reader's attention and provide a roadmap for your essay."
  },
  "Organization": {
    "Mark": 95,
    "Comment": "You have a well-organized essay that follows a logical sequence of events. You use transitions and paragraphs to connect your ideas and create a smooth flow. However, you could improve your organization by adding an introduction and a conclusion that frame your essay and restate your main point."
  },
  "Readability": {
    "Mark": 90,
    "Comment": "You have a readable essay that uses clear and concise language and varied sentence structures. You also use punctuation and capitalization correctly. However, you could improve your readability by avoiding some minor errors and inconsistencies."
  },
  "Grammar": {
    "Mark": 85,
    "Comment": "You have a good command of grammar and syntax. You use subject-verb agreement, pronoun-antecedent agreement, and parallelism correctly. However, you could improve your grammar by avoiding some common errors and pitfalls."
  },
  "Overall Comment": "You have written a powerful and compelling essay that showcases your personal growth and passion for helping others. You have also demonstrated your writing skills and abilities. However, you could improve your essay by following the suggestions above."
}""")

json_example = [json0]
#类型转换
for json in json_example:
    for key, value in json.items():
        if key == "Content":
            comment_content.append(value.get("Comment"))
            mark_content.append(value.get("Mark"))
        if key == "Statement":
            comment_statement.append(value.get("Comment"))
            mark_statement.append(value.get("Mark"))
        if key == "Organization":
            comment_organization.append(value.get("Comment"))
            mark_organization.append(value.get("Mark"))
        if key == "Readability":
            comment_readability.append(value.get("Comment"))
            mark_readability.append(value.get("Mark"))
        if key == "Grammar":
            comment_grammar.append(value.get("Comment"))
            mark_grammar.append(value.get("Mark"))
        if key == "Overall Comment":
            comment_overall.append(value)
#增加数据
df2=pd.DataFrame([[topic,essay,mark_content,comment_content,mark_statement,comment_statement,mark_organization,comment_organization,mark_readability,
               comment_readability,mark_grammar,comment_grammar,np.mean([mark_content, mark_statement, mark_organization, mark_readability,mark_grammar],axis=0),comment_overall]]
                ,columns=["Topic","Essay","Mark_Content","Comment_Content","Mark_Statement","Comment_Statement","Mark_Organization","Comment_Organization","Mark_Readability","Comment_Readability","Mark_Grammar","Content_Grammar","Mark_Overall","Comment_Overall"])
               

new_df = pd.concat([df, df2], ignore_index=True)
new_df.to_csv("web/database/essaychecker.csv",index=False)

df_mark = pd.DataFrame({
    "Mark_Content":
    mark_content,
    "Mark_Statement":
    mark_statement,
    "Mark_Organization":
    mark_organization,
    "Mark_Readability":
    mark_readability,
    "Mark_Grammar":
    mark_grammar,
    "Mark_Overall":
    np.mean([
        mark_content, mark_statement, mark_organization, mark_readability,
        mark_grammar
    ],
            axis=0)
})


df_mark.to_csv("web/database/mark.csv", index=False)

df_comment = pd.DataFrame({
    "Comment_Content":
    comment_content,
    "Comment_Statement":
    comment_statement,
    "Comment_Organization":
    comment_organization,
    "Comment_Readability":
    comment_readability,
    "Comment_Grammar":
    comment_grammar,
    "Comment_Overall":
    comment_overall
})
df_comment.to_csv("web/database/remark.csv", index=False)

df3 = pd.read_csv('web/database/essaychecker.csv')

col_essay= df3.loc[:, 'Essay']
col_topic= df3.loc[:, 'Topic']

df4=pd.DataFrame(col_topic)
df5=pd.DataFrame(col_essay)

table1 = df4.to_html(justify='center')
table2 = df5.to_html(justify='center')
table3 = df_comment.to_html(justify='center')

data = {'Content': 90, 'Statement': 85, 'Organization': 95,
        'Readability': 90, 'Grammar': 85, 'Overall': 89.0}

app = Flask(__name__)

@app.route('/')
def index():
    
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())
    ax.set_xlabel('Categories')
    ax.set_ylabel('Marks')
    ax.set_title('Marks Overview')

    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)
    encoded_image = base64.b64encode(image.getvalue()).decode()
    return render_template('index1.html', table1=table1,table2=table2,table3=table3,image=encoded_image)



if __name__ == '__main__':
    app.run(host="localhost", port=8088)
