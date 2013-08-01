#-*- coding: UTF-8-*-
from app import models, db

#Add categories
cat1 = models.Category(category_name="Arab Crossroads")
cat2 = models.Category(category_name="Film and New Media")
cat3 = models.Category(category_name="Chemistry")
cat4 = models.Category(category_name="Computer Science")
cat5 = models.Category(category_name="Core")
cat6 = models.Category(category_name="Economics")
cat7 = models.Category(category_name="Engineering")
cat8 = models.Category(category_name="History")
cat9 = models.Category(category_name="Mathematics")
cat10 = models.Category(category_name="Music")
cat11 = models.Category(category_name="Philosophy")
cat12 = models.Category(category_name="Physics")
cat13 = models.Category(category_name="Political")
cat14 = models.Category(category_name="Psychology")
cat15 = models.Category(category_name="Social Research and Public Policy")
cat16 = models.Category(category_name="Theater")
cat17 = models.Category(category_name="Visual Arts")
cat18 = models.Category(category_name="Litterature and Creative Writing")
cat19 = models.Category(category_name="Biology")

db.session.add_all([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10,\
                   cat11, cat12, cat13, cat14, cat15, cat16, cat17, cat18, cat19])

db.session.commit()
#db.session.rollback()


prof_list = ['Abdelall Brenda', 'Abdulkadir Rahma ', 'Acker Jennifer',\
             'Agamanolis Stefan ', 'Al-Assah Rana', 'Al-Ghoussein Tarek ',\
             'Al-Khalil Muhamed', 'Almeida Diogo ', 'Alvarez Jose ', 'Alwan Yasser',\
             'Ampka Awam ', 'Avakian Alexandra', 'Balzani Marzia', 'Barkow Rachel ',\
             'Bazzi Mohamad ', 'Bearman Peter', 'Benaych-Georges Florent', 'Berestycki Julien ',\
             'Bernstein Joel ', 'Biais Bruno ', 'Bilbiie Florin ', 'Bisin Alberto', 'Block Ned ', 'Bogomolnaia Anna ',\
             'Bouarroudj Sofiane ', 'Bougdaeva Saglar', 'Bourguignon Francois ','Bransford Jesse ', 'Bruckner Hannah', \
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
             'Odeh Sana ', 'Ogrodnik Mo ', 'OBrien John', 'Paik Christopher ',\
             'Parthesius Robert', 'Patell Cyrus ', 'Peutz Nathalie ', 'Piano Fabio', 'Polendo Ruben ', 'Puccetti Goffredo', 'Purugganan Michael',\
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

# some users:

user2 =models.User(net_id="tpn223")
user3 =models.User(net_id="mji237")
user4 =models.User(net_id="mdk353")
user5 =models.User(net_id="mtk297")


db.session.add_all([user2, user3, user4, user5])



db.session.commit()

#Add courses

course1 = models.Course(course_name="Anthropology and the Arab World"\
        , course_description= "How have anthropologists encountered,\
        written about, and produced the 'Arab world' over the past century?\
        Beginning with early Western travelers' imaginaries of Arabia and\
        ending with an ethnography of Egyptian dreamscapes, this course\
        provides an introduction to the anthropological project and to the\
        everyday realities of people living in the region. Through\
        ethnography, literature, film, and field trips, we explore such topics\
        as colonialism, nation building and development, family, gender and\
        piety, media, art and globalization, labor migration, diaspora, and\
        pilgrimage." )

course2 = models.Course(course_name="What is Music?",
course_description= "This course analyzes what we understand as\
'music.' Drawing on music of different styles from all over the world,\
we will explore what constitutes musical meaning, how it is produced,\
and how music expresses feelings. Taking advantage of the\
multicultural nature of NYUAD, we will explore the cultural and\
universal mechanisms at play when we listen and understand music. A\
lab portion of the class guides students through basic musical\
elements such as notation systems, scales, and simple compositional\
techniques.")

course3 = models.Course(course_name="What is Music?",
course_description= "This course analyzes what we understand as\
'music.' Drawing on music of different styles from all over the world,\
we will explore what constitutes musical meaning, how it is produced,\
and how music expresses feelings. Taking advantage of the\
multicultural nature of NYUAD, we will explore the cultural and\
universal mechanisms at play when we listen and understand music. A\
lab portion of the class guides students through basic musical\
elements such as notation systems, scales, and simple compositional\
techniques.")

course4 = models.Course(course_name="Innovation in the Ancient World",
course_description="This course probes the heuristics of human\
innovation in the ancient world. We study the earliest human\
inventions such as spears and simple tools; ponder the methods that\
might have been used in the construction of monolithic structures such\
as Stone Henge, Egyptian obelisks, and pyramids; and explore examples\
of technological innovations that affected the course of human\
history. Throughout the course, the emphasis is on developing personal\
approaches to creativity and innovation by studying specific examples\
of these attributes from the ancient world.")



course5 =models.Course(course_name="Bio Imaging", course_description="This course presents an introduction to image\
formation, processing, and related techniques, as they pertain to imaging of biological structures for medical and other\
 applications. Ultrasound, Magnetic Resonance Imaging, X-Ray Tomography, and Nuclear Medicine are among the topics cover\
ed, together with a hands-on introduction to biomedical image processing and pattern recognition.")

db.session.add_all([course1, course2, course3, course4, course5])

db.session.commit()

user1 = models.User.query.get(1)
user2 = models.User.query.get(2)
user3 = models.User.query.get(3)
user4 = models.User.query.get(4)
                              
course1 = models.Course.query.get(1)
course2 = models.Course.query.get(2)
course3 = models.Course.query.get(3)
course4 = models.Course.query.get(4)

from datetime import datetime
review1 = models.Review(review_date= datetime.utcnow(), review_comment="This course is so good I love it", rating =5, course_id=course1.id, user_id =user1.id)
review2 = models.Review(review_date= datetime.utcnow(), review_comment="The best course I have ever taken", rating =4, course_id=course2.id, user_id =user2.id)
review3 = models.Review(review_date= datetime.utcnow(), review_comment="I recommend this course to everyone who is curious", rating =5, course_id=course3.id, user_id =user3.id)
review4 = models.Review(review_date= datetime.utcnow(), review_comment="Man you gotta love this class", rating =3, course_id=course4.id, user_id =user4.id)

db.session.add_all([review1, review2, review3, review4])

db.session.commit()
