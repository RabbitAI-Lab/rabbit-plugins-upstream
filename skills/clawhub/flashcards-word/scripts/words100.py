# -*- coding: utf-8 -*-
"""40 simple English words for a 5-year-old, as flashcards.
Each entry: (word, "", emoji_unicode). The middle "" slot is unused for
English (no pinyin) so the card shows picture + big word.
Keep: unique words, multiple of 4, kid-appropriate, short.
"""
WORDS = [
    # animals
    ("cat",        "", "🐱"),
    ("dog",        "", "🐶"),
    ("bird",       "", "🐦"),
    ("fish",       "", "🐟"),
    ("cow",        "", "🐮"),
    ("pig",        "", "🐷"),
    ("duck",       "", "🦆"),
    ("rabbit",     "", "🐰"),
    # food
    ("apple",      "", "🍎"),
    ("banana",     "", "🍌"),
    ("watermelon", "", "🍉"),
    ("egg",        "", "🥚"),
    ("milk",       "", "🥛"),
    ("cake",       "", "🍰"),
    ("cookie",     "", "🍪"),
    ("cheese",     "", "🧀"),
    ("ice cream",  "", "🍦"),
    # body
    ("eye",        "", "👁️"),
    ("nose",       "", "👃"),
    ("hand",       "", "✋"),
    ("ear",        "", "👂"),
    ("mouth",      "", "👄"),
    # colors
    ("red",        "", "🔴"),
    ("blue",       "", "🔵"),
    ("yellow",     "", "🟡"),
    ("green",      "", "🟢"),
    ("orange",     "", "🟠"),
    ("purple",     "", "🟣"),
    # nature
    ("sun",        "", "☀️"),
    ("moon",       "", "🌙"),
    ("star",       "", "⭐"),
    ("rain",       "", "🌧️"),
    ("snow",       "", "❄️"),
    ("flower",     "", "🌸"),
    ("tree",       "", "🌳"),
    ("grass",      "", "🌿"),
    # objects
    ("ball",       "", "⚽"),
    ("book",       "", "📖"),
    ("house",      "", "🏠"),
    ("car",        "", "🚗"),
]

if __name__ == "__main__":
    words = [w[0] for w in WORDS]
    assert len(words) == len(set(words)), "DUPLICATE words!"
    assert len(words) % 4 == 0, "word count must be a multiple of 4"
    print(f"OK: {len(WORDS)} unique English words")
