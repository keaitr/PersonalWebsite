import datetime
import sys


def postCreator(post_idToHTML, datePostToHTML, carousel, gitHubLinkToHTML, description):
	post = post_idToHTML +'\n  '+datePostToHTML+'\n\
  <hr>\n  '+carousel+'\n  '+description+'\n  '+gitHubLinkToHTML+'\
  \n<p><br><br></p>\n\
</div>' 

	return post
 
#return a list of the names of images pertaining to carousel
def image_list():
	path_to_image = "photos/"#[image name]
	images = [""]
	while (True):
		image = ""
		image = raw_input("Enter 'no', or Image name (Path already defined): ").strip()
		if image =='no':
			break
		#don't append to images, but return [""] or a list that ends at ["no"] (w/o 'no')
		images.append((path_to_image+image+'.jpg'))
	z = [x for x in images if x!="photos/.jpg" and x!=""]
	print z
	return z

def post_idToHTMLfunc(text):
	if text == 'no':
		return '<div id="default">'
	return "<div id="+text+">"
def datePostToHTMLfunc(text):
    return "<h4>"+text+"</h4>"

#this creates the carousel
#					str     list
def createCarousel(dateNum,images):
	cName =  "carousel"+dateNum
	size = len(images)

	if size == 0:
		return ""

	imageWraper= '\
  <!-- CAROUSEL START-->\n\
    <div id="'+cName+'" class="carousel slide" data-ride="carousel">\n\
    <!-- Indicators -->\n\
      <ol class="carousel-indicators">\n\
        <li data-target="#'+cName+'" data-slide-to="0" class="active"></li>'

	for i in range(1,size):
		imageWraper += '\n\
        <li data-target="#'+cName+'" data-slide-to="'+str(i)+'"></li>'

	imageWraper +='\n\
      </ol>\n'

	if size>0:
		imageWraper += '\n\
    <!-- Wrapper for slides -->\n\
    <div class="carousel-inner">\n\
      <div class="item active">\n\
        <img src="'+images[0]+'" style="width:100%;">\n\
      </div>\n'
	if size>1:
		for image in images[1:]:
			imageWraper +='\
      <div class="item">\n\
        <img src="'+image+'" style="width:100%;">\n\
      </div>\n'

  	if size>0:
		imageWraper+= '\
    </div>\n\
    <!-- Left and right controls -->\n\
    <a class="left carousel-control" href="#'+cName+'" data-slide="prev">\n\
      <span class="glyphicon glyphicon-chevron-left"></span>\n\
      <span class="sr-only">Previous</span>\n\
    </a>\n\
    <a class="right carousel-control" href="#'+cName+'" data-slide="next">\n\
      <span class="glyphicon glyphicon-chevron-right"></span>\n\
      <span class="sr-only">Next</span>\n\
    </a>\n\
  </div>\n\
  <br>\n\
  <!-- CAROUSEL END-->\n'

	return imageWraper

def gitHubLinkToHTMLfunc(text):
	if text == 'no':
		return "" 
	return '<a href="'+text+'" target="_blank">GitHub</a>'


if __name__ == "__main__": 
	# some_parameter = str(sys.argv[1]) 

 	#getting the dates
	now =  datetime.datetime.now()
	month3 = now.strftime("%B")[:3] #only want the first 3 for month i.e. (Jan, Feb, Mar, ..., Dec).

	#Title date(which is posted)
	datePost = ("%s %d %d")%(month3,now.day,now.year)
	#Numer date which will be used for filename, and image carousel for uniqueness
	dateNum = ("%d%d%d")%(now.month,now.day,now.year)

	#Take in the id for the post. Future plan for filtering with id
	post_id = str(raw_input("What is the post #id: ")).strip()

	#Will add image names to html
	images = image_list()
	#create git hub link (or no)
	ghl = raw_input("Enter 'no', or provide github html").strip()
	gitHubLink = ghl

	#write posts description
	description = raw_input("Enter description, include <p></p> or <br> when appropriate (first one too):\n ")

	#make user inputed into HTML, and carousel
	post_idToHTML = post_idToHTMLfunc(post_id)
	datePostToHTML = datePostToHTMLfunc(datePost)
	carousel = createCarousel(dateNum,images)
	gitHubLinkToHTML = gitHubLinkToHTMLfunc(gitHubLink)    
 
 	#create post string of HTML post
	post=  postCreator(post_idToHTML, datePostToHTML, carousel, gitHubLinkToHTML, description)

	#open (create) and write to file
	p = "files/post"+dateNum+".txt"
	f = open(p,'w')
	f.write(post)
	f.close()







