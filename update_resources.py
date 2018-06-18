import pandas as pd
import validators
import yaml
import sys
#from definitions import *

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
    file_path = "_data/" + topic + ".yml"
    try:
        with open(file_path, 'r') as yml_data:
            current_content = yaml.safe_load(yml_data)
            if (data not in current_content['data'] 
            and not is_duplicate_link(data['content_link'], current_content['data'])):
                current_content['data'].append(data)
                with open(file_path, 'w') as outfile:
                    yaml.dump(current_content, outfile, default_flow_style=False)
    except:
        output_data = {}
        output_data['data'] = [data]
        with open(file_path, 'w') as new_yml_data:
            yaml.dump(output_data, new_yml_data, default_flow_style=False)
        print("Made a new file for {}".format(data['title']))

#iterates over csv file of submitted content and adds to related .yml file
def main(argv):
	df = pd.read_csv(argv[1])
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


main(sys.argv)
