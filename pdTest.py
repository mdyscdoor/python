A=[[101,'a','z'],[102,'b','y'],[103,'c','x'],[104,'d','w']]
B=[[101,'A','Z'],[102,'B','Y'],[104,'C','X'],[105,'D','W']]


import pandas as pd
dfa = pd.DataFrame(A)
dfb= pd.DataFrame(B)

dfa.columns = ['no','la','lz']
dfb.columns = ['no', 'ua', 'uz']





print(pd.concat([dfa,dfb]))


print(dfa.set_index('no').join(dfb.set_index('no')))

print(dfa.set_index('no').join(dfa.set_index('no'), rsuffix='rsfx_'))
