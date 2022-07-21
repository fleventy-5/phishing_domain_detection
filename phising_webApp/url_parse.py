import pandas as pd
from urllib.parse import urlparse

def get_file(fl):
  firstpos=fl.rfind("/")
  lastpos=len(fl)
  return fl[firstpos+1:lastpos]

def get_url_comp(url):
  df_output = pd.DataFrame(columns=['domain','path','file','param'])
  for i in url:
    url_parse = urlparse(i)
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

urls = [
    'https://www.google.com/search?q=how+to+dispose+of+a+corpse&oq=how+to+dispose+of+a+corpse&aqs=chrome..69i57j69i64.4925j1j7&sourceid=chrome&ie=UTF-8',
    'https://tales.as/101-things-to-do-with-a-dead-body_9780997711639?utm_source=google-shopping&utm_medium=cpc&utm_campaign=',
    'https://www.worldofbooks.com/en-gb/books/hugh-whitemore/disposing-of-the-body/9781872868271#NGR9781872868271',
    'https://www.google.com/search?q=where+to+buy+hydrofluoric+acid&oq=where+to+buy+hydrofl&aqs=chrome.1.69i57j0l2j0i10j0i10i395j0i395i457j0i10i395l2.8058j1j7&sourceid=chrome&ie=UTF-8',
    'http://173-254-91-220.unifiedlayer.com/mxndoc/verificationAttempt.php?sf58gfd1s689sxd2sdf8angf264s9df23sd2f1n495K3L2C151645172991f1477dbd26917ef3822423f62e984a91f1477dbd26917ef3822423f62e984a91f1477dbd'
]

#df = get_url_comp(urls)
#print(df.head())

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

#df_url = get_features(df)
#print(df_url.head())




