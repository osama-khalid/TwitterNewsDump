import requests
import urllib

A='''BD:"Bangladesh",BE:"Belgium",BF:"Burkina Faso",BG:"Bulgaria",BA:"Bosnia and Herzegovina",BN:"Brunei",BO:"Bolivia",JP:"Japan",BI:"Burundi",BJ:"Benin",BT:"Bhutan",JM:"Jamaica","US-NH":"New Hampshire",BW:"Botswana",BR:"Brazil",BS:"The Bahamas","US-NC":"North Carolina",BY:"Belarus",BZ:"Belize","US-NE":"Nebraska","US-VA":"Virginia",RU:"Russia",RW:"Rwanda","US-ME":"Maine",RS:"Republic of Serbia",TL:"East Timor",TM:"Turkmenistan",TJ:"Tajikistan",RO:"Romania","US-FL":"Florida",GW:"Guinea Bissau",
GT:"Guatemala",GR:"Greece",GQ:"Equatorial Guinea","US-WI":"Wisconsin","US-NV":"Nevada","US-OR":"Oregon","US-CO":"Colorado",GY:"Guyana","US-OH":"Ohio",GE:"Georgia",GB:"United Kingdom",GA:"Gabon","US-SD":"South Dakota","US-WY":"Wyoming",GN:"Guinea",GM:"Gambia",GL:"Greenland",GH:"Ghana","US-NJ":"New Jersey",OM:"Oman",TN:"Tunisia",_3:"Somaliland",_2:"Western Sahara",_1:"Kosovo",_0:"Northern Cyprus","US-GA":"Georgia",JO:"Jordan","US-SC":"South Carolina","US-VT":"Vermont","US-TN":"Tennessee",HR:"Croatia",
"US-NM":"New Mexico",HT:"Haiti",HU:"Hungary","US-TX":"Texas",HN:"Honduras",PR:"Puerto Rico",PS:"West Bank",PT:"Portugal",PY:"Paraguay","US-NY":"New York",PA:"Panama",PG:"Papua New Guinea",PE:"Peru",PK:"Pakistan",PH:"Philippines","US-DC":"District of Columbia","US-DE":"Delaware",PL:"Poland","US-CT":"Connecticut",ZM:"Zambia",EE:"Estonia","US-MI":"Michigan",EG:"Egypt","US-RI":"Rhode Island",ZA:"South Africa",EC:"Ecuador",IT:"Italy",VN:"Vietnam",SB:"Solomon Islands",ET:"Ethiopia",SO:"Somalia",ZW:"Zimbabwe",
ES:"Spain",ER:"Eritrea",ME:"Montenegro",MD:"Moldova",MG:"Madagascar","US-MD":"Maryland",MA:"Morocco","US-MA":"Massachusetts",UZ:"Uzbekistan",MM:"Myanmar",ML:"Mali",MN:"Mongolia",MK:"Macedonia",MW:"Malawi","US-MT":"Montana","US-MS":"Mississippi",MR:"Mauritania",UG:"Uganda",MY:"Malaysia",MX:"Mexico",VU:"Vanuatu",FR:"France","US-ID":"Idaho",FI:"Finland",FJ:"Fiji",FK:"Falkland Islands","US-PA":"Pennsylvania",NI:"Nicaragua","US-UT":"Utah",NL:"Netherlands","US-WA":"Washington",NO:"Norway",NA:"Namibia",
NC:"New Caledonia",NE:"Niger",NG:"Nigeria",NZ:"New Zealand",NP:"Nepal",CI:"Ivory Coast",CH:"Switzerland",CO:"Colombia",CN:"China",CM:"Cameroon",CL:"Chile",CA:"Canada",CG:"Republic of the Congo",CF:"Central African Republic",CD:"Democratic Republic of the Congo",CZ:"Czech Republic",CY:"Cyprus",CR:"Costa Rica",CU:"Cuba","US-IN":"Indiana",SZ:"Swaziland",SY:"Syria",KG:"Kyrgyzstan",KE:"Kenya",SS:"South Sudan",SR:"Suriname",KH:"Cambodia","US-CA":"California",SV:"El Salvador",SK:"Slovakia",KR:"South Korea",
SI:"Slovenia",KP:"North Korea",KW:"Kuwait",SN:"Senegal",SL:"Sierra Leone",KZ:"Kazakhstan",SA:"Saudi Arabia",SE:"Sweden",SD:"Sudan",DO:"Dominican Republic",DJ:"Djibouti",DK:"Denmark",DE:"Germany",YE:"Yemen",AT:"Austria",DZ:"Algeria",US:"United States of America",UY:"Uruguay","US-MO":"Missouri",LB:"Lebanon","US-KS":"Kansas",LA:"Laos","US-HI":"Hawaii",TW:"Taiwan",TT:"Trinidad and Tobago",TR:"Turkey",LK:"Sri Lanka",LV:"Latvia",LT:"Lithuania",LU:"Luxembourg",LR:"Liberia",LS:"Lesotho",TH:"Thailand",TF:"French Southern and Antarctic Lands",
TG:"Togo",TD:"Chad","US-MN":"Minnesota",LY:"Libya","US-LA":"Louisiana",AE:"United Arab Emirates",VE:"Venezuela",AF:"Afghanistan",IQ:"Iraq","US-KY":"Kentucky",IS:"Iceland",IR:"Iran",AM:"Armenia",AL:"Albania",AO:"Angola","US-IA":"Iowa",AR:"Argentina",AU:"Australia",IL:"Israel",IN:"India",TZ:"Tanzania","US-ND":"North Dakota",AZ:"Azerbaijan",IE:"Ireland",ID:"Indonesia","US-IL":"Illinois","US-AK":"Alaska","US-AL":"Alabama",UA:"Ukraine","US-WV":"West Virginia","US-OK":"Oklahoma",QA:"Qatar","US-AZ":"Arizona",
"US-AR":"Arkansas",MZ:"Mozambique"'''

A= A.replace("\n","")
A= A.replace('"',"")
i=0
len(A)
StartName=0
while StartName>-1:
    NameStart=':'
    NameEnd=','
    i=i+1
   
   
    StartName= A.find(NameStart)
   
    EndName=A[StartName+1:].find(NameEnd)
    if EndName >-1:
        A=A[:StartName]+A[StartName+1+EndName:]
    else:
        A=A[:StartName]
    
A=A.split(",")
print A
NewsMap=open("ListofPub.tsv", "w")
for i in range(0,len(A)):
    
    header="http://newsmap.mhlakhani.com/data/"
    Location=header+A[i] #Songs
    r = requests.get(Location)
    outPut=r.content
    if outPut.find("<title>") <0:
        NewsMap.write(A[i]+": "+outPut)
    
    
    