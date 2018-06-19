# fb-messenger-analytics
A python script to extract FB messenger data from the JSON format provided by FB to a table format (and csv)

## How to use the script
1. Download your FB messenger data in the `JSON` format in your privacy settings ([link](https://www.facebook.com/help/1701730696756992?helpref=hc_global_nav) to FB FAQ for details) 
```diff
- Don't forget to change the default format from HTML to JSON when you download your data
```
2. Clone the repo in your computer
3. When you have the file from FB, copy the `messages` folder provided by FB in the repo
4. Navigate to the repo with the terminal `$cd repo_name`
5. Install required packages using pip for your python 3 distribution `$pip3 install -r requirements.txt`
6. Run the script `$python3 messenger_analysis.py` 
7. The script will scroll through you messages and create three CSVs in a new directory called `csv_output` in the repo 

## Data Structure
The script create 3 tables from your FB messages: 
- message_extract.csv: contains the main content of each messages
- meta_extract.csv: contains the meta data of each message thread
- part_extract.csv: contains the lsit of participant of each message_thread
The key to link this tables together is `thread_path`

## Analysis
I am building a jupyter notebook template for you to be able to graph you messenger data. I will push the notebook in this repo. It is a WIP, stay tuned.
