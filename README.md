<a href="url"><img src="https://github.com/wessilfie/soyouwanttobewoke/blob/master/static/img/logo-black.png" align="middle" height="370" width="690" ></a>

# So You Want To Be Woke
> The path to becoming woke is hard; this site’s meant to help you get there.

This site was created to help people become more aware of the issues facing different marginalized communities. 
Some of these topics may be ones you are aware of and others not. By making this site, we hope to help people 
affected by these issues have an easy reference to provide people who may ask them to educate them on the topic 
and for those interesting in learning, provide an initial set of links to assist them in their progress to becoming woke.

To submit content to be featured on the site, click [here](http://bit.ly/wokecontent)

## Structure

```bash
├── README.md         # This file
├── requirements.txt  # Libraries used to build the site
├── Procfile          # Used when deploying the website to production
├── app.py            # Handles site routing
├── card.py           # Generates HTML for resource cards shown on site
├── definitions.py    # Stores definitions and their sources for site topics
├── update_resources.py # Converts submissions from http:bit.ly/wokecontent to .yml files used on site
├── data              # .yml files for saving resource data that is displayed on site to users
├── templates/         # HTML files for the site
└── static/             
    ├── style.css     # Site CSS
    ├── img/          # Images/logos
```

## Technology Stack
Below are the core libraries used in building the site.

### Python 3
So You Want To Be Woke's website is written in Python 3. 

### Flask
Flask is powerful micro web-framework that makes it easy to get a server-based Python app up and running quickly. 

### Pandas
A super helpful library that is used in this project for reading in .csv files of user submissions

## Credits
The following tools/pens were used to help make this site:
* https://github.com/mattboldt/typed.js 
* https://flatuicolors.com/
* https://codepen.io/ibanez182/pen/qZOvNj
* https://codepen.io/duness/pen/vezOYW
