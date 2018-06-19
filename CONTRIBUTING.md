# Contributing to So You Want To Be Woke (website)

Thank you for your interest in helping improve the So You Want To Be Woke website.

## How to submit a new feature

We're always interested in adding new sections to the site and improving the site's UI.
To make an update, you need to do the following:
1. Make a branch and add your new code
2. (If adding a new section) Requesting the new topic be added to the [submission form](http://bit.ly/wokecontent)
3. Testing your changes (locally)

## How can I add my new feature(s) to the site? 

### Branching 
To add to the site, first make a branch off of the latest version of master. 
Locally, you can run `git pull && git checkout [branch]` to switch to the new branch you will be working on.

### Reviewing Site Structure
To see how the web app is organized, see the [README](https://github.com/wessilfie/soyouwanttobewoke#structure). 
To make the site modular, the app uses Jinja templating. Read more about how that works [here](http://jinja.pocoo.org/).

### Format for writing topics in the code
All topics are formatted in the same style and are in lower case letters. For multi-word topics, replace each space with an underscore.
For example, Allyship would be `allyship` and Racial Identity would be `racial_identity`.

### Adding a definition
Each topic on the site requires a definition and a source. To do this, edit `definitions.py` by adding a new key/value
pair to the dictionary in the following format:

```python
defintions = {....,
...,
topic: [""" 'DEFINITION GOES HERE' """, 'LINK_TO_DEFINITION_SOURCE']
}

```
where topic follows the rules in the above [section](https://github.com/wessilfie/soyouwanttobewoke/new/master#format-for-writing-topics-in-the-code).

### Adding a new .yml file
When adding a new section, you also need to add a .yml file in the `data/` folder. The site uses these files to quickly load in the content 
displayed on the site. They are formatted in the following way. If adding a new section, add the first one manually; later additions will be added
using `update_resources.py` and pulled from the submission form. 

Here is an example of a file. `[VAL]` denotes placeholder text
```yml
data:
  [TOPIC]: 
  - content_link: [LINK TO CONTENT SUBMITTED]
    description: [DESCRIPTION OF CONTENT]
    isIntersectional: [true/false]
    social_media: [LINK TO SUBMITTER'S SOCIAL MEDIA]
    submitted_by: [SUBMITTER'S NAME]
    title: [CONTENT TITLE]
```
## Testing

**Note: If you're working on a new feature, be sure that you are working on branch based on the most recent version of master.**
### Running code locally
To run the site locally, you need to do the following:

### 1) (Optional) Set up a Python3 Virtual Environment (taken from [here](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)):

First type the following in Terminal: 
`python3 -m venv <filepath to your repo clone>`

Next, `cd` into the `bin` folder,
` cd bin `

Next, activate the virtual environment: 
`source activate`

To deactivate the environment, simply write: 
`deactivate `

### 2) Install Required Libraries
To install the required libraries, change directories to your clone of the repo and run the following:
`pip3 install -r requirements.txt` in order to install the libraries currently used in the site. When adding a new feature to 
the site that requires a new library, be sure to add the library and the version number used following the formatting 
convention in the file.

### 3) Confirm your version is working locally
If you have everything setup correctly, you should be able to run the Flask app and check any of the update you've made

`python3 app.py`
You should get a message with a similar output to the following:

` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
### 4) Make Pull Request
Once you've tested your code and verified everything's working, make a pull request on the repo. 


 ## Now what?
 Woo! You've gone through the process of contributing to the site. Continue working on new things to help make the site even better.


