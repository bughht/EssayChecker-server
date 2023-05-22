import pandas as pd
import numpy as np
import os
import json

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

for demo_id in range(3):
    path_essay = "web/database/example_data/essay{}.txt".format(demo_id)
    path_topic = "web/database/example_data/topic{}.txt".format(demo_id)

    data_essay = open(path_essay, "r").readlines()
    data_topic = open(path_topic, "r").readlines()

    essay.append("".join(data_essay))
    topic.append("".join(data_topic))

json0 = json.loads("""{"Content": {
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
json1 = json.loads("""{"Content": {
    "Mark": 80,
    "Comment": "You have addressed the topic and the task well. You have discussed both views and given your opinion with some reasons and examples. However, you could have developed your arguments more fully and provided more specific evidence to support your claims."
  },
  "Statement": {
    "Mark": 85,
    "Comment": "You have a clear thesis statement that expresses your position and outlines the main points of your essay. However, you could have made it more specific and original by adding your own perspective or insight on the issue."
  },
  "Organization": {
    "Mark": 90,
    "Comment": "You have a good structure for your essay, with an introduction, a conclusion, and four body paragraphs. You have used appropriate transition words and phrases to connect your ideas and paragraphs. However, you could have improved the coherence and cohesion of your essay by using more topic sentences and concluding sentences for each paragraph."
  },
  "Readability": {
    "Mark": 85,
    "Comment": "You have used a range of vocabulary and sentence structures to convey your ideas clearly and effectively. However, you could have avoided some repetition and redundancy by using synonyms or paraphrasing."
  },
  "Grammar": {
    "Mark": 80,
    "Comment": "You have demonstrated a good command of grammar and punctuation. However, you made some minor errors that could have been avoided by proofreading your essay carefully."
  },
  "Overall Comment": "Your essay is well-written and shows a good understanding of the topic and the task. However, you can improve your essay by developing your arguments more fully, adding more originality and specificity to your thesis statement, enhancing the coherence and cohesion of your paragraphs, expanding your vocabulary and avoiding repetition, and correcting some minor grammar and punctuation errors."
} """)
json2 = json.loads("""{
  "Content": {
    "Mark": 85,
    "Comment": "You have addressed the topic well and provided relevant examples and reasons to support your opinion. However, you could have elaborated more on the benefits of government-funded research for society and the drawbacks of privately funded research for scientific integrity. You could also have considered some counterarguments or alternative viewpoints to make your essay more balanced and convincing."
  },
  "Statement": {
    "Mark": 90,
    "Comment": "You have clearly stated your opinion in the introduction and restated it in the conclusion. You have also used appropriate transition words and phrases to connect your paragraphs and sentences. However, you could have made your thesis statement more specific and focused by mentioning the main points you will discuss in your body paragraphs."
  },
  "Organization": {
    "Mark": 95,
    "Comment": "You have organized your essay well into four paragraphs: introduction, two body paragraphs, and conclusion. You have also followed a clear structure for each paragraph: topic sentence, supporting sentences, and concluding sentence. However, you could have improved the coherence of your essay by using more cohesive devices such as pronouns, synonyms, or parallel structures to link your ideas."
  },
  "Readability": {
    "Mark": 90,
    "Comment": "You have used a formal and academic tone throughout your essay. You have also varied your sentence length and structure to create interest and avoid monotony. However, you could have improved the readability of your essay by avoiding some repetition of words or phrases such as ``research``, ``responsible``, or ``on the other hand``. You could also have used some punctuation marks such as commas or semicolons to avoid run-on sentences or fragments."
  },
  "Grammar": {
    "Mark": 95,
    "Comment": "You have demonstrated a good command of grammar and vocabulary in your essay. You have used a range of grammatical structures and word forms correctly and accurately. However, you could have avoided some minor errors such as:
    - ``remain contentious issues`` -> ``remains a contentious issue`` (subject-verb agreement)
    - ``the need for positive results is paramount`` -> ``the need for positive results are paramount`` (subject-verb agreement)
    - ``their accountability means that such conflicts of interest are less likely to occur`` -> ``their accountability means that such conflicts of interest is less likely to occur`` (subject-verb agreement)
    - ``Strong checks and balances need to be in place`` -> ``Strong checks and balances needs to be in place`` (subject-verb agreement)"
  },
  "Overall Comment": "Overall, you have written a good essay that meets the requirements of the task. However, you could have improved it by following some of the suggestions I have given above. I hope you find this feedback helpful and useful for your future writing."
}""",
                   strict=False)

json_example = [json0, json1, json2]

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

df = pd.DataFrame({
    "Topic":
    topic,
    "Essay":
    essay,
    "Content_Mark":
    mark_content,
    "Content_Comment":
    comment_content,
    "Statement_Mark":
    mark_statement,
    "Statement_Comment":
    comment_statement,
    "Organization_Mark":
    mark_organization,
    "Organization_Comment":
    comment_organization,
    "Readability_Mark":
    mark_readability,
    "Readability_Comment":
    comment_readability,
    "Grammar_Mark":
    mark_grammar,
    "Grammar_Comment":
    comment_grammar,
    "Overall_Mark":
    np.mean([
        mark_content, mark_statement, mark_organization, mark_readability,
        mark_grammar
    ],
        axis=0),
    "Overall_Comment":
    comment_overall
})

df.to_csv("web/database/data.csv", index=False)
