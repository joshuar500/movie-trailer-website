import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
<head>
  <meta content="charset=utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Josh's Favorite Films</title>

  <!-- FlexSlider vs Kwiks credit: http://webcodebuilder.com/responsive-jquery-plugin-flexslider-feat-kwiks/-->
  
  <!-- FlexSlider & Movie Stuff pieces -->
  <link rel="stylesheet" href="css/style.css" type="text/css" />
  <link rel="stylesheet" href="css/magnific-popup.css"> 
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
  <script src="js/jquery.flexslider-min.js"></script>
  <script src="js/jquery.magnific-popup.min.js"></script>
  <script src="js/css3-mediaqueries.js"></script>
  
  <!-- Kwiks pieces -->
  <script src="js/kwiks.js"></script>
  
  <!-- Includes for this default -->
  <link rel="stylesheet" href="css/default.css" type="text/css" media="screen" />
  
  <!-- Hook up the FlexSlider -->
  <script type="text/javascript">
    var Main = Main || {};

    jQuery(window).load(function() {
      window.responsiveFlag = jQuery('#responsiveFlag').css('display');
      Main.gallery = new Gallery();
      
      jQuery(window).resize(function() {
        Main.gallery.update();
      });
    });

    function Gallery(){
      var self = this,
        container = jQuery('.flexslider'),
        clone = container.clone( false );
        
      this.init = function (){
        if( responsiveFlag == 'block' ){
          var slides = container.find('.slides');
          
          slides.kwicks({
            max : 400,
            spacing : 0
          }).find('li > a').click(function (){
            return false;
          });
        } else {
          container.flexslider();
        }
      }
      this.update = function () {
        var currentState = jQuery('#responsiveFlag').css('display');
        
        if(responsiveFlag != currentState) {
        
          responsiveFlag = currentState;
          container.replaceWith(clone);
          container = clone;
          clone = container.clone( false );
          
          this.init();  
        }
      }
      
      this.init();
    }
  </script>
  <script type="text/javascript">
    $('.test-popup-link').magnificPopup({ 
      type: 'iframe'      
    });
  </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<body>
  <noscript>    
    <div class="nojs">Javascript must be enabled for the correct page display.</div>
  </noscript>
  <div id="container">
    <h2>Josh's Favorite Films</h2>
    
    <div class="flexslider">
      <ul class="slides">
        <!-- Creates the list of movies, displays them in the slider -->
        {movie_tiles}
      </ul>
    </div>
  </div>
  <span id="responsiveFlag"></span>
</body>  
</html>
'''

# A single movie entry html template
movie_tile_content = '''
        <li>
          <img src="{poster_image_url}" />
          <div class="flex-caption">
            <div class="movie-tile">
            <h3>{movie_title}</h3>            
            <p><a class="test-popup-link" href="{trailer_youtube_url}">watch trailer</a> Lorem ipsum dolor sit amet, consectetur adipiscing elit. In venenatis porttitor massa eget pretium. Mauris vel erat sem, id tempor est. Pellentesque lobortis iaculis massa quis auctor.</p>
            </div>
          </div>
        </li>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        trailer_youtube_url = movie.trailer_youtube_url

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            trailer_youtube_url=trailer_youtube_url
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))  

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
