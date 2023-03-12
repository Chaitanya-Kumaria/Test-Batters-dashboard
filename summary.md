# Dashboard Visualization Players Data 
### Q. What are we doing in this project?

Ans. We will be visualizing a cricketer's batting career in test matches(post 2002), through an interactive dashboard.

### Q. What tools have been used for the dashboard?
Ans. We have used following python libraries  for the given purpose

1. **Beautiful Soup** : This library is used to web-scrap data from the web. It is very expensive to maintain data for each and every player on our systems,so web-scrapping provides an excellent way to get data. It also ensures that we have updated data.

    The data for this project has been taken from [cricmetric](http://www.cricmetric.com/index.py)

    *Note*: Not all websites allow web scrapping, so its better to check websites policy regarding the same.

2. **Requests**: Requests library is one of the integral part of Python for making HTTP requests to a specified URL. Whether it be REST APIs or Web Scraping, requests is must to be learned for proceeding further with these technologies. When one makes a request to a URI, it returns a response. Python requests provides inbuilt functionalities for managing both the request and response.

3. **Pandas**: Once data is web scrapped it is then converted into data frames and the Pandas library take over making handling of data easy.


4. **Ploty**: This is the graphing library which will be used for visualizing data, specifically we will be using 3 components of this library

    - `Express`
    - `graph_objects`
    - `make_subplots`

5. **Dash**: This library is used to convert our graphical data into web app.
Dash apps give a point-&-click interface to models written in Python, vastly expanding the notion of what's possible in a traditional "dashboard." With Dash apps, data scientists and engineers put complex Python analytics in the hands of business decision-makers and operators.

### Q. What are the metrics based on which the analysis would be done

Ans. At first thought one may think of using well known metrics like Average, SR, No. of 100s, Dot% etc.
but we must remember ,`what we are visualizing ?`,`Why we are visualizing?`, `based on the above questions, what metrics suite the purpose?`

**For us our main aim is to focus a batsman's test match career, this analysis can be used to highlight some of the batsman's shortcomming,or decide on which batting positions/ oppositions suite the batsman ,or help prepare bowling plans against a specific batsman.**


So, based on above requirements I have created my dashboard covering the following 4 subheadings

- Players year on year  batting average 
- Players statistics vs different oppositions
- Players batting average vs different opponents
- Players performance vs different bowler types

*Note: The reason for us focusing primarily on the average and innings played is because the need here is to analyze players test match performance, its a format where strike doesn't matter a lot.*

### Q. Now we know the metrics based on which the evaluation would be done, how to decide the correct visualization
Ans. This is a great question,so the way I approached this was as follows

- In the first visualization we have to analyze year on year trends for a batsman. so, a **line chart** is used to visualize this trend. In fact for time series data where you need trends a line chart usually serves the purpose
- In the 2nd visualization, I have to focus on Players performance vs oppositions.Here also I thought of using Averages and denote with a bar chart however, Averages don't depict the true picture, because certain batsmen may may have played only a few matches against an opposition giving us a false impression, so I here used 2 **pie charts** one for the innings vs an opposition and other for runs. 
        - So, what it does is gives us depection of no. matches played w.r.t number of runs scored by a team.
        - For eg Sachin Tendulkar has played 24.7% of matches against Austrailia scoring 26.2% of his career runs against them
- For the batting position data, bar chart completely serves the purpose. A players total career average has also been given here, just to make the numbers more compareable.
-  Now visualization of a batsman's data vs a particular bowler type. Now the reason for me not going for bar chart here is same as the used for 2nd chart.
    - So here, **bubble chart** is used where bubble color represent the bowler type,the size of bubble indicates number of runs scored, here the x-axis depicts number of innings played and y-axis depicts number of runs.



