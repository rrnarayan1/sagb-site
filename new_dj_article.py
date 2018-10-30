import sys
import os

f= open("articles/"+sys.argv[1]+".html","w+")
os.mkdir("images/dj-pics/"+sys.argv[1])

title = input("Enter Title: ")

f.write("""
  <!DOCTYPE HTML>
<!--
  ZeroFour by HTML5 UP
  html5up.net | @ajlkn
  Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
  <head>
    <title>"""+title+""" | Sports Analytics Group at Berkeley</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="../assets/css/main.css" />
  </head>
  <body class="right-sidebar is-preload">
    <div id="page-wrapper">

      <!-- Header Wrapper -->
        <div id="header-wrapper">
          <div class="container">

            <!-- Header -->
              <header id="header">
                <div class="inner">

                  <!-- Logo -->
                    <h1><a href="../index.html" id="logo"><img src="../images/logo1.png" /></a></h1>

                  <!-- Nav -->
                    <nav id="nav">
                    </nav>
                    <script id="nav-src" curr="dj" folder="up" src="../shared/nav.js"></script>
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
                  <div class="col-8 col-12-medium">
                    <div id="content">

                      <!-- Content -->

                        <article>
                          <header class="major">
                            <h2>"""+title+"""</h2>
                            <h4>By <a href="https://google.com" target="_blank">Rohan Narayan</a> | September 11, 2018</h4>
                          </header>
                          <span class="image featured"><img src="../images/dj-pics/"""+sys.argv[1]+"""/main.jpg" alt="" /></span>
                        </article>

                    </div>
                  </div>
                  <div class="col-4 col-12-medium">
                    <div id="sidebar">
                    <!-- <div id="sidebar-sticky"> -->

                      <!-- Sidebar -->

                        <section>
                          <header class="major">
                            <h2>Related Articles</h2>
                          </header>
                          <ul id="recent-articles" class="style2">
                          </ul>
                          <script id="recent-articles-src" src="../shared/recent-articles.js"></script>
                        </section>

                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="wrapper style3">
            <div class="inner">
              <div class="container">
                <div class="row">
                  <div class="col-8 col-12-medium">

                    <!-- Article list -->
                      <section class="box article-list">
                        <h2 class="icon fa-file-text-o">Recent Posts</h2>

                        <!-- Excerpt -->
                          <article class="box excerpt">
                            <a href="#" class="image left"><img src="images/pic04.jpg" alt="" /></a>
                            <div>
                              <header>
                                <span class="date">July 24</span>
                                <h3><a href="#">Repairing a hyperspace window</a></h3>
                              </header>
                              <p>Phasellus quam turpis, feugiat sit amet ornare in, hendrerit in lectus
                              semper mod quisturpis nisi consequat etiam lorem. Phasellus quam turpis,
                              feugiat et sit amet ornare in, hendrerit in lectus semper mod quis eget mi dolore.</p>
                            </div>
                          </article>

                        <!-- Excerpt -->
                          <article class="box excerpt">
                            <a href="#" class="image left"><img src="images/pic05.jpg" alt="" /></a>
                            <div>
                              <header>
                                <span class="date">July 18</span>
                                <h3><a href="#">Adventuring with a knee injury</a></h3>
                              </header>
                              <p>Phasellus quam turpis, feugiat sit amet ornare in, hendrerit in lectus
                              semper mod quisturpis nisi consequat etiam lorem. Phasellus quam turpis,
                              feugiat et sit amet ornare in, hendrerit in lectus semper mod quis eget mi dolore.</p>
                            </div>
                          </article>

                        <!-- Excerpt -->
                          <article class="box excerpt">
                            <a href="#" class="image left"><img src="images/pic06.jpg" alt="" /></a>
                            <div>
                              <header>
                                <span class="date">July 14</span>
                                <h3><a href="#">Preparing for Y2K38</a></h3>
                              </header>
                              <p>Phasellus quam turpis, feugiat sit amet ornare in, hendrerit in lectus
                              semper mod quisturpis nisi consequat etiam lorem. Phasellus quam turpis,
                              feugiat et sit amet ornare in, hendrerit in lectus semper mod quis eget mi dolore.</p>
                            </div>
                          </article>

                        <footer>
                          <a class="button alt icon fa-file-o" href="../all-articles-1.html">View All Articles</a>
                        </footer>

                      </section>
                  </div>
                  <div class="col-4 col-12-medium">

                    <!-- Spotlight -->
                      <section class="box spotlight">
                        <h2 class="icon fa-file-text-o">Spotlight</h2>
                        <article>
                          <a href="#" class="image featured"><img src="images/pic07.jpg" alt=""></a>
                          <header>
                            <h3><a href="#">Neural Implants</a></h3>
                            <p>The pros and cons. Mostly cons.</p>
                          </header>
                          <p>Phasellus quam turpis, feugiat sit amet ornare in, hendrerit in lectus semper mod
                          quisturpis nisi consequat ornare in, hendrerit in lectus semper mod quis eget mi quat etiam
                          lorem. Phasellus quam turpis, feugiat sed et lorem ipsum dolor consequat dolor feugiat sed
                          et tempus consequat etiam.</p>
                          <p>Lorem ipsum dolor quam turpis, feugiat sit amet ornare in, hendrerit in lectus semper
                          mod quisturpis nisi consequat etiam lorem sed amet quam turpis.</p>
                          <footer>
                            <a href="#" class="button alt icon fa-file-o">Continue Reading</a>
                          </footer>
                        </article>
                      </section>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      <!-- Footer Wrapper -->
        <div id="footer-wrapper">
          <footer id="footer" class="container">
            <div class="row">
              <div class="col-6 col-12-medium imp-medium">

                <!-- Contact -->
                  <section>
                    <h2>Get in touch</h2>
                    <div>
                      <div class="row">
                        <div class="col-6 col-12-small">
                          <dl class="contact">
                            <dt>Twitter</dt>
                            <dd><a href="https://twitter.com/sagberkeley">@sagberkeley</a></dd>
                            <dt>Facebook</dt>
                            <dd><a href="https://facebook.com/SportsAnalyticsBerkeley">facebook.com/SportsAnalyticsBerkeley</a></dd>
                            <dt>WWW</dt>
                            <dd><a href="../index.html">berkeleysportsanalytics.org</a></dd>
                            <dt>Email</dt>
                            <dd><a>sagberkeley@gmail.com</a></dd>
                          </dl>
                        </div>
                      </div>
                    </div>
                  </section>

              </div>
              <div class="col-1 col-12-small hide-mobile">
                <span> </span>
              </div>
              <div class="col-4 col-12-small hide-mobile">
                <img class="footer-image" src="images/logo1.png" />
              </div>
              <div class="col-12">
                <div id="copyright">
                  <ul class="menu">
                    <li>&copy; Untitled. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </footer>
        </div>

    </div>

    <!-- Scripts -->
      <script src="../assets/js/jquery.min.js"></script>
      <script src="../assets/js/jquery.dropotron.min.js"></script>
      <script src="../assets/js/browser.min.js"></script>
      <script src="../assets/js/breakpoints.min.js"></script>
      <script src="../assets/js/util.js"></script>
      <script src="../assets/js/main.js"></script>

  </body>
</html>
""")

