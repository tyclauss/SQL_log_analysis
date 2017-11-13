/* creates ArticleCountsUse view */

CREATE VIEW ArticleCountsUse AS 
	SELECT path, count(*) AS views
	FROM log WHERE '/article/' || articles.slug = ArticleCountsUse.path
	GROUP BY path 
	ORDER BY views DESC;

/* creates totalrequests view */

CREATE VIEW totalrequests AS 
	SELECT COUNT (*) AS total, CAST (time AS DATE) AS date
	FROM log 
	GROUP BY date ORDER BY date;

/* creates badrequests view */

CREATE VIEW badrequests AS
	SELECT COUNT(*) AS bad, CAST (time AS DATE) AS date 
	FROM log WHERE status = '404 NOT FOUND'
	GROUP BY date ORDER BY date;