# AROT-COV23

The AROT-COV23 (**AR**abic **O**riginal **T**weets on **COV**ID-19 as of 20**23**) dataset is a large-scale collection of original Arabic tweets related to COVID-19, spanning from January 2020 to January 2023, and the period for which we collected the data runs from January 1, 2020 to January 5, 2023. The dataset contains approximately 500,000 original tweets, providing a rich source of information on how Arabic-speaking Twitter users have discussed and shared information about the pandemic. For more details on this dataset, please see the [paper](https://openreview.net/forum?id=aUZhVQBl2W) in the citation section below.

The tweets in the AROT-COV23 dataset were collected using a set of COVID-19-related keywords in Arabic. The tweets were then filtered to ensure that they were written in Arabic. We selected three keywords related to COVID-19 for the data request, the details are in the table below.

| Keyword | Description |
| --- | --- |
| COVID-19 | Coronavirus disease 2019 (COVID-19) was released by the World Health Organization as the most common name for this disease. |
| مرض فيروس كورونا | This is Arabic for "Coronavirus Disease" (COVID-19) |
| فيروس كوفيد | This is Arabic for "Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2)" |


## Features
------------------
The dataset has the following features:

> ⚠️ Please note that due to the restrictions imposed by [Twitter's Developer Agreement and Policy on Content redistribution](https://developer.twitter.com/en/developer-terms/agreement-and-policy), the data that we make public available does not comprise direct tweet text data and user privacy data.

| Field | Type | Description |
| --- | --- | --- |
| tweet id | string | The unique identifier of the requested Tweet. |
| author id | string | The unique identifier of this user. |
| created\_at | date | Creation time of the Tweet. |
| lang | string | Language of the Tweet, if detected by Twitter. |
| like\_count | int | The number of likes on this tweet |
| quote\_count | int | The number of times this tweet has been quoted. |
| reply\_count | int | The number of replies to this tweet. |
| retweet\_count| int | The number of retweets to this tweet. |
| tweet❌ | string | The actual UTF-8 text of the Tweet. |
| user\_verified | boolean | Indicates if this user is a verified Twitter User. |
| followers\_count | int | The number of followers of the author. |
| following\_count | int | The number of following of the author. |
| tweet\_count | int | Total number of tweets by the author. |
| listed\_count | int | The number of public lists that this user is a member of. |
| name❌ | string | The name of the user. |
| username❌ | string | The Twitter screen name, handle, or alias. |
| user\_created\_at | date | The UTC datetime that the user account was created. |
| description❌ | string | The text of this user’s profile description (bio). |

## Download
------------------
You can download the dataset from [here](https://github.com/chengxuphd/AROT-COV23/tree/main/data).

- AROT-COV23_publish.csv - Contains all features except those marked with ❌ above.
- AROT-COV23_id_only.csv - Contains only tweets and their author's id.

You can get the source code of our request for tweet data to the Twitter API from [here](https://github.com/chengxuphd/AROT-COV23/tree/main/data_collection).

- Twitter_API_Request.py - A Python script for accessing the Twitter API to collect data.
- Data_Processing.py - A Python script for converting tweets json data to csv format.
- Tweets_Preprocessing.py - A Python script for pre-processing tweets data.

**If you want to access the AROT-COV23 complete version, you need to fill out this [form](https://docs.google.com/forms/d/e/1FAIpQLSdrC7VEebyH76IMXBLsruwig66SnfKOgkWGwzcYMrCokY9LSQ/viewform?usp=sf_link) to request.**

## Examples
------------------

| Field            | Value                                          |
|-----------------|------------------------------------------------|
| tweet id         | 1233338555252006918                            |
| author id        | 805692634127736832                             |
| created_at       | 2020-02-28 10:30:00+00:00                      |
| lang             | ar                                             |
| like_count       | 25                                             |
| quote_count      | 1                                              |
| reply_count      | 0                                              |
| retweet_count    | 4                                              |
| tweet            | في الصور الملتقطة 27 فبراير 2020، 2 من المرضى... |
| user_verified   | True                                           |
| followers_count  | 667414                                         |
| following_count  | 7                                              |
| tweet_count      | 121945                                         |
| listed_count     | 671                                            |
| name             | CGTN Arabic                                    |
| username         | cgtnarabic                                     |
| user_created_at  | 2016-12-05T08:37:47.000Z                       |
| description      | شبكة تلفزيون الصين الدولية مؤسسة إعلامية فريدة... |



## Citation
------------------
If you use this dataset in your research, please cite the following paper:
```bibtex
@inproceedings{xu2023arotcov,
  title={{AROT}-{COV}23: A Dataset of 500K Original Arabic Tweets on {COVID}-19},
  author={Cheng Xu and Nan Yan},
  booktitle={4th Workshop on African Natural Language Processing},
  year={2023},
  url={https://openreview.net/forum?id=aUZhVQBl2W}
}
```

## Contact
------------------
If you have any questions or comments about the dataset, please contact Cheng Xu (<cheng.xu1@ucdconnect.ie>). 

Potential cooperation in related fields is also welcome. :)
