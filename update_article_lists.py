import sys
from bs4 import BeautifulSoup
from pathlib import Path

def move_to_next_page(article, page_num):
  next_filename = "all-articles-"+str(page_num+1)+".html"
  if (not Path(next_filename).exists()):
    f= open("all-articles-"+str(page_num+1)+".html","w+", encoding='cp1252')
    f.write(
      """
      <!DOCTYPE html>
      <!--
        ZeroFour by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)

        Created By Rohan Narayan @rrnarayan1
      -->
      <html>
       <head>
        <title>
         Data Journalism, Sports Analytics Group at Berkeley
        </title>
        <meta charset="utf-8"/>
        <meta content="width=device-width, initial-scale=1, user-scalable=no" name="viewport"/>
        <link href="assets/css/main.css" rel="stylesheet"/>
       </head>
       <body class="left-sidebar is-preload">
        <div id="page-wrapper">
         <!-- Header Wrapper -->
         <div id="header-wrapper">
          <div class="container">
           <!-- Header -->
           <header id="header">
            <div class="inner">
             <!-- Logo -->
             <h1>
              <a href="index.html" id="logo">
               <img src="images/logo1.png" />
              </a>
             </h1>
             <!-- Nav -->
              <nav id="nav">
              </nav>
              <script id="nav-src" curr="dj" src="shared/nav.js"></script>
            </div>
           </header>
          </div>
         </div>
         <!-- Main Wrapper -->
         <div id="main-wrapper">
          <div class="wrapper style2">
           <div class="inner">
            <div class="container">
             <div class="row">
              <div class="col-9 col-12-medium">
               <!-- Article list -->
               <section class="box article-list">
                <h2 class="icon fa-file-text-o">
                 All Articles (Page """+str(page_num+1)+""")
                </h2>
                <!-- Excerpt -->"""+
                article.prettify()+
                """
               </section>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
         <!-- Footer Wrapper -->
         <div id="footer-wrapper">
        </div>
        <script id="footer-src" src="shared/footer.js"></script>
        </div>
        <!-- Scripts -->
        <script src="assets/js/jquery.min.js">
        </script>
        <script src="assets/js/jquery.dropotron.min.js">
        </script>
        <script src="assets/js/browser.min.js">
        </script>
        <script src="assets/js/breakpoints.min.js">
        </script>
        <script src="assets/js/util.js">
        </script>
        <script src="assets/js/main.js">
        </script>
       </body>
      </html>
      """)
  else:
    with open(next_filename, encoding='cp1252') as next_list_articles:
      next_list_articles_soup = BeautifulSoup(next_list_articles, "html5lib")

    current_len = len(next_list_articles_soup.findAll("article"))

    if (current_len >= 10):
      last_article = next_list_articles_soup.findAll("article")[-1].extract()

    next_list_articles_soup.section.article.insert_before(article)

    with open(next_filename,"w", encoding='cp1252') as next_list_articles_file:
      next_list_articles_file.write(str(next_list_articles_soup.prettify()))

    if (current_len >= 10):
      move_to_next_page(last_article, page_num+1)


article_name = sys.argv[1]
filename = "articles/"+article_name+".html"
with open(filename, encoding='utf-8') as article:
    article_soup = BeautifulSoup(article, "html5lib")

with open("all-articles-1.html", encoding='cp1252') as list_articles:
  list_articles_soup = BeautifulSoup(list_articles, "html5lib")

current_len = len(list_articles_soup.findAll("article"))

if (current_len >= 10):
  last_article = list_articles_soup.findAll("article")[current_len-1].extract()
  move_to_next_page(last_article, 1)

article_new = list_articles_soup.new_tag("article")
article_new['class'] = 'box excerpt'

byline = str(article_soup.findAll("h4")[0])[4:-5]
author = byline[:byline.find("|")]
date = byline[byline.find("|")+2:]

title = str(article_soup.findAll("h2")[0])[4:-5]

article_parsed = BeautifulSoup("""
<a href='"""+filename+"""' class='image left'><img src='images/dj-pics/"""+article_name+"""/main.jpg' alt='' /></a>
<div>
  <header>
    <span class='date'>"""+date+"""</span>
    <h3><a href='"""+filename+"""'>"""+title+"""</a></h3>
    <div>"""+author+"""</div>
  </header>
</div>
  """, "html.parser")

article_new.append(article_parsed)


list_articles_soup.section.article.insert_before(article_new)
list_articles_result = list_articles_soup.prettify()

with open("all-articles-1.html","w") as list_articles_file:
  list_articles_file.write(list_articles_result)
