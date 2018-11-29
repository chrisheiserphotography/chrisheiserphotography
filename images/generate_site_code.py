
import csv
import json
import os
import sys
from PIL import Image

# Categories
# flyfishing
# landscapes
# products

# PHOTO SIZES
# - Bio photo
# - 1920x1900

# - Index Slides are 1.5-1.58x ratio
# - 2750x4300
# - 1000x1578
# - 3350x5300


# - Portfolio Thumbnails 
# - 1000x1124

# 1. All slides go in the "slides" folder. Create photos manually where needed.
# 2. All portfolio photos go in the "photos" folder
# 3. All portfolio thumbnails go in the "photos" folder
# - Each Thumbnail file prefixed with "thumbnail"
# - 

# 4. Create a CSV file that has all metadata. Photo Type. Code Targets. Title. Description. Location. etc.
# 5. Generate code with script. Run once for Slides. Run once for Portfolio
# 6. Place code into HTML files. 



def create_thumbnail(file):
	size = 600,650
	infile = os.path.join("photos", file["filename"] + ".jpg")
	outfile = os.path.join("photos","thumbnail_" + file["filename"] + ".jpg")
	try:
		im = Image.open(infile)
		im.thumbnail(size)
		im.save(outfile)
	except IOError:
		print("cannot create thumbnail for " + infile)
	file["thumbnail"] = "thumbnail_" + file["filename"]
	return file

def read_csv(filename):
	out = []
	with open(filename) as csvfile:
		# Csv reader
		reader = csv.DictReader(csvfile, delimiter=",")
		for row in reader:
			out.append(row)
	return out

def create_slide(file):
	slide_code = """<!--=============== {} ===============-->	
                                    <div class="swiper-slide">
                                        <div class="bg" style="background-image:url(images/img/{}.jpg)"></div>
                                        <div class="zoomimage"><img src="images/img/{}.jpg" class="intense" alt=""><i class="fa fa-expand"></i></div>
                                    </div>
                                    <!-- {} end -->""".format(file["filename"], file["filename"], file["filename"], "", "", file["filename"])

	print(slide_code)


def create_portfolio(file):

	# Create thumbnail here
	# file = create_thumbnail(file)
	portfolio_code = """<!-- {} -->  
								<div class="portfolio_item {}">
                                        <img  src="images/img/{}.jpg" alt="">
                                        <div class="zoomimage"><img src="images/img/{}.jpg" class="intense" alt=""><i class="fa fa-expand"></i></div>
                                        <div class="port-subtitle-holder">
                                            <div class="port-subtitle">
                                                <span><a href="#">{}</a></span>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- END {} -->  """.format(file["filename"], file["category"], file["filename"], file["filename"], file["category"], file["filename"])

	print(portfolio_code)


files = read_csv("db.csv")
# print(files)

print("========================== SLIDE CODE =============================")

for file in files: 
	if(file["slide"]):
		create_slide(file)



print("========================== PORTFOLIO CODE =============================")

for file in files:
	if(file["portfolio"]):
		create_portfolio(file)



"""  INDEX PAGE SLIDE TEMPLATE
                                    <div class="swiper-slide">
                                        <div class="bg" style="background-image:url(images/bg/1.jpg)"></div>
                                        <div class="overlay"></div>
                                        <div class="zoomimage"><img src="images/bg/1.jpg" class="intense" alt=""><i class="fa fa-expand"></i></div>
                                        <div class="slide-title-holder">
                                            <div class="slide-title">
                                                <span class="subtitle">At posuere sem accumsan </span>
                                                <div class="separator-image"><img src="images/separator.png" alt=""></div>
                                                <h3 class="transition">  <a href="portfolio-single.html">Blandit praesent</a></h3>
                                                <h4><a  href="portfolio-single.html">View</a></h4>
                                            </div>
                                        </div>
                                    </div>
                                    <!--  end TEMPLATE -->
"""


""" PORTFOLIO ITEM TEMPLATE
                                    <!-- portfolio item -->
                                    <div class="portfolio_item people comercial">
                                        <img  src="images/bg/1.jpg"   alt="">
                                        <div class="port-desc-holder">
                                            <div class="port-desc">
                                                <div class="overlay"></div>
                                                <div class="grid-item">
                                                    <h3><a href="portfolio-single.html">Quisque non augue</a></h3>
                                                    <span>Travel</span>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="port-subtitle-holder">
                                            <div class="port-subtitle">
                                                <h3><a href="portfolio-single.html">Quisque non augue</a></h3>
                                                <span><a href="#">Travel</a> / <a href="#">Photography</a></span>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- portfolio item end -->
END PORTFOLIO ITEM
""" 