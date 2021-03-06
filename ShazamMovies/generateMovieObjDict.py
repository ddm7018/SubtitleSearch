from movieObj import movieObj
import pickle

movieObjDict = dict()

movieObjDict["Inception.srt"] 									= movieObj("Inception","inception.jpg")
movieObjDict["social_network.srt"]								= movieObj("Social Network","sn.jpg")
movieObjDict['Birdman.srt']										= movieObj("Birdman","b.jpg")
movieObjDict['carol.srt']										= movieObj("Carol","c.jpg")
movieObjDict['Comfort_and_Joy.srt']								= movieObj("Comfort and Joy","c1.jpg")
movieObjDict['Deadpool.srt'] 									= movieObj("Deadpool","d.jpg")
movieObjDict['Dilwale.srt']										= movieObj("Dilwale","d1.jpg")
movieObjDict['District_9.srt']									= movieObj("District 9","d2.jpg")
movieObjDict['Django_Unchained.srt']							= movieObj("Django Unchained","dj.jpg")
movieObjDict['Fifty_Shades_Of_Gray.srt']						= movieObj("Fifty Shades","five.jpg")
movieObjDict['Fight_Clup.srt']									= movieObj("Fight Club","fight.jpg")
movieObjDict['Forrest Gump (1994).DVDRip.UnSeeN.en.srt']		= movieObj("Forrest Gump","fg.jpg")
movieObjDict['Gladiator.720p.SiLU.en.srt']						= movieObj("Gladiator","g.jpg")
movieObjDict['Goodfellas (1990).DVDRip.en.srt']					= movieObj("Goodfellas","good.jpg")
movieObjDict['Green Mile The(1999).en.srt']						= movieObj("Green Mile","green.jpg")
movieObjDict['Halloween.srt']									= movieObj("Halloween","hall.jpg")
movieObjDict['Hangover.srt']									= movieObj("Hangover","hang.jpg")
movieObjDict['Highway.srt']										= movieObj("Highway","highway.jpg")
movieObjDict['Interstellar.1080p.BlueRay.RARBG.en.srt']			= movieObj("Interstellar","i.jpg")
movieObjDict['Kung_Fu_Panda.srt']								= movieObj("Kung Fu Panda","kf.jpg")
movieObjDict['Lion King The.DVDRip.en.srt']						= movieObj("Lion King","lk.jpg")
movieObjDict['Lucy.srt']										= movieObj("Lucy","lucy.jpg")
movieObjDict['Mad_Max_Fury_Road.srt']							= movieObj("Mad Max Fury Road", "mad.jpg")
movieObjDict['Moneyball.srt']									= movieObj("Moneyball", "money.jpg")
movieObjDict['Nightmare_on_elm_st.srt']							= movieObj("Nightmare on Elm Street", "nightmare.jpg")
movieObjDict['Osaka_Tough_Guys.srt']							= movieObj("Osaka Tough Guys","os.jpeg")
movieObjDict['Psycho.srt']										= movieObj("Pyscho","p.jpg")
movieObjDict['Pulp Fiction (1994).en.srt']						= movieObj("Pulp Fiction","pulp.jpg")
movieObjDict['Room.srt']										= movieObj("Room","room.jpg")
movieObjDict['Saving_Prvt_Ryan.srt']							= movieObj("Saving Private Ryan","svp.jpg")
movieObjDict['Se7en Seven (1995).en.srt']						= movieObj("Seven","7.jpg")
movieObjDict['seven_day_hell.srt']								= movieObj("Seven day hell","sevenday.jpg")
movieObjDict['Shawshank Redemption The.DVDRip.en.srt']			= movieObj("Shawshank Redemption","shaw.jpg")
movieObjDict['Sisters.srt'] 									= movieObj("Sisters","sis.jpg")
movieObjDict['slumdog.srt']										= movieObj("Slumdog","slum.jpg")			
movieObjDict['Spotlight.srt']									= movieObj("Spotlight","spot.jpg")
movieObjDict['The_Dark_Night.srt']								= movieObj("Dark Knight","dark.jpg")
movieObjDict['The_Departed.srt']								= movieObj("The Departed","depart.jpg")
movieObjDict['The_Imitation_Game.srt']							= movieObj("The Imitation Game","game.jpeg")
movieObjDict['The_Maritian.srt']								= movieObj("The Maritian","mart.jpg")
movieObjDict['The_Mutilator.srt']								= movieObj("The Mutilator","mut.jpg")	
movieObjDict['the_rev.srt']										= movieObj("The Rev","rev.jpg")	
movieObjDict['The_Revenant.srt']								= movieObj("The Revenant","rev.jpg")
movieObjDict['titanitc.srt']									= movieObj("Titanic", "t.jpg")	

pickle.dump(movieObjDict,open("dict.p","wb"))