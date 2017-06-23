#!/usr/bin/env python

# load the adapter
import psycopg2

# load the psycopg extras module
import psycopg2.extras


USER = "postgres"
PASSWORD = "123456"
# Try to connect

try:
    conn = psycopg2.connect(
        "dbname='news' user='%s' host='localhost' password='%s'"
        % (USER, PASSWORD))
except:
    print "I am unable to connect to the database."

print "What are the most popular three articles of all time?"
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute(
    """select articles.title, count(*) count from articles,
     log where log.path like '%' || articles.slug || '%' and status = '200 OK'
     group by articles.title order by count desc limit 3;""")
rows = cur.fetchall()

for row in rows:
    print u"    \u00B7 \"%s\" - %d views" % (row['title'], row["count"])


print "\n"
print "Who are the most popular article authors of all time?"
cur.execute(
    """select authors.name, count(*) count
    from articles, log, authors where
    log.path like '%' || articles.slug || '%' and
    authors.id = articles.author and status = '200 OK'
    group by authors.id order by count desc""")
rows = cur.fetchall()
for row in rows:
    print u"    \u00B7 \"%s\" - %d views" % (row['name'], row["count"])

print "\n"
print "On which days did more than 1% of requests lead to errors?"
cur.execute(
    """select log_date, (error_count::decimal*100)/log_count::decimal
    as pct from
    (select time::date error_date, count(*) error_count from log
    where status != '200 OK' group by error_date) errors,
    (select time::date log_date, count(*) log_count from log
    group by log_date) logs
    where error_date = log_date
    and (error_count::decimal*100)/log_count::decimal > 1;""")
rows = cur.fetchall()
for row in rows:
    print u"    \u00B7 \"%s\" - %.2f%% errors" % (row['log_date'], row["pct"])
