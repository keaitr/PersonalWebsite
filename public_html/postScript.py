#python script that creates post
import datetime

"""
EXAMPLE


      <div id="helloworld">
          <h4> DATE </h4>
          <hr>

          <!-- CAROUSEL START-->
          <div id="myCarousel1" class="carousel slide" data-ride="carousel">
          <!-- Indicators -->
            <ol class="carousel-indicators">
              <li data-target="#myCarousel1" data-slide-to="0" class="active"></li>
              <li data-target="#myCarousel1" data-slide-to="1"></li>
              <li data-target="#myCarousel1" data-slide-to="2"></li>
            </ol>

            <!-- Wrapper for slides -->
            <div class="carousel-inner">
              <div class="item active">
                <img src="https://unsplash.it/800/600/?random&v=1" style="width:100%;">
              </div>

              <div class="item">
                <img src="https://unsplash.it/800/600/?random&v=2" style="width:100%;">
              </div>
            
              <div class="item">
                <img src="https://unsplash.it/800/600/?random&v=3" style="width:100%;">
              </div>
            </div>

            <!-- Left and right controls -->
            <a class="left carousel-control" href="#myCarousel1" data-slide="prev">
              <span class="glyphicon glyphicon-chevron-left"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#myCarousel1" data-slide="next">
              <span class="glyphicon glyphicon-chevron-right"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
          <br>
          <!-- CAROUSEL END-->



          <p> 
          WRITING CONTENT
          </p>
          <a href="https://github.com/keaitr/PersonalWebsite" target="_blank">GitHub </a> 

        <p><br><br></p>

      </div>
"""
now =  datetime.datetime.now()
month3 = now.strftime("%B")[:3]
datePost = ("%s %d %d")%(month3,now.day,now.year)
dateNum = ("%d%d%d")%(now.month,now.day,now.year)
print datePost
print dateNum
#get id/post type name
#get images. if 'no', quit if name continue
#get github. if 'no', then no, else paste url
#get post. <br> or <p> and stuff
	#have to start with <p> your self and end it?
	#have a loop until "END" so keep adding and can hit enter

