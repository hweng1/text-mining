# text-mining

Please read the [instructions](instructions.md).

### 1. Project Overview

I use IMDB Moview Reviews as my data source.  
I use import packages, def(), for loop, string related functions, list related functions, dictionary related functions, tuple related function, arithmetic, and NLTK to process and analyze the movie review data.  
For this assignment, I hope to learn about the process and get a hand-on experience of text mining, and I hope to apply what we have learned before to this assignment.  
As there are no specfic problems to solve and strict instruction to follow, this assignment is very much similar to a real life situation. Therefore, I hope to get a good practice.  
I hope to create some functions, which can be used to analyze reviews of the desired movie.  
For this assignment, I will analyze the reviews of the movie "La La Land", but the functions created can be used on every movie. 

### 2. Implementation

To analyze the reviews, I created 10 functions.  
Each of the functions, except the first one, will utilize the last function created before.   
The four major functions are the ones that generate the final analysis of word frequency of all reviews, word frequency of each review, sentiment score, and sentiment score of all movies given.  
A big part of the analyzing is spent on cleaning the raw data and storing the data in lists.  
The functions of word frequency analysis of all reviews and each reviews generate two list of sorted lists outcomes; the sentiment anlysis generates two dictionaries as outcomes.  
Algorithms of word frequency analysis involves mostly for loop, making change of lists, dictionaries, and string, and conversion between different data structures. 
Algorithms of sentiment analysis involves using NTLK package, for loop, basic calculation, and list.

For sorting word frequency of each review, I was choosing whether to use a list of dictionaries as the final outcome or a list of lists of tuples as the final outcome.  
At last I adopted a list of lists of tuple because if this structure would make the process easier. If using a list of dictionaries, I would have to extract another list as the correct order of frequency, and then use for loop and if statements to match the order of the directed list and the final list of dictionaries.  
Using a list of lists wcould save me a lot of trouble as each list of tuples can be sorted without changing. 

### 3. Results

In word frequency analysis of all reviews, I found that for all reviews, besides the common conjunction, preposition, and so on, words of "jazz", "love", "music", "musical", "hollywood", "oscar", and the name of the actors are mentioned a lots.  
Music, as well as the actors, of the movie seems to leave a big impression on most viewers.
In word frequency analysis of each reviews, music and love are also mentioned in most reviews.  
Positive words like "inspired", "perfect", and "lovely" are also a big component of most reviews.  
Most viewers seem to like and made positive reviews of the movies. 
They seem to like the music and the love between the characters of the movie. 
For sentiment score of the film La La Land, all reviews combined produced a score in which negative sentiment is about 7.1%, neutral sentiment is about 71.6 percent, and positive sentiment is about 21.3 percent, adding up to 100%.
The sentiment score also reinforce that most viewers like the movie.  
Even though the neutral sentiment is the biggest number, positive sentiment is quite over negative sentiment, indicating most viewers feel good about the movie. 
To compare the sentiment socre of "La La Land" with other movies's sentiment score, I created a function that can generate average sentiment score of all movies input.  
I input three best rating romantic movies on Rotten Tomato in the same year as "La La Land", and they produced an average sentiment score in which negative sentiment is about 10.7 percent, neutral sentiment is about 98.4 percent, and positive sentiment is about 24.2 percent, adding up to 133.4 percent. 
Making a little calculation to convert the score, the negative sentiment is about 8.2%, neutral sentiment is 73.76%, and positive sentiment is about 18.14%, adding up to about 100%. 
Compared to this three movies' sentiment score, "La La Land"'s score is even slightly better. This result could mean that most viewers who left a review for the movie tend to be viewers who felt good about the movie. 

### 4. Reflection

The results came out well and correctly at last.  
The function write up was relatively smooth.  
However, when I went back to check the word frequency of each review result, it came out as frequency of letters, so I have to go back and recheck every function to see what went wrong, but the problem was solved at last.  
Debugging in the middle of and at the end really took me a lot of time. For testing, I used print in the middle of the functions and at last to test a lots.  
To make a improvement, the raw data cleaning in two of the vunftions can be modifies.  
I tried to simulate what we have done in analze book exercise before to clean the data using string strippables all for once, but my attempt failed. 
The data wasn't coming out as cleaned data even though I ran the statement. 
Thus, I have to write more replace statements to clean the data, and I have to scan through the reviews to see what should be cleaned.  
This alternative elongated the code and was time consuming, so next time I hope to discover why strippables was not working in the for loop and fix it to make the functions more efficient.  