#-*- coding: UTF-8-*-
from app import models, db

#Add categories
cat1 = models.Category(category_name="Arab Crossroads")
cat2 = models.Category(category_name="Film and New Media ")
cat3 = models.Category(category_name="Chemistry ")
cat4 = models.Category(category_name="Computer Science")
cat5 = models.Category(category_name="Cores ")
cat6 = models.Category(category_name="Economics")
cat7 = models.Category(category_name="Engineering")
cat8 = models.Category(category_name="History ")
cat9 = models.Category(category_name="Mathematics ")
cat10 = models.Category(category_name="Music")
cat11 = models.Category(category_name="Philosophy")
cat12 = models.Category(category_name="Physics")
cat13 = models.Category(category_name="Political")
cat14 = models.Category(category_name="Psychology")
cat15 = models.Category(category_name="Social Research and Public Policy")
cat16 = models.Category(category_name="Theater")
cat17 = models.Category(category_name="Visual Arts")
cat18 = models.Category(category_name="Litterature and Creative Writing")
cat19 = models.Category(category_name="Biology ")

#db.session.add_all([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10,\
                   #cat11, cat12, cat13, cat14, cat15, cat16, cat17, cat18, cat19])

#db.session.commit()
db.session.rollback()


prof_list = ['Abdelall Brenda', 'Abdulkadir Rahma ', 'Acker Jennifer',\
             'Agamanolis Stefan ', 'Al-Assah Rana', 'Al-Ghoussein Tarek ',\
             'Al-Khalil Muhamed', 'Almeida Diogo ', 'Alvarez Jose ', 'Alwan Yasser',\
             'Ampka Awam ', 'Avakian Alexandra', 'Balzani Marzia', 'Barkow Rachel ',\
             'Bazzi Mohamad ', 'Bearman Peter', 'Benaych-Georges Florent', 'Berestycki Julien ',\
             'Bernstein Joel ', 'Biais Bruno ', 'Bilbiie Florin ', 'Bisin Alberto', 'Block Ned ', 'Bogomolnaia Anna ',\
             'Bouarroudj Sofiane ', 'Bougdaeva Saglar', 'Bourguignon Francois ','Bransford Jesse ', u'Br\xfcckner Hannah', \
             'Buarque de Hollanda Cristina ', 'Buchanan Bruce', 'Burt John ', 'Cai David ', 'Camia Federico', \
             'Carey Susan ', 'Cesarini David', 'Chacon Mario', 'Chandra Kanchan ', 'Charlier Celina ', 'Chassagneux Jean-Francois ',\
             'Chaudhuri Una', 'Chen Jay ', 'Ciezadlo Annia', 'Coleman Jules', 'Cook Douglas ', 'Copti Scandar', 'Coray Catherine ', 'Daughtry Martin',\
             'Dave Chetan ', 'Derluguian Georgi ', 'Desplan Claude ', 'Dimitri Alexandra ', 'Dixon Jo ', 'Djouma Georges ', 'Dore Tim ', 'El Araby Omima ', \
             'El Saddik Abdulmotaleb ', 'Emerson Jed ', 'England Paula','Eynot Tzipora ', 'Ezgi Defne', 'Falkenburg Reindert', 'Feldman Walter',\
             'Fitzgerald Scott ', 'Friedland Roger ', 'Gelfand Joseph','Gladish Carl', 'Guedes Carlos', 'Haefke Christian ', 'Haykel Bernard',\
             'Hedstrom Peter', 'Helmrich Leonard', 'Henry PJ', 'Hix Simon', 'Holmes Stephen ', 'Horta Paulo', 'Hudson Dale ', 'Imbs Jean',\
             'Isleem Nasser ', 'Jagannathan Ramesh', 'Jarjour Tala', 'Jensen Jeffrey ', 'Jeong Seung-Hoon ', 'Jiao Xiao Xiao ', 'Kennedy Philip',\
             'Khapli Sachin ', 'King Jason ', 'Kittaneh Khulood', 'Klass Perri',\
             'Klimke Martin', 'Klinenberg Eric ', 'Klingermann Hans-Dieter ', 'Koss Brian ', 'Koussa Joseph ', 'Kronman Anthony ', 'Kuhlke Kevin', 'Kumar Sunil ',\
             'Laver Michael ', 'Le Jan Yves', 'Leahy John', 'Levine Debra', 'Magzoub Mazin', 'Majithia Sheetal ', 'Major Charlie', 'Malik Samreen ', \
             'Manza Jeff ', 'Maudlin Timothy ', 'Mayoral Laura', 'McGlennon David ', 'Menoret Pascal ', 'Michael Marc', 'Mihm Maximilian ', 'Miller Judith',\
             'Minsky Lauren ', 'Minsky Amir ',\
             'Mitsis Phil ', 'Morning Ann', 'Morton Rebecca ', 'Moulin Herve ',\
             'Naumov Pance ', 'Neuber Wolfgang', 'Noury Abdul ', 'Nyarko Yaw',\
             'Odeh Sana ', 'Ogrodnik Mo ', u'O\x92Brien John', 'Paik Christopher ',\
             'Parthesius Robert', 'Patell Cyrus ', 'Peutz Nathalie ', 'Piano Fabio', u'Polendo Rub\xe9n ', 'Puccetti Goffredo', 'Purugganan Michael',\
             'Pycke Jean-Renaud ', 'Quadflieg Susanne ', 'Quayle Matthew', 'Rabeh Wael ', 'Ramey Adam ', 'Ranciere Romain', 'Ray Debraj ', 'Riordan Kevin ', \
             'Roberts Mallory', 'Roth Nadine ', 'Saint-Paul Gilles ',\
             'Salehi-Ashtiani Kourosh', 'Sanders Lamar ', 'Savio Joanne ', 'Savio Jim', 'Scicchitano David ', 'Segal Gail', 'Sexton John ', 'Shah Nishi',\
             'Shao Qiuxia ', 'Shariff Azim ', 'Shasha Dennis', 'Shiffman Daniel', 'Shohat Ella', 'Silverstein Matthew ', 'Sinanoglu Ozgur ', 'Siskin Clifford ',\
             'Sissel Sandra ', 'Skop Ahna ', 'Smith Shafer ', 'Smith Roy ', 'Sreenivasan Katepalli ', 'Stalla Heidi ', 'Stam Robert ',\
             'Stearns Justin ', 'Stimpson Catharine', 'Sunder Rajan Rajeswari ',\
             'Swislocki Mark ', 'Szelenyi Ivan', 'Tan Ignatius ', 'Thom Kevin ',\
             'Torche Florencia ', 'Torreano John ', 'Toussaint Godfried ','Trabolsi Ali ', 'Traub James ', 'Tsishchanka Kiryl ', 'Tucker Joshua', \
             'Verdier Thierry ', 'Volk Tyler', 'Waley-Cohen Joanna', 'Waterbury John ', 'Waterman Bryan ', 'Way Niobe ', 'Westermann Mariet ',\
             'Williams Deborah ', 'Wilson Charles ', 'Wolff Larry ', 'Zaloom Caitlin ', 'Zamir Shamoon ', 'Zaw Ingyin ', 'Zimmerman Jonathan',\
             'Ziter Edward ', 'Zogby James']

#Add professors
for i in range(198):
    prof= models.Professor(professor_name = prof_list[i])
    db.session.add(prof)

db.session.commit()
















 

