import random

hindi_jokes = [
    "Teacher: Tum fail kaise ho gaye? Student: Sir, paper easy tha.. main hi tough hoon!",
    "Biwi: Suno mujhe ek mehenga gift chahiye. Pati: Theek hai recharge karwa deta hoon 299 ka!",
    "Doctor: Din me kitni chai? Patient: Sir bas do.. ek subah se shaam tak aur ek shaam se subah tak!",
    "Boy: Tum mere liye kya ho? Girl: Kya? Boy: Low battery 1 percent.. sabse important!",
    "Teacher: Newton ka sabse famous law? Student: Law of attraction!"
]

def get_joke():
    return random.choice(hindi_jokes)
