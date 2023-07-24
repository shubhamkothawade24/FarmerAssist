import sqlite3
conn = sqlite3.connect('farmassist_guide.sqlite')
cur = conn.cursor()
# cur.execute('CREATE TABLE crop (season VARCHAR,  nh VARCHAR,nl VARCHAR, sh VARCHAR, sl VARCHAR,northern VARCHAR,southern VARCHAR)')
# cur.execute('INSERT INTO crop (season,nh,nl,sh,sl) values ("Kharif","Sugarcane","Rice","Cotton","Maize")')
# cur.execute('INSERT INTO crop (season,nh,nl,sh,sl) values ("Rabi","Wheat","Mustard","Banana","Mango")')
# cur.execute('INSERT INTO crop (season,nh,nl,sh,sl) values ("Zaid","Cucumber","Jute","Pumpkin","Tomato")')
# cur.execute('INSERT INTO crop (northern) values ("Chandigarh  Delhi  Haryana  Himachal Pradesh  Jammu  Kashmir  Ladakh  Punjab  Rajasthan  Uttarakhand  Uttar Pradesh  Madhya Pradesh  West Bengal  Bihar  Gujarat  ")')
# cur.execute('INSERT INTO crop (southern) values ("Andhra Pradesh  Karnataka  Kerala  Lakshadweep  Puducherry  Tamil Nadu  Telangana  Chennai  Bengaluru  Hyderabad  Kochi  Warangal  Thiruvananthapuram  Coimbatore  Visakhapatanam  Mysuru  Madurai  Vijayawada Kozhikode")')
# conn.commit()

# ans = cur.execute("SELECT * FROM crop WHERE northern IS NOT NULL")
# ans = cur.fetchall()
# ans = list(ans[0][5:-1])
# print(ans)

# se = "Kharif"
# cur.execute("SELECT nh FROM crop WHERE season=?",[se])
# dd = cur.fetchall()
# dd = str(dd[0])[2:-3]
# print(dd)