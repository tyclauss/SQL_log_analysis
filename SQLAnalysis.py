#!/usr/bin/env python2.7

import psycopg2


def popular_articles():
    """Connects to the news database and queries to extract the name
    of the three most popular articles and how many views each has accumulated.
    Prints results.
    """
    try:
        conn = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print "Error - database not found"
        pass
    
    cursor = conn.cursor()
    cursor.execute("""SELECT ArticleCountsUse.views, articles.title FROM ArticleCountsUse,
                    articles WHERE ArticleCountsUse.Right = articles.slug
                    ORDER BY views DESC LIMIT 3""")
    results = cursor.fetchall()
    conn.close()
    print "Most Popular Articles"
    for art in results:
        print("     " + '"' + str(art[1]) + '"' + " - " + str(art[0]))
    print '\n'


def popular_authors():
    """ Connects to the news database and queries to extract the name
    of the three most popular authors and the number of views each has accumlated across all of their articles.
    Prints results.
    """
    try:
        conn = psycopg2.connect("dbname=news")

    except psycopg2.Error as e:
        print "Error - database not found"
        pass
    
    cursor = conn.cursor()
    
    cursor.execute("""SELECT SUM(ArticleCountsUse.views) AS totalviews , authors.name
                FROM ArticleCountsUse, authors, articles
                WHERE ArticleCountsUse.Right = articles.slug
                AND articles.author = authors.id GROUP BY authors.name
                ORDER BY totalviews DESC LIMIT 3;""")
    results = cursor.fetchall()
    conn.close()
    print "Most Popular Authors"
    for auth in results:
        print("     " + str(auth[1]) + " - " + str(auth[0]))
    print '\n'


def error_days():
    """Connects to the news database and queries for the days on which more than
    1% of HTTP requests returned 404 errors.
    Prints the results.
    """
    try:
        conn = psycopg2.connect("dbname=news")

    except psycopg2.Error as e:
        print "Error - database not found"
        pass
    
    cursor = conn.cursor()
    
    cursor.execute("""SELECT ROUND((CAST(bad AS DECIMAL(8,2))/CAST(total
                    AS DECIMAL(8,2)))*100, 2) AS percent,
                    totalrequests.date FROM totalrequests, badrequests
                    WHERE totalrequests.date = badrequests.date
                    AND ((CAST(bad AS DECIMAL(8,2))/CAST(total AS 
                    DECIMAL(8,2)))*100) > 1.00;""")
    results = cursor.fetchall()
    conn.close()
    print "Days with More than 1% Errors"
    for day in results:
        print("     " + str(day[1]) + " -- " + str(day[0]) + "% errors")

if __name__ == '__main__':
    popular_articles()
    popular_authors()
    error_days()


