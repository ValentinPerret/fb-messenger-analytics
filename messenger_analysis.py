import json
import pandas as pd
import inspect, os
import fnmatch
import codecs

def data_extraction(path):
	'''
	Input: path to the JSON data folder downloaded from FB
	Output: csv for the message table, the meta table and the participants table 
	'''
	output_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

	message_df = pd.DataFrame()
	meta_df = pd.DataFrame()
	part_df = pd.DataFrame()

	for path,dirs,files in os.walk(path):
		for f in fnmatch.filter(files,'*.json'):
			message_path = os.path.join(path, f)
			with codecs.open(message_path, encoding='utf-8') as jsonfile:
				# move from JSON to dict
				data = json.load(jsonfile)

				# Extract messages from dict
				message_df_temp = pd.DataFrame(data['messages'])
				message_df_temp['thread_path'] = data['thread_path']
				message_df = pd.concat([message_df, message_df_temp], ignore_index = True)
				print('{} message data extracted'.format(data['thread_path']))

				# Extract participants from dict
				try:
					part_df_temp = pd.DataFrame(data['participants'])
					part_df_temp['thread_path'] = data['thread_path']
					part_df = pd.concat([part_df, part_df_temp], ignore_index = True)
					print('{} participants data extracted'.format(data['thread_path']))
				except:
					continue

				# Extract metadata from dict
				data.pop('messages')
				data.pop('participants')
				meta_df_temp = pd.DataFrame(data, index = [0])
				meta_df = pd.concat([meta_df, meta_df_temp], ignore_index = True)
				print('{} metadata data extracted'.format(data['thread_path']))


	# Clean data format
	message_df = message_format_cleaning(message_df)
	# Output CSV files
	message_csv_name = '{}/csv_output/message_extract.csv'.format(output_path)
	meta_csv_name = '{}/csv_output/meta_extract.csv'.format(output_path)
	part_csv_name = '{}/csv_output/part_extract.csv'.format(output_path)
	# for encoding in ('utf-8', 'latin1'):
	for encoding in (['latin1']):
		message_df.to_csv(message_csv_name.format(encoding), encoding = encoding)
		part_df.to_csv(part_csv_name.format(encoding), encoding = encoding)
		meta_df.to_csv(meta_csv_name.format(encoding), encoding = encoding)
	return message_df, meta_df, part_df

def message_cleaning(csv_path):
	'''
	Input: csv path of the message table
	Output: data frame with the good table format 
	'''
	df = pd.read_csv(csv_path)
	df = df.where((pd.notnull(df)), None)
	df['timestamp'] = pd.to_datetime(df['timestamp'], unit = 's')
	message_df.to_csv(csv_path)
	return df

def message_format_cleaning(df):
	'''
	Input: message dataframe
	Output: datafraome with NA as Null and timestamps as datetime
	'''
	df = df.where((pd.notnull(df)), None)
	df['timestamp'] = pd.to_datetime(df['timestamp'], unit = 's')
	return df

if __name__ == "__main__":
	path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/messages'
	data_extraction(path)