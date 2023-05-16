import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.title('🥣 My snowflake bedge 2 practice');
streamlit.header('🥗 Snowflake');
# streamlit.text('🐔 streamlit text');
streamlit.text('🥑 trying to resolve error');
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit');
# streamlit.dataframe(my_fruit_list);
# Let's put a list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon','Lime','Orange']);
# display the table on the page
fruits_to_show = my_fruit_list.loc[fruits_selected];
streamlit.dataframe(fruits_to_show);

#streamlit.header("Build your own fruit Smoothie");
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon");
# streamlit.text(fruityvice_response.json());

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi");

# take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
#streamlit.dataframe(fruityvice_normalized);

#New section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
# try:
#fruit_choice = streamlit.text_input('What fruit would you like information about?')
# if not fruit_choice:
   # streamlit.error("Please select a fruit to get information.")
# else:
  # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice);
   # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 #   streamlit.dataframe(fruityvice_normalized);
 # except URLError as e:
 # streamlit.error()
  
import requests

# don't run anything past here while we troubleshoot
streamlit.stop()

import snowflake.connector
from urllib.error import URLError

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list");
# CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

streamlit.header("Fruityvice Fruit Advice!");
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit'); #fruit_choice

#streamlit.write('Thanks for adding', fruit_choice);  

streamlit.write('Thanks for adding', add_my_fruit);
my_cur.execute("insert into fruit_load_list values('from streamlit')");
# don't run anything past here while we troubleshoot
streamlit.stop()
