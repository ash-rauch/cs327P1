

# This file was *autogenerated* from the file modexp.sage
from sage.all_cmdline import *   # import sage library

_sage_const_96869613754622061477140922254355882905759991124574319874695120930816298225145708356931476622883989628013391990551829945157815154 = Integer(96869613754622061477140922254355882905759991124574319874695120930816298225145708356931476622883989628013391990551829945157815154); _sage_const_106698614368578024442868771328920154780709906633937862801226224496631063125911774470873340168597462306553968544513277109053606095 = Integer(106698614368578024442868771328920154780709906633937862801226224496631063125911774470873340168597462306553968544513277109053606095); _sage_const_114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541 = Integer(114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541)
a = _sage_const_96869613754622061477140922254355882905759991124574319874695120930816298225145708356931476622883989628013391990551829945157815154 
b = _sage_const_106698614368578024442868771328920154780709906633937862801226224496631063125911774470873340168597462306553968544513277109053606095  
c = _sage_const_114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541 
#d = power_mod(a,b,c)
d = a.powermod(b, c)
print ('a^b mod c = ', a, '^', b, ' mod ', c, ' = ', d)

