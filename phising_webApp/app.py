import flask
import pandas as pd
from urllib.parse import urlparse
import pickle

with open(f'model/model1.pkl', 'rb') as f:
    model1 = pickle.load(f)

with open(f'model/model2.pkl', 'rb') as f:
    model2 = pickle.load(f)

with open(f'model/model3.pkl', 'rb') as f:
    model3 = pickle.load(f)

with open(f'model/model4.pkl', 'rb') as f:
    model4 = pickle.load(f)




def get_file(fl):
  firstpos=fl.rfind("/")
  lastpos=len(fl)
  return fl[firstpos+1:lastpos]

def get_url_comp(url):
  df_output = pd.DataFrame(columns=['domain','path','file','param'])
  url_parse = urlparse(url)
  fle = get_file(url_parse[2])
  path = url_parse[2]
  if '.' not in fle:
      fle =''
  else:
      path.replace(fle,'')
  parts ={
        'domain':url_parse[1],
        'path':path,
        'file':fle,
        'param':url_parse[4],
    }

    #df_output = df_output.append(parts, ignore_index=True)
  df_output = pd.concat([df_output,pd.DataFrame([parts])],ignore_index=True)
  return df_output




features = ['qty_slash_url', 'qty_dot_directory', 'qty_underline_directory', 'qty_slash_directory', 'qty_questionmark_directory', 'qty_equal_directory', 'qty_at_directory', 'qty_and_directory', 'qty_exclamation_directory', 'qty_space_directory', 'qty_tilde_directory', 'qty_comma_directory', 'qty_plus_directory', 'qty_asterisk_directory', 'qty_hashtag_directory', 'qty_dollar_directory', 'directory_length', 'qty_dot_file', 'qty_underline_file', 'qty_slash_file', 'qty_questionmark_file', 'qty_equal_file', 'qty_at_file', 'qty_and_file', 'qty_exclamation_file', 'qty_space_file', 'qty_tilde_file', 'qty_comma_file', 'qty_plus_file', 'qty_asterisk_file', 'qty_hashtag_file', 'qty_dollar_file']

def get_features(url):
  url_extract = pd.DataFrame(columns=features)
  for i in range(len(url.index)):
    parts ={
        'qty_slash_url':url['domain'][i].count('/'),
        'qty_dot_directory':url['path'][i].count('.'),
        'qty_underline_directory':url['path'][i].count('_'),
        'qty_slash_directory':url['path'][i].count('/'),
        'qty_questionmark_directory':url['path'][i].count('?'),
        'qty_equal_directory':url['path'][i].count('='),
        'qty_at_directory':url['path'][i].count('@'),
        'qty_and_directory':url['path'][i].count('&'),
        'qty_exclamation_directory':url['path'][i].count('!'),
        'qty_space_directory':url['path'][i].count(' '),
        'qty_tilde_directory':url['path'][i].count('"'),
        'qty_comma_directory':url['path'][i].count(','),
        'qty_plus_directory':url['path'][i].count('+'),
        'qty_asterisk_directory':url['path'][i].count('*'),
        'qty_hashtag_directory':url['path'][i].count('#'),
        'qty_dollar_directory':url['path'][i].count('$'),
        'directory_length':len(url['path'][i]),
        'qty_dot_file':url['file'][i].count('.'),
        'qty_underline_file':url['file'][i].count('_'),
        'qty_slash_file':url['file'][i].count('/'),
        'qty_questionmark_file':url['file'][i].count('?'),
        'qty_equal_file':url['file'][i].count('='),
        'qty_at_file':url['file'][i].count('@'),
        'qty_and_file':url['file'][i].count('&'),
        'qty_exclamation_file':url['file'][i].count('!'),
        'qty_space_file':url['file'][i].count(' '),
        'qty_tilde_file':url['file'][i].count('"'),
        'qty_comma_file':url['file'][i].count(','),
        'qty_plus_file':url['file'][i].count('+'),
        'qty_asterisk_file':url['file'][i].count('*'),
        'qty_hashtag_file':url['file'][i].count('#'),
        'qty_dollar_file':url['file'][i].count('$'),
        }
    #url_extract= url_extract.append(parts, ignore_index=True)
    url_extract = pd.concat([url_extract,pd.DataFrame([parts])],ignore_index=True)
  return url_extract

def pred_out(res):
  if res==1:
    return 'Phishing'
  return 'Not a Phishing Site'


    

app = flask.Flask(__name__,template_folder ='templates')

@app.route('/',methods=['GET','POST'])
def main():
    if flask.request.method =='GET':
        return (flask.render_template('main.html'))

    if flask.request.method =='POST':
        url = flask.request.form['url']
        
        url_df = get_url_comp(url)
        

        input_df = get_features(url_df)
        
      
        pred1=pred_out(model1.predict(input_df))
        pred2=pred_out(model2.predict(input_df))
        pred3=pred_out(model3.predict(input_df))
        pred4=pred_out(model4.predict(input_df))
        
        result = {'Model 1':pred1,'Model 2':pred2,'Model 3':pred3 , 'Model 4':pred4 }
        return flask.render_template('main.html',site=url,result = result)


if __name__ == '__main__':
    app.run()
	
