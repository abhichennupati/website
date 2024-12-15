import requests
import json
import os

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": os.getenv("GITHUB_API_AUTH"),
    "X-GitHub-Api-Version": "2022-11-28"
}

# Gathers github information, and returns a HTML string representing the list of events
# TODO add writing stuff, links for repos owned by me, limit each repo to only be visible once
def get_user_info():
    r = requests.get("https://api.github.com/users/abhichennupati/events", headers=headers)
    json_version = json.loads(r.content)

    events = []
    repos = []
    for i in json_version:
        name = i['repo']['name']
        if name in repos:
            continue

        repos.append(name)

        if name[:14] == "abhichennupati":
            name = """<a href=\"""" + "https://www.github.com/" + name +  """\">""" + name + """</a>"""

        type = i['type']
        if type == "WatchEvent":
            type = "Starred"
        elif type == "CreateEvent":
            type = "Created"
        elif type == "PushEvent":
            type = "Pushed to"

        time = "[" + i['created_at'].split("T")[0].replace('-', '.') + "]"
        events.append(f"""
                            <p>
                                <span class="date">{time}</span><br />
                                {type + " " + name}
                            </p>
            """)


    html_events = ""
    for i in events:
        html_events = html_events + i
    return html_events

# Basic function for returning HTML, with the response from get_user_info() where it should be
def get_main_html():
    return """<!doctype html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>home</title>
            <style>
                body {
                    font-family: "Courier New", Courier, monospace;
                    max-width: 600px;
                    margin: 40px auto;
                    padding: 0 20px;
                    background: #ffe4cc; /* Warmer, peachy sand color */
                    color: #4a2511; /* Rich brown for main text */
                    line-height: 1.4;
                }

                h1 {
                    font-size: 16px;
                    font-weight: normal;
                    margin-bottom: 25px;
                    color: #733821; /* Terracotta for headers */
                }

                p {
                    margin-bottom: 20px;
                    font-size: 14px;
                }

                a {
                    color: #a65d37; /* Warm terracotta for links */
                    text-decoration: none;
                }

                a:hover {
                    color: #8b3a15; /* Darker terracotta for hover */
                    text-decoration: underline;
                }

                .navigation {
                    margin: 30px 0;
                    border-top: 1px solid #a65d37;
                    border-bottom: 1px solid #a65d37;
                    padding: 10px 0;
                }

                .navigation a {
                    margin-right: 15px;
                }

                .main-content {
                    margin-top: 30px;
                }

                .date {
                    color: #965a3e; /* Warm brown for dates */
                }
            </style>
        </head>
        <body>
            <div class="navigation">
                <a href="/">home</a>
                <a href="writing">writing</a>
                <a href="https://github.com/abhichennupati">github</a>
                <a href="/Users/abhi/Desktop/AbhiCV2024.pdf">resume</a>
                <a href="https://www.linkedin.com/in/abhiram-chennupati-b02058198/"
                    >linkedin</a
                >
            </div>

            <div class="main-content">

                <p> Hi. I'm Abhi. this space serves as an archive of my thoughts and work. </p>

                <h1>Recent Things</h1>

                """ + get_user_info() + """

                <p>
                    <span class="date">[contact]</span><br />
                    >>>
                    <a href="mailto:achennupati03@berkeley.edu"
                        >achennupati03@berkeley.edu</a
                    ><br />
                </p>
            </div>
        </body>
    </html> """


def get_writing_page():
    return
