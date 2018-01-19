## Analysis on Enron Data:

```ENRON Dataset:
It contains data from about 150 users, mostly senior management of Enron, organized into folders. This data was used during the investigation   of the scandal. The data contains the mail directory of each user. Data is organised as: Under each user all mail directories containg mails related to that user. 
```

So here I decided to perform 3 analysis that would be useful in analysing the scanadal. 

#### Analysis-1:

*CEO of Enron - Jeffrey Skilling would have played an important role in the scandal. So, I decided to take a look of his mails. I thought if I can fetch the persons from whome he received most of the mails and to whom he sent most of the mails and also the words that have been mostly exchanged in their mails.*

With this analysis I can get to know about what he is talking the most and with whom.

I analysed all the mails from his 'sent' folders to check to whom he mailed the most and what are the top words he used in his mails.
I also analysed his 'inbox' folders to check from whom he received the most of his inbox mails and what were the frequents they used in the mails.

I fetched each sender from his inbox mails and receiver of his mail from his outbox(sent) mails. I counted the number of mails for each person.
I fetched all the words from his mails using NLTK's tokenization function and pre-processed them like removing punctuations, numbers, common words and lemmatized them. Then using these words, I counted the frequecy of each word to get the most frequent words.

The ouput of the analysis is written to csv files and can be found using these links:
#####
Code: [Que1_Ana1_Code](./Analysis%20on%20Enron%20Data/que_1_ana_1.ipynb)

Output Files:
  * [Que1_Ana1_Output1](./Analysis%20on%20Enron%20Data/ana_1/Analysis_1_Top10Receivers.xlsx)    
  * [Que1_Ana1_Output2](./Analysis%20on%20Enron%20Data/ana_1/Analysis_1_Top10_Outbox_Words.xlsx)
  * [Que1_Ana1_Output3](./Analysis%20on%20Enron%20Data/ana_1/Analysis_1_Top10Senders.xlsx)
  * [Que1_Ana1_Output4](./Analysis%20on%20Enron%20Data/ana_1/Analysis_1_Top10_Inbox_Words.xlsx)
    
    
Output ScreenShot: 
* ![Que1_Ana1_Output_Screenshot1](./Analysis%20on%20Enron%20Data/ana_1/Que-1_Ana-1_Output1.JPG)
* ![Que1_Ana1_Output_Screenshot2](./Analysis%20on%20Enron%20Data/ana_1/Que-1_Ana-1_Output2.JPG)
* ![Que1_Ana1_Output_Screenshot3](./Analysis%20on%20Enron%20Data/ana_1/Que-1_Ana-1_Output3.JPG)
* ![Que1_Ana1_Output_Screenshot4](./Analysis%20on%20Enron%20Data/ana_1/Que-1_Ana-1_Output4.JPG)

#####



#### Analysis-2:

*As the data is related to a scandal, I thought of analysing from when this crisis was going on and were they aware of it. Eventhough most of the communication regarding this would have gone offline but there will be some hints if we go through their mails. So I thought 'bankrupt','fraud','deal','ageement' would play a critical role. Like 'bankrupt' and 'fraud' would give us idea about the scandal and 'deal','agreement' would give their business deals. So I decided to analyse the use of these words in their mails based on the year they have exchanged the mails.*

I first took all the words from each person's sent mails and checked for the critical words; if present add it to a dictionary with year as its key. Similarly, did for all files and updated the dictionary. At the end, I wrote the output to a csv file which can be visualized as below:

#####
Code : [Que1_Ana2_Code](./Analysis%20on%20Enron%20Data/que_1_ana_2.ipynb)

Output File: [Que1_Ana2_Output](./Analysis%20on%20Enron%20Data/ana_2/Analysis_2_Critcal_Words_Yearwise.xlsx)    
    
Output ScreenShot: ![Que1_Ana2_Output_Screenshot](./Analysis%20on%20Enron%20Data/ana_2/Que-1_Ana-2.JPG)

#####

#### Analysis-3:

*While doing the above two analysis, I thought like they would have exchanged the mails in the odd time i.e. not during the office hours. That would give us some idea about the scandal like who sent most of the mails at odd time and they can pose an investigation on them. So I considered the time duration between 10pm to 6am as odd (unusual) timing. As all the mails were exchanged at Pacific time zone, I did had to bother about time zones. So from the sent mails of each person, I checked for the time of mail sent and if it is at odd time, I added them to the dictionary. This was done all user and dictionary was updated correspondingly. Finally, I ordered the dictionary to see the top 10 users who sent mails at unusual time. The output was written to a csv file as:*

#####
Code : [Que1_Ana3_Code](./Analysis%20on%20Enron%20Data/que_1_ana_3.ipynb)


Output Files:
   * [Que1_Ana3_Output1](./Analysis%20on%20Enron%20Data/ana_3/Analysis_3_Odd_Time_Mail_Senders.xlsx)    
   * [Que1_Ana3_Output2](./Analysis%20on%20Enron%20Data/ana_3/Analysis_3_Top_10_Odd_Time_Mail_Senders.xlsx)
    
Output ScreenShot: 
    * ![Que1_Ana3_Output_Screenshot1](./Analysis%20on%20Enron%20Data/ana_3/Que-1_Ana-3_Output1.JPG)
    * ![Que1_Ana3_Output_Screenshot2](./Analysis%20on%20Enron%20Data/ana_3/Que-1_Ana-3_Output2.JPG)

#####

###
## Analysis on New York Times Data:


``
New York Times Dataset: New York Times consists of several APIS. I took a lot of time to decide on which two APIs to choose among them and what useful analysis I can perform. I decided to choose Archive API and Community API data for the year 2016.
``

>Archive API data contains the information about articles like the url of the articles, published date, section to which it belongs, reporter/s of the article, multimedia information of the article and so on. I fetched the articles of all months of 2016 and stored them in a hierarchical order as Archive_API --> 2016 --> Month --> Data.

But for my analysis I wanted only few fields of the data. So I went throgh each of the file, fetched the required information and stored them in an excel file for my analysis. The data preperation code is in que_2_ana_1.py. The data fetching code and the excel file can be found at:

#####
Archive API Data Extraction Code : [Archive_API_Data_Extraction_Code](./Analysis%20on%20New%20York%20Times%20Data/que_2_Archive_API_data_extraction.py)

Prepared Excel for Analysis of Archive API: [Prepared_Excel_for_Analysis_Archive_API](./Analysis%20on%20New%20York%20Times%20Data/Archive_API_Data_For_Analysis.xlsx)    
    
Excel ScreenShot: ![Excel ScreenShot](./Analysis%20on%20New%20York%20Times%20Data/Archive_API_Prepared_Data.JPG)

#####


>Community API contains the information about the comments from registered users of NYT like the content of the comment, when was it commented, url of the article about which comment was made, who commented and from where and so on. I fetched all the comments made in 2016 and stored them in a hierarchical order as Community_API --> 2016 --> Month --> Date --> Data.

But for my analysis I wanted only few fields of the data. So I went throgh each of the file, fetched the required information and stored them in an excel file for my analysis. The data preperation code is in que_2_ana_3.py.  The data fetching code and the excel file can be found at:

#####
Community API Data Extraction Code : [Archive_API_Data_Extraction_Code](./Analysis%20on%20New%20York%20Times%20Data/que_2_Community_API_data_extraction.ipynb)

Prepared Excel for Analysis of Community API: [Prepared_Excel_for_Analysis_Archive_API](./Analysis%20on%20New%20York%20Times%20Data/Community_API_Data_For_Analysis.xlsx)    
    
Excel ScreenShot: ![Excel ScreenShot](./Analysis%20on%20New%20York%20Times%20Data/Community_API_Prepared_Data.JPG)

#####

I merged that data from both of these APIs for my 3rd analysis.

####Analysis-1:

*I thoght like fetching the data according each section for rach month of 2016 would be useful. We know that artcles are categorised as sections. Like for a month, if a section has less number of articles, editors can focus on how to improve that section by increasing the number of articles. So, I decide to analyse the data on a monthly basis for each section. I read the data from the excel file I had prepared, and for each month for each section I counted the number of articles. Then I found the top section i.e. with most number articles and bottom section with least number of articles. The code for the above and output is at below locations: *

#####
Code : [Que2_Ana1_Code](./Analysis%20on%20New%20York%20Times%20Data/que_2_ana_1.ipynb)

Output Files: 
    * [Que2_Ana1_Output1](./Analysis%20on%20New%20York%20Times%20Data/ana_1/Analysis_1_Ouput_Monthwise_Sectionwise_Data.xlsx)    
    * [Que2_Ana1_Output2](./Analysis%20on%20New%20York%20Times%20Data/ana_1/Analysis_1_Ouput_Top_Bottom_Section_Monthwise.xlsx)
    
Output ScreenShot:
    * ![Que2_Ana1_OutputScreen_shot1](./Analysis%20on%20New%20York%20Times%20Data/ana_1/Que-2_Ana-1_Output1.JPG)
    * ![Que2_Ana1_OutputScreen_shot2](./Analysis%20on%20New%20York%20Times%20Data/ana_1/Que-2_Ana-1_Output2.JPG)

#####


#### Analysis-2:

*Each reporter is having his own expertise section. Like he may write in only one section or if he write in 2 or more he may not write articles equally in all sections. So, for an editor it is good to know each reporter's expertise and non-expertise area based on the number of articles he has written. I fetched the number of articles in each section for each reporter using a dictionary. Then I found the expertise and non-expertise sections of a reporter based on the number of articles he has written. The code for this analysis and the output can be found at: *

#####
Code : [Que2_Ana2_Code](./Analysis%20on%20New%20York%20Times%20Data/que_2_ana_2.ipynb)

Output Files: 
    * [Que2_Ana2_Output1](./Analysis%20on%20New%20York%20Times%20Data/ana_2/Analysis_2_Ouput_Reporterwise_Sectionwise_Data.xlsx)    
    * [Que2_Ana2_Output2](./Analysis%20on%20New%20York%20Times%20Data/ana_2/Analysis_2_Ouput_Reporterwise_Expertise_Non-Expertise_Section_Data.xlsx)
    
Output ScreenShot: 
    * ![Que2_Ana2_OutputScreen_shot1](./Analysis%20on%20New%20York%20Times%20Data/ana_2/Que-2_Ana-2_Output1.JPG)
    * ![Que2_Ana2_OutputScreen_shot2](./Analysis%20on%20New%20York%20Times%20Data/ana_2/Que-2_Ana-2_Output2.JPG)

#####


#### Analysis-3:
*Here I wanted to find the locations from where I am getting most of the comments for the articles written in 2016 based on their section. 
We have the information of all articles of 2016 and the information of all comments made in 2016. But we don't to which section of articles for which the commenter is commenting. This data is missing in Community API files. So as I wanted the analysis only on articles of 2016,
I merged both the API's data using the url of the article which is a common filed in both APIs. So, now I can fetch the section of articles for which comment was made. I took the commenter's location from Community API and based on the url of the article I fetched the section of the article. So, I started counting the number of comments made in 2016 and on articles written in 2016 based on commenter's location. *

With this data, editor can get to know from where most of the comments are made for each section. So, he can think that people are interested for that particular section in that region. He can now focus on that section for that region.

The code and results can be found at:

#####
Code : [Que2_Ana3_Code](./Analysis%20on%20New%20York%20Times%20Data/que_2_ana_3.ipynb)

Output Files: 
    * [Que2_Ana3_Output1](./Analysis%20on%20New%20York%20Times%20Data/ana_3/Analysis_3_Sectionwise_Loctaionwise_Comments.xlsx)    
    * [Que2_Ana3_Output2](./Analysis%20on%20New%20York%20Times%20Data/ana_3/Analysis_3_Ouput_Sectionwise_Most_Least_Commenting_Locations.xlsx)
    
Output ScreenShot: 
    * ![Que2_Ana3_OutputScreen_shot1](./Analysis%20on%20New%20York%20Times%20Data/ana_3/Que-2_Ana-3_Output1.JPG)
    * ![Que2_Ana3_OutputScreen_shot1](./Analysis%20on%20New%20York%20Times%20Data/ana_3/Que-2_Ana-3_Output2.JPG)

#####
