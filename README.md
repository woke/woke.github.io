<a href="url"><img src="https://github.com/wessilfie/soyouwanttobewoke/blob/master/static/img/logo-black.png" align="middle" height="370" width="690" ></a>

# So You Want To Be Woke
> The path to becoming woke is hard; this site’s meant to help you get there. 

Visit the site [here](https://www.soyouwanttobewoke.com/).

This site was created to help people become more aware of the issues facing different marginalized communities. 
Some of these topics may be ones you are aware of and others not. By making this site, we hope to help people 
affected by these issues have an easy reference to provide people who may ask them to educate them on the topic 
and for those interesting in learning, provide an initial set of links to assist them in their progress to becoming woke.

To submit content to be featured on the site, click [here](http://bit.ly/wokecontent)

## Structure
This site has been made as a Flask app (see Flask branch) and as a Jekyll site. The main directories within the
Jekyll version of the site are as follows:

```bash
├── README.md         # This file
├── CONTRIBUTING.md   # How to contribute to this project's codebase
├── _layouts/         # General site design HTMLs 
├── 404/credit.html   # 404 page and link to tools used in creation of the site
├── index.md          # Site homepage
├── card.py           # Generates HTML for resource cards shown on site
├── update_resources.py # Converts submissions from http:bit.ly/wokecontent to .yml files used on site
├── _data/             # .yml files for saving resource data that is displayed on site to users
├── _includes/         # HTML templates
├── img/              # Images/logos
├── topics/           # HTML for all of the topics pages on the site
└── css/              # Site CSS
```

## Credits
The following tools were used to help make this site:
* https://github.com/mattboldt/typed.js 
* https://codepen.io/ibanez182/pen/qZOvNj
* https://codepen.io/duness/pen/vezOYW
