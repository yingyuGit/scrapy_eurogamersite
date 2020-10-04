# scrapy
Using scrapy to build your own data.Here I extracted Switch game news (news title, date, comments and Urls) from Eurogamer site. 

-----------
**1. Step1: Install Scrapy**

As Scrapy official website strongly recommend that you install Scrapy in a dedicated virtualenv, to avoid conflicting with your system packages.
Steps to install scrapy in a virtual environment.

Install a virtual environment using pip
```
pip install virtualenv
```

Make a directory for your virutual environment.
```
mkdir your_virtualenv_name
cd your_virtualenv_name
```

Create your first project under the virtual enviroment and activate it.
```
virtualenv *project1*
source project1/bin/activate
```

Deactivate the project
```
source deactivate
```

Remove the project
```
rm -rf project1
```

How to save your local python package list so that you can reuse for other projects too.
```
pip freeze  -- local > requirements.txt
pip install -r requirements.txt
```


**2. Creating a New Scrapy project**

```
scrapy startproject *switchgames*
```
This will create a project directory with the contents below.  
```
scrapy.cfg            # deploy configuration file

    switchgames/      # project's Python module, you'll import your code from here
        __init__.py
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
            __init__.py
            
```
            
**3. Define Items and create your spiders**

In this project I only edited the items.py and created a spider file (eurogamer.py) to extract data from eurogamer sites.

- Defined items in items.py
- Created the first spider file called "eurogamer.py" and stored under "spiders/" directory.  Inside my spider, I defined GamesSpider class that defines scraping information.


**4. Storing the scraped data**

```
scrapy crawl SwitchGames -o swithgamenews-1004-final.csv
```

Note: SwitchGames are the spider name I difined inside the eurogamer.py
Note: output can be other formats too like JSON.


The next step from here would be clean the data and analise it.



** Reference Tutorial**

https://docs.scrapy.org/en/latest/intro/tutorial.html
https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors
https://towardsdatascience.com/using-scrapy-to-build-your-own-dataset-64ea2d7d4673


