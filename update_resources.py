import pandas as pd
import validators
import yaml
from definitions import *

#validate that user submitted correctly formatted link
def validate_link(link):
    return True if validators.url(link) else False

#checks if a link is already on the site to prevent duplicates
def is_duplicate_link(link, data):
    for content in data:
        if link == content['content_link']:
            return True
    return False

#update .yml file with new content
def update_yml(data, topic):
    file_path = "data/" + topic + ".yml"
    with open(file_path, 'r') as yml_data:
        try:
            current_content = yaml.safe_load(yml_data)
            if (data not in current_content['data'][topic] 
            and not is_duplicate_link(data['content_link'], current_content['data'][topic])):
                current_content['data'][topic].append(data)
                with open(file_path, 'w') as outfile:
                    yaml.dump(current_content, outfile, default_flow_style=False)
            else:
                print(data['title'] + " is already saved as a resource.")
        except:
            print("Failed to update .yml file")

#iterates over csv file of submitted content and adds to related .yml file
def main():
	df = pd.read_csv("Submit to So You Want to be Woke  (Responses) - Form Responses 1.csv")
	for index, row in df.iterrows():
	    content = {}
	    content['submitted_by'] = row['Your Name']
	    content['social_media'] = row['Social Media Handle/Website Link'] if validate_link(row['Social Media Handle/Website Link']) else "#"
	    content['title'] = row['Content Title']
	    content['description'] = row['Content Description']
	    content['content_link'] = row['Content Link']
	    content['isIntersectional'] = True if row['Is this content intersectional?'] == 'Yes' else False
	    topic = row['Content Topic'].replace(" ", "_").lower()
	    update_yml(content, topic)


main()