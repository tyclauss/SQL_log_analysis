# Logs Analysis

## Project Description

SQLAnalysis.py is a script that connects to a PostreSQL database via psycopg2 and inserts 
queries to answer three questions about the data (data is from a fictional site).

The script (SQLAnalysis.py) connects to the database and runs the necessary queries to return the answers 
to the following three questions.

	1. What are the three most popular articles on the site and how many do they each have?

	2. Which three authors have the most views and how many do they each have?
	
	3. On what days were more than 1% of the total HTTP requests returned as 404 errors?
	

To run the report follow these 7 steps.

	1. enter "vagrant up" from the vagrant directory
			- this ensures your vagrant virtual machine is up and running!

	2. enter "vagrant ssh" from the vagrant directory
			- this logs you in using your ssh key!

	3. enter "cd /vagrant" from the vagrant directory
			- this enters you into using the virtual machine

	4. enter "psql -d news -f newsdata.sql"
			- this runs the queries from newsdata.sql to create and populate the database
			- to download 'newsdata.sql'... 

			visit -> https://d17h27t6h515a5.cloudfront.net/topher/2016August/57b5f748_newsdata/newsdata.zip

	5. enter "psql -d 'news'"
			- this connects you to the appropriate database

	6. create the following views by entereing the queries below or by running 'create_views.sql'
			- if 'using create_views.sql' enter "psql -d news -f create_views.sql"

**ArticleCountsUse**

```sql
CREATE VIEW ArticleCountsUse AS 
	SELECT path, count(*) AS views
	FROM log 
	WHERE '/article/' || articles.slug = ArticleCountsUse.path
	GROUP BY path 
	ORDER BY views DESC;
```

**totalrequests**

```sql
CREATE VIEW totalrequests AS 
	SELECT COUNT (*) AS total, CAST (time AS DATE) AS date
	FROM log 
	GROUP BY date ORDER BY date;
```

**badrequests**

```sql
CREATE VIEW badrequests AS
	SELECT COUNT(*) AS bad, CAST (time AS DATE) AS date 
	FROM log WHERE status = '404 NOT FOUND'
	GROUP BY date ORDER BY date;
```

	7. run the script by entering "python SQLAnalysis.py"
			- this calls on the file python script that runs the report

