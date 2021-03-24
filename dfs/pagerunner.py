import pandas as pd
from IPython.display import Image, HTML
from datetime import datetime

# convert link to html tags 
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

# Grab raw data to convert to html pages.
dfs = pd.read_csv("inputs/dfs.csv")
fd = pd.read_csv("inputs/fanduel.csv")
dk = pd.read_csv("inputs/draftkings.csv")
st = pd.read_csv("inputs/statline.csv")
dfs = dfs.drop("Unnamed: 0", axis=1)
fd = fd.drop("Unnamed: 0", axis=1)
dk = dk.drop("Unnamed: 0", axis=1)
st = st.drop("Unnamed: 0", axis=1)

# Grab timestamp.
ts = datetime.now()
ts = ts.strftime("%b %d, %Y %I:%M %p")
ts = "Last Updated: " + ts

# Highlights given player row to indicate hot/cold status for 19 columns.
def highlight_dfs(df):
    if df.Hot > 0.0 and df.Hot < 0.5: return ['background-color: #ff9999']*19
    elif df.Hot >= 0.5 and df.Hot < 1.0: return ['background-color: #ff6666']*19
    elif df.Hot >= 1.0 and df.Hot < 1.5: return ['background-color: #ff3333']*19
    elif df.Hot >= 1.5: return ['background-color: #ff0000']*19
    elif df.Cold > 0.0 and df.Cold < 0.5: return ['background-color: #99e6ff']*19
    elif df.Cold >= 0.5 and df.Cold < 1.0: return ['background-color: #66d9ff']*19
    elif df.Cold >= 1.0 and df.Cold < 1.5: return ['background-color: #33ccff']*19
    elif df.Cold >= 1.5: return ['background-color: #00bfff']*19
    else: return ['background-color: white']*19

# Highlights given player row to indicate hot/cold status for 14 columns.
def highlight_fd(df):
    if df.Hot > 0.0 and df.Hot < 0.5: return ['background-color: #ff9999']*14
    elif df.Hot >= 0.5 and df.Hot < 1.0: return ['background-color: #ff6666']*14
    elif df.Hot >= 1.0 and df.Hot < 1.5: return ['background-color: #ff3333']*14
    elif df.Hot >= 1.5: return ['background-color: #ff0000']*14
    elif df.Cold > 0.0 and df.Cold < 0.5: return ['background-color: #99e6ff']*14
    elif df.Cold >= 0.5 and df.Cold < 1.0: return ['background-color: #66d9ff']*14
    elif df.Cold >= 1.0 and df.Cold < 1.5: return ['background-color: #33ccff']*14
    elif df.Cold >= 1.5: return ['background-color: #00bfff']*14
    else: return ['background-color: white']*14

# Adds fire or ice emoji for respective hot/cold status.
def emojize(df):
    for i in range(len(df)):
        if df['Hot'][i+1] > 0.0: df['Name'][i+1] = df['Name'][i+1] + ('\n🔥')
        if df['Hot'][i+1] >= 1.0: df['Name'][i+1] = df['Name'][i+1] + ('🔥')
        if df['Hot'][i+1] >= 2.0: df['Name'][i+1] = df['Name'][i+1] + ('🔥')
        if df['Cold'][i+1] > 0.0: df['Name'][i+1] = df['Name'][i+1] + ('\n❄️')
        if df['Cold'][i+1] >= 1.0: df['Name'][i+1] = df['Name'][i+1] + ('❄️')
        if df['Cold'][i+1] >= 2.0: df['Name'][i+1] = df['Name'][i+1] + ('❄️')
    return df

# Error Handling

# Players that don't have a BBall Ref picture, as of 8/7/20.
no_pic_list = ["Paul Watson", "Donta Hall"]

# Player names that don't match to our in-house data.
special_names =       {"Luka Dončić": "Luka Doncic", 
                       "Luka Šamanić": "Luka Samanic", 
                       "Kristaps Porziņģis": "Kristaps Porzingis", 
                       "Nikola Vučević": "Nikola Vucevic",
                       "Jonas Valančiūnas": "Jonas Valanciunas",
                       "Bogdan Bogdanović": "Bogdan Bogdanovic",
                       "Dario Šarić": "Dario Saric",
                       "Timothé Luwawu-Cabarrot": "Timothe Luwawu-Cabarrot",
                       "Džanan Musa": "Dzanan Musa",
                        "Dāvis Bertāns": "Davis Bertans",
                        "Boban Marjanović": "Boban Marjanovic",
                        "Ersan İlyasova": "Ersan Ilyasova",
                        "Anžejs Pasečņiks": "Anzejs Pasecniks",
                       "Bojan Bogdanović": "Bojan Bogdanovic",
                        "Nicolò Melli": "Nicolo Melli",
                        "Nikola Jokić": "Nikola Jokic",
                        "Jusuf Nurkić": "Jusuf Nurkic",
                        "Goran Dragić": "Goran Dragic",
                        "Dennis Schröder" :"Dennis Schroder",
                       "Gary Payton": "Gary Payton II",
                       "Mohamed Bamba": "Mo Bamba",
                       "Wesley Iwundu": "Wes Iwundu",
                        "J.J. Redick": "JJ Redick",
                        "B.J. Johnson": "BJ Johnson"}
# Invert dictionary for use in data grabbing.
inv_names = {v: k for k, v in special_names.items()}

# Creates an HTML page based on input DataFrame and respective coloring.
'''
Args: 
    df: input DataFrame
    out: name of output HTML file (refer to main pages for correct naming)
    coloring: hot/cold highlights for HTML page
'''
def gen_page(df, out, coloring):
    # Read games file to grab slug code, for BBall Ref data.
    games = pd.read_csv('games.csv').loc[:,['name','slug']]
    trans_games = games.set_index('name').T
    img_dict = trans_games.to_dict('list')
    
    # Update data in Name and Picture column to display link to BBall Ref page and profile picture, respectively.
    images = []
    names = []
    for i in df["Name"]:
        display_name = i
        if i in inv_names:
            display_name = inv_names[i]
        code = "https://raw.githubusercontent.com/BerkeleySportsAnalytics/sagb-site/master/images/profile_picture.jpg"
        # Catch errors when player is not tracked in games file.
        if img_dict.get(display_name) != None:
            if display_name not in no_pic_list:
                # BBall Ref image hyperlink.
                code = "https://d2cwpp38twqe55.cloudfront.net/req/202005142/images/players/" + img_dict.get(display_name)[0] + ".jpg"
            # BBall Ref player profile hyperlink and embed code.
            display_name = "<a href=\"https://www.basketball-reference.com/players/" + \
                img_dict.get(display_name)[0][0] + "/" + img_dict.get(display_name)[0] + ".html\" target=\"_blank\">" + display_name + "</a>"
        images.append(code)
        names.append(display_name)
    df["Picture"] = images
    df["Name"] = names
    
    # Change the picture column to the second column in order.
    cols = df.columns.tolist()
    cols = [cols[0]] + cols[-1:] + cols[1:-1]
    df = df[cols]
    pd.set_option('display.max_colwidth', -1)
    df.index +=1
    
    # Header of output HTML file.
    pre = (
        "<head>\n<script src=\"sorttable.js\"></script>\n"
        "<link rel=\"stylesheet\" href=\"df_styles.css\">\n</head>\n"
    )
    pre = pre + ts + "\n"
    pre += (
        "\n<body>\n<div id=\"filter\">\n<input type=\"text\" id=\"name\" onkeyup=\"nameSearch()\" placeholder=\"Search for name...\">\n"
        "<input type=\"text\" id=\"team\" onkeyup=\"teamSearch()\" placeholder=\"Search for team...\">\n"
        "<label for=\"pos\">Search by position:</label>\n"
        "<select id=\"pos\" onchange=\"posSearch()\" class='form-control'>\n"
        "<option></option>\n"
        "<option>PG</option>\n"
        "<option>SG</option>\n"
        "<option>SF</option>\n"
        "<option>PF</option>\n"
        "<option>C</option>\n"
        "</select>\n"
        "</div>\n\n"
    )
    
    # Footer of output HTML file.
    post = (
        "\n"
        "\n<script src=\"main.js\"></script>"
        "\n</body>"
        )
    
    # Render dataframe as HTML.
    if coloring is not None:
        images = ['<img src="' + image + '" width="60">' for image in images]
        df["Picture"] = images
        df = emojize(df)
        body = df.style.apply(coloring, axis=1).hide_columns(['Hot', 'Cold']).render()
    else:
        html = HTML(df.to_html(escape=False ,formatters=dict(Picture=path_to_image_html)))
        body = html.data

    # Generate HTML and add configuration for output tables, so JavaScript functions can run properly.
    body = body.replace("<table id=", "<table ignore=", 1)
    body = body.replace("<table ", "<table id=\"tbl\" class=\"sortable\" ", 1)
    a = pre + body + post
    # write html to file
    with open(out, 'w', encoding="utf-8") as f:
        f.write(a)
    return df

# Create the page for given output.
gen_page(dfs, 'dfs.html', highlight_dfs)
gen_page(fd, 'fd.html', highlight_fd)
gen_page(dk, 'dk.html', highlight_fd)
gen_page(st, 'st.html', None)