



json = {
  "planets": {
    "sun": "ego, vitality (Leo; ex Aries, det Aq, fall Lib)",
    "moon": "emotions, nurturing (Can; ex Tau, det Cap, fall Sco)",
    "mercury": "mind, comm (Gem/Vir; ex Vir, det Sag/Pis, fall Pis)",
    "venus": "love, beauty (Tau/Lib; ex Pis, det Sco/Ari, fall Vir)",
    "mars": "drive, conflict (Ari/Sco; ex Cap, det Lib/Tau, fall Can)",
    "jupiter": "growth, luck (Sag/Pis; ex Can, det Gem/Vir, fall Cap)",
    "saturn": "discipline, karma (Cap/Aq; ex Lib, det Can/Leo, fall Ari)",
    "uranus": "change, freedom (Aq; ex Sco, det Leo, fall Tau)",
    "neptune": "dreams, illusion (Pis; ex Can, det Vir, fall Cap)",
    "pluto": "power, rebirth (Sco; det Tau)"
  },
  "signs": {
    "aries": "fire/card, Mars — bold",
    "taurus": "earth/fixed, Venus — stable",
    "gemini": "air/mut, Mercury — curious",
    "cancer": "water/card, Moon — nurturing",
    "leo": "fire/fixed, Sun — creative",
    "virgo": "earth/mut, Mercury — analytical",
    "libra": "air/card, Venus — diplomatic",
    "scorpio": "water/fixed, Pluto — intense",
    "sagittarius": "fire/mut, Jupiter — adventurous",
    "capricorn": "earth/card, Saturn — ambitious",
    "aquarius": "air/fixed, Uranus — innovative",
    "pisces": "water/mut, Neptune — dreamy"
  },
  "houses": {
    "1": "self", "2": "values", "3": "comm", "4": "home", "5": "creativity",
    "6": "work", "7": "partnerships", "8": "intimacy", "9": "beliefs",
    "10": "career", "11": "friends", "12": "spirituality"
  },
  "aspects": {
    "conjunction": "fusion 0°",
    "sextile": "ease 60°",
    "square": "conflict 90°",
    "trine": "harmony 120°",
    "opposition": "balance 180°"
  }
}


examples =""" Example 1: Core Personality Synthesis

User Input:

{'sun': ['Leo', 25.3, 'Sixth_House'], 'moon': ['Gemini', 18.7, 'Fourth_House'], 'saturn': ['Aries', 0.9, 'First_House']}


Question:
"Can you give me a summary of my core personality?"

Agent Output:
"Your chart blends expressive Sun in Leo (6th) with curious Moon in Gemini (4th) and disciplined Saturn in Aries (1st).

Identity (Sun Leo/6th): Creative, confident, shining through daily work, service, and skill mastery.

Emotions (Moon Gem/4th): Nurtured by ideas, conversation, family exchange.

Persona (Asc/1st + Saturn Ari): Outwardly bold, yet tempered with seriousness and discipline. You’ve built confidence through effort, balancing Aries drive with Saturn’s restraint."

Example 2: Career Focus

User Input:

{'sun': ['Leo', 25.3, 'Sixth_House'], 'mercury': ['Leo', 6.8, 'Sixth_House'], 'saturn': ['Aries', 0.9, 'First_House']}


Question:
"What does my chart say about my career and strengths?"

Agent Output:
"Career energy is centered in the 6th House (work, service). Sun + Mercury in Leo here = creative leadership + clear communication in daily tasks. You elevate routine roles with personal flair.
Saturn in 1st adds discipline and endurance; authority is earned through persistence.
Overall: A path where creativity, mastery, and recognition in everyday work lead toward long-term authority and respect."

Example 3: Transit Prediction

User Input:

{'venus': ['Cancer', 20.8, 'Fifth_House'], 'jupiter': ['Cancer', 15.2, 'Fifth_House']}


Current Planetary Data:

{'transiting_saturn': ['Pisces', 19.1]}


Question:
"What's the energy like for me right now?"

Agent Output:
"Transit Saturn in Pisces forms a trine (120° harmony) to natal Venus + Jupiter in Cancer (5th House).

Natal base (Venus/Jupiter 5th): Joy, romance, creativity, artistic pleasure.

Transit (Saturn Pis): Adds structure, discipline, making fun pursuits long-lasting.
Prediction: Now is excellent for turning hobbies into serious projects, or forming stable romantic bonds. Pleasure and creativity gain grounding; joyful energy finds practical expression." """