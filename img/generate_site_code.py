
import csv
import json
import os
import sys
from PIL import Image

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
	slide_code = """<div class="single-hero-slide bg-img slide-background-overlay" style="background-image: url(img/slides/{}.jpg);">
		<div class="container h-100">
			<div class="row h-100 align-items-end">
				<div class="col-12">
					<div class="hero-slides-content">
					</div>
				</div>
			</div>
		</div>
	</div>""".format(file["filename"])
	# slide_code = """<div class="single-hero-slide bg-img slide-background-overlay" style="background-image: url(img/slides/{}.jpg);">
	# 	<div class="container h-100">
	# 		<div class="row h-100 align-items-end">
	# 			<div class="col-12">
	# 				<div class="hero-slides-content">
	# 					<div class="line"></div>
	# 					<h2>{}</h2>
	# 					<p>{}</p>
	# 				</div>
	# 			</div>
	# 		</div>
	# 	</div>
	# </div>""".format(file["filename"], file["title"], file["description"])

	print(slide_code)


def create_portfolio(file):

	# Create thumbnail here
	file = create_thumbnail(file)
	portfolio_code = """<div class="col-12 col-sm-6 col-lg-3 single_gallery_item {0} wow fadeInUpBig" data-wow-delay="300ms">
		<a class="gallery-img" href="img/photos/{1}.jpg"><img src="img/photos/{2}.jpg" alt="{3}" title="{4}"></a>
	</div>""".format(file["category"], file["filename"], file["thumbnail"], file["description"], file["description"])

	print(portfolio_code)


files = read_csv("db.csv")
# print(files)

print("========================== SLIDE CODE =============================")

for file in files: 
	if(file["slide"]):
		create_slide(file)



print("========================== PORTFOLIO CODE =============================")

for file in files:
	create_portfolio(file)