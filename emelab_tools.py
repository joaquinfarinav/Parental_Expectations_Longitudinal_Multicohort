# Emelab tools 

# cohorts
T1 = ['2005_4b_cpad', '2009_8b_cpad', '2012_3m_cpad']
T2 = ['2007_4b_cpad', '2011_8b_cpad', '2013_2m_cpad']
T3 = ['2008_4b_cpad', '2014_2m_cpad']
T4 = ['2009_4b_cpad', '2013_8b_cpad', '2015_2m_cpad']
T5 = ['2010_4b_cpad', '2014_8b_cpad', '2016_2m_cpad']
T6 = ['2011_4b_cpad', '2013_6b_cpad', '2015_8b_cpad', '2017_2m_cpad']
T7 = ['2012_4b_cpad', '2014_6b_cpad', '2018_2m_cpad']
T8 = ['2013_4b_cpad', '2015_6b_cpad', '2017_8b_cpad']
T9 = ['2012_2b_cpad', '2014_4b_cpad', '2016_6b_cpad']
T10 = ['2013_2b_cpad', '2015_4b_cpad', '2019_8b_cpad']
T11 = ['2014_2b_cpad', '2016_4b_cpad', '2018_6b_cpad']
# not yet 
T11_pandemia = ['2014_2b_cpad', '2016_4b_cpad', '2018_6b_cpad', '2022_2m_cpad']

# two point cohorts
T12 = ['2004_8b_cpad', '2006_2m_cpad']
T13 = ['2006_4b_cpad', '2012_2m_cpad']
T14 = ['2015_2b_cpad', '2017_4b_cpad']
T15 = ['2002_4b_cpad','2008_2m_cpad']

# one point cohorts
CS1 = ['2003_2m_cpad']
CS2 = ['2007_8b_cpad']
CS3 = ['2010_2m_cpad']
CS4 = ['2018_4b_cpad']
CS5_pandemia = ['2022_4b_cpad']

# Paths
path = r'C:\Users\JoaquinFarina\OneDrive - Teachers College, Columbia University\Desktop\EMELAB\SIMCE'
EE_path = r'C:\Users\JoaquinFarina\OneDrive - Teachers College, Columbia University\Desktop\TESIS\MINEDUC'
path_cned = r'C:\Users\JoaquinFarina\OneDrive - Teachers College, Columbia University\Desktop\EMELAB\SIMCE\CNED\Cuadros_resumen'
path_esup = r'C:\Users\JoaquinFarina\OneDrive - Teachers College, Columbia University\Desktop\TESIS\MINEDUC\ESUP'


def get_tipo_ense(row):
    ens = 0
    for cod in ['ens_01', 'ens_02', 'ens_03', 'ens_04', 'ens_05', 'ens_06', 'ens_07', 'ens_08', 'ens_09', 'ens_10', 'ens_11']:
            #print(row[cod.upper()])
            if row[cod.upper()] == 110:
                ens = ens + 1
    return ens


def get_tipo_ense(row):
    ens = ''
    for cod in ['ens_01', 'ens_02', 'ens_03', 'ens_04', 'ens_05', 'ens_06', 'ens_07', 'ens_08', 'ens_09']:
            if row[cod] == 310:
                ens = ens + 'HC'
            if row[cod] == 410:
                ens = ens + 'TP'  
    return ens


def get_questions_from_questionnaire(question,df_questionaire,case):
    from fuzzywuzzy import process
    from fuzzywuzzy import fuzz
    import pandas as pd

    match_list = []
    for x in [x for x in df_questionaire.columns if 'prompt' in x]:
        print('\n',x)
        vals= list(df_questionaire[x].values)
        vals = [str(x) for x in vals if str(x) != 'nan']
        match = process.extractOne(question, vals, scorer=fuzz.ratio)     
        print(match)
        varname =  df_questionaire[df_questionaire[x] == match[0]][x.replace('prompt','key')].values[0]

        curso =  x[5:7]
        agno = x[:4]

        match_list = match_list + [[curso+agno+'_'+case,varname]]

    match_df =  pd.DataFrame(match_list,columns = ['grade_year','key'])
    return match_df


def standarizar_simce_mat(ptje,agno,curso):
    if str(ptje)!='nan':
        mean = dict_a_simce_mat[agno][curso][0]
        std = dict_a_simce_mat[agno][curso][1]
        val = (ptje-mean)/std
    else:
        val = np.nan
    return val
    
def standarizar_simce_leng(ptje,agno,curso):
    if str(ptje)!='nan':
        mean = dict_a_simce_leng[agno][curso][0]
        std = dict_a_simce_leng[agno][curso][1]
        val = (ptje-mean)/std
    else:
        val = np.nan
    return val