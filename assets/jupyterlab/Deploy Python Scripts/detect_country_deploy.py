# Generated by cpd_software_env

#wml_python_function
def score(wml_data):
    import os
    import cpd_software_env  # import auto-installer before other modules
    # install commands are run automatically as part of the import
    
    # An input data argument (usually the first one) may contain environment variables;
    # map them to the local session and download any pending assets.      
    for elem in wml_data['input_data']:
        assert isinstance(elem,dict)
        envdict = elem.get('environment_variables')
        if envdict:
            assert isinstance(envdict,dict)
            for var,val in envdict.items():
                os.environ[var] = val
            cpd_software_env.download_pending_assets()
            
    # access sample_function_class after assets have been downloaded
    from sample_function_class import detect_country
    # map input data to function
    # detect_country(text: str) -> str
    data = wml_data['input_data']
    assert isinstance(data,list), 'input_data must be a list'
    if len(data)==1 and 'tail' in data[0]:
        assert isinstance(data[0]['tail'],list), 'input_data tail must be a list'
        data += data[0]['tail']
    if 0>=len(data) : raise ValueError('Too few arguments in input data for deployed function detect_country')
    val_text = str(data[0]['values'][0])
    scorefn_res = detect_country(text=val_text)
    score_res = scorefn_res

    # WML expects { 'predictions': [some_dictionary] }
    if isinstance(score_res,dict):
        return { 'predictions': [score_res] }
    else:
        result = {}
        #result['autoinstall msgs'] = cpd_software_env.get_msgs()   
        result['score'] =  score_res
        return { 'predictions': [result] }
