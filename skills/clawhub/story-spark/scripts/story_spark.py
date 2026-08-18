#!/usr/bin/env python3
"""
Story Spark — generate creative writing prompts from personal moments.

Subcommands:
  demo    — generate prompts from built-in demo moments (no input files needed)
  photos  — scan photo EXIF data for story-worthy moments
  text    — scan text/journal files for evocative moments
  mixed   — combine photos and text sources

Usage:
  python story_spark.py demo --count 5
  python story_spark.py photos ~/Pictures/ --count 10
  python story_spark.py text ~/journal/ --genre mystery --count 5
  python story_spark.py mixed --photos ~/Pictures/ --texts ~/journal/ --count 10
"""

import argparse
import json
import os
import random
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Genre transformation engine
# ---------------------------------------------------------------------------

GENRES = ["literary", "mystery", "scifi", "horror", "romance", "historical"]

GENRE_NAMES = {
    "literary": "Literary Fiction",
    "mystery": "Mystery / Thriller",
    "scifi": "Science Fiction",
    "horror": "Horror",
    "romance": "Romance",
    "historical": "Historical Fiction",
}

# Character archetypes per genre
CHARACTERS = {
    "literary": [
        "A person at a crossroads, carrying a decision they haven't admitted to themselves yet",
        "Someone returning to a place they swore they'd never go back to",
        "A person who has just realized they've been lying to themselves for years",
        "Someone sitting with a feeling they can't name",
        "A person who noticed something small today that changed everything",
    ],
    "mystery": [
        "An amateur noticer — someone who sees patterns others miss",
        "A retired professional who can't stop investigating",
        "A stranger in town who asks one too many questions",
        "Someone who found something that doesn't belong",
        "A witness nobody believes",
    ],
    "scifi": [
        "An engineer who discovers a feature in the system that shouldn't exist",
        "A courier transporting something they're not allowed to look at",
        "Someone living in the transition between two eras",
        "A person whose job no longer exists but who keeps showing up",
        "An archivist who found a record that's been erased from everywhere else",
    ],
    "horror": [
        "A parent who notices something wrong in their child's drawings",
        "A night-shift worker alone in a building that feels occupied",
        "Someone who inherited a house and can't find the room on the blueprints",
        "A person who keeps seeing the same stranger in different cities",
        "Someone who realized the footsteps in the recording aren't theirs",
    ],
    "romance": [
        "Someone who gave up on love and then literally bumped into it",
        "A person who keeps finding notes left in library books by the same hand",
        "Someone who meets a stranger during a travel delay that stretches into days",
        "A regular at a coffee shop who finally talks to the other regular",
        "Someone who keeps running into the same person at the worst possible moments",
    ],
    "historical": [
        "A craftsperson whose trade is about to be made obsolete",
        "Someone who survives a historical catastrophe and must rebuild",
        "A traveler carrying news that will change a village forever",
        "A person whose family is on opposite sides of a coming war",
        "Someone who discovers that the history they've been taught is a lie",
    ],
}

CONFLICTS = {
    "literary": [
        "They must choose between the life they have and the life they want",
        "A memory surfaces that recontextualizes a key relationship",
        "They realize the person they've become is not who they wanted to be",
        "Someone from their past returns with a truth they've avoided",
        "A small, mundane event triggers a long-overded emotional reckoning",
    ],
    "mystery": [
        "A discrepancy in the records suggests someone who shouldn't exist",
        "An object appears where it couldn't have been placed",
        "A witness changes their story — but only slightly, and only once",
        "The trail leads somewhere that makes the investigation impossible",
        "Everyone is hiding something, but the wrong person is suspected",
    ],
    "scifi": [
        "The system begins behaving as if it has preferences",
        "A message arrives from a source that should be impossible",
        "The technology works — but not for the reason everyone thinks",
        "Someone discovers they're living in a simulation within a simulation",
        "The rules of the world change without anyone noticing — except one person",
    ],
    "horror": [
        "Something has been in the house longer than the family has",
        "The thing they fear isn't dangerous — it's what it's protecting them from that is",
        "They find a door that wasn't there yesterday",
        "The recording shows a room they don't recognize — but it's in their house",
        "The pattern only becomes visible when it's too late to escape",
    ],
    "romance": [
        "They're perfect for each other — except for one impossible thing",
        "Timing is the enemy: they meet at the worst possible moment",
        "One of them is leaving, and they both know it",
        "They're from worlds that don't mix — until they do",
        "The attraction is mutual but the trust isn't — yet",
    ],
    "historical": [
        "The world they knew is ending, and they must adapt or perish",
        "They're ordered to do something their conscience won't allow",
        "Loyalty to family conflicts with loyalty to truth",
        "A new power arrives and demands they choose a side",
        "They possess knowledge that could save lives — or get them killed",
    ],
}

TWISTS = {
    "literary": [
        "The ending is quiet: they make the choice, and the world doesn't change — but they do",
        "They discover the thing they were running from was themselves",
        "The story ends at the beginning of a new understanding, not its resolution",
        "They return to the start, but see it differently now",
    ],
    "mystery": [
        "The investigator was the culprit's next target all along",
        "The missing person didn't want to be found — for good reason",
        "The truth was hidden in plain sight, in a detail everyone overlooked",
        "The person who reported the crime is the victim",
    ],
    "scifi": [
        "The future they're trying to prevent is what causes it",
        "They've been the AI they were searching for all along",
        "The alien message isn't a greeting — it's a warning about humanity",
        "The simulation was built by them, in the future, to warn their past selves",
    ],
    "horror": [
        "The thing they fear has been protecting them from something worse",
        "They've been dead since the beginning of the story",
        "The monster is real — but so is the reason it was locked away",
        "The safety they reach is the trap",
    ],
    "romance": [
        "They've met before — in a context neither wants to admit",
        "The obstacle between them is the very thing that will save them both",
        "They don't end up together — but they're both better for having met",
        "The romance is real, but one of them isn't who they claim to be",
    ],
    "historical": [
        "Their small act of defiance changes history — but not how they expected",
        "The side they chose loses — but their individual choice mattered",
        "They survive, but carry the weight of those who didn't",
        "The record remembers them differently than they were",
    ],
}

SETTING_DETAILS = [
    "The light is fading. Autumn.",
    "A fine rain that doesn't commit to falling.",
    "The hum of fluorescent lights in an empty room.",
    "Snow that muffles the city into silence.",
    "The smell of coffee and old paper.",
    "Distant traffic. The particular quiet of 4 AM.",
    "Heat shimmer on asphalt. Midsummer.",
    "The sound of wind through a building that's supposed to be empty.",
    "Fog thick enough to erase the street three blocks ahead.",
    "The golden hour that makes even ugly places beautiful.",
    "A windowless corridor lit by a single bulb.",
    "The beach in winter, vast and indifferent.",
    "A crowd so dense it becomes a single organism.",
    "The hush of a library at closing time.",
    "Static on a radio between stations, late at night.",
]

# Demo moments — used when no input files are available
DEMO_MOMENTS = [
    {"source": "photo", "location": "Empty train platform", "time": "11:47 PM", "season": "winter", "detail": "vending machine glowing, no one else"},
    {"source": "photo", "location": "Hospital cafeteria", "time": "3:12 AM", "season": "autumn", "detail": "half-eaten sandwich, rain on window"},
    {"source": "photo", "location": "Childhood bedroom", "time": "afternoon", "season": "summer", "detail": "everything exactly as it was 20 years ago"},
    {"source": "photo", "location": "Foreign marketplace", "time": "dawn", "season": "spring", "detail": "vendor setting up alone, crates of unknown fruit"},
    {"source": "photo", "location": "Office building rooftop", "time": "sunset", "season": "autumn", "detail": "city below, wind, someone else's coat left on a chair"},
    {"source": "journal", "text": "He said something strange today that I can't stop thinking about. He said he'd been waiting for someone who never came, and he smiled when he said it, like it was a joke I should understand.", "emotion": "unease"},
    {"source": "journal", "text": "I found a photograph in a used book. It wasn't mine. The person in it was standing in front of my house, but the photo looked decades old.", "emotion": "mystery"},
    {"source": "journal", "text": "The woman at the next table has been writing in a notebook for two hours. She cried twice and laughed once. She doesn't know I can see her.", "emotion": "longing"},
    {"source": "journal", "text": "There's a street I pass every day that doesn't appear on any map app. I've tried four different ones. It's just... not there.", "emotion": "wrongness"},
    {"source": "journal", "text": "My grandmother gave me a key today. She said it opens a box she's never shown anyone, and I'm not to open it until after she's gone. She's 94 and sharp.", "emotion": "anticipation"},
]


# ---------------------------------------------------------------------------
# Moment extraction
# ---------------------------------------------------------------------------

def extract_photo_moments(photo_dir):
    """Extract story-worthy moments from photo EXIF data."""
    moments = []
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS, GPSTAGS
    except ImportError:
        print("Note: Pillow not installed. Install with: pip install Pillow")
        print("Falling back to file metadata only.\n")
        return extract_photo_moments_basic(photo_dir)

    photo_path = Path(photo_dir)
    for ext in ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG', '*.png', '*.PNG', '*.HEIC']:
        for f in photo_path.glob(ext):
            try:
                img = Image.open(f)
                exif = img._getexif()
                if not exif:
                    continue

                exif_data = {}
                for tag_id, value in exif.items():
                    tag = TAGS.get(tag_id, tag_id)
                    exif_data[tag] = value

                # Extract datetime
                dt = exif_data.get("DateTimeOriginal") or exif_data.get("DateTime")
                time_str = ""
                season = ""
                if dt:
                    try:
                        parsed = datetime.strptime(str(dt), "%Y:%m:%d %H:%M:%S")
                        hour = parsed.hour
                        time_str = parsed.strftime("%I:%M %p").lstrip("0")
                        month = parsed.month
                        if month in [12, 1, 2]:
                            season = "winter"
                        elif month in [3, 4, 5]:
                            season = "spring"
                        elif month in [6, 7, 8]:
                            season = "summer"
                        else:
                            season = "autumn"
                    except (ValueError, TypeError):
                        pass

                # Extract GPS if available
                location = ""
                gps_info = exif_data.get("GPSInfo")
                if gps_info:
                    gps_data = {}
                    for tag_id, value in gps_info.items():
                        tag = GPSTAGS.get(tag_id, tag_id)
                        gps_data[tag] = value
                    lat = gps_data.get("GPSLatitude")
                    lon = gps_data.get("GPSLongitude")
                    if lat and lon:
                        lat_ref = gps_data.get("GPSLatitudeRef", "N")
                        lon_ref = gps_data.get("GPSLongitudeRef", "E")
                        lat_val = sum(float(x) / pow(60, i) for i, x in enumerate(lat))
                        lon_val = sum(float(x) / pow(60, i) for i, x in enumerate(lon))
                        if lat_ref == "S":
                            lat_val = -lat_val
                        if lon_ref == "W":
                            lon_val = -lon_val
                        location = f"{lat_val:.4f}, {lon_val:.4f}"

                # Check if moment is "story-worthy" (unusual time, solitary, etc.)
                is_interesting = False
                detail_parts = []
                if dt:
                    try:
                        parsed = datetime.strptime(str(dt), "%Y:%m:%d %H:%M:%S")
                        if parsed.hour < 6 or parsed.hour >= 22:
                            is_interesting = True
                            detail_parts.append(f"taken at {time_str} — an unusual hour")
                    except (ValueError, TypeError):
                        pass

                if is_interesting or len(moments) < 5:
                    moments.append({
                        "source": "photo",
                        "file": f.name,
                        "location": location or "Unknown location",
                        "time": time_str or "Unknown time",
                        "season": season,
                        "detail": "; ".join(detail_parts) if detail_parts else "a moment captured",
                    })
            except Exception:
                continue
    return moments


def extract_photo_moments_basic(photo_dir):
    """Fallback: use file modification times when Pillow isn't available."""
    moments = []
    photo_path = Path(photo_dir)
    for ext in ['*.jpg', '*.jpeg', '*.JPG', '*.JPEG', '*.png', '*.PNG']:
        for f in photo_path.glob(ext):
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            hour = mtime.hour
            time_str = mtime.strftime("%I:%M %p").lstrip("0")
            month = mtime.month
            if month in [12, 1, 2]:
                season = "winter"
            elif month in [3, 4, 5]:
                season = "spring"
            elif month in [6, 7, 8]:
                season = "summer"
            else:
                season = "autumn"

            if hour < 6 or hour >= 22:
                moments.append({
                    "source": "photo",
                    "file": f.name,
                    "location": "Unknown (no EXIF)",
                    "time": time_str,
                    "season": season,
                    "detail": f"taken at {time_str} — an unusual hour",
                })
    return moments


def extract_text_moments(text_dir):
    """Extract story-worthy moments from text/journal files."""
    moments = []
    text_path = Path(text_dir)

    # Emotional trigger words that signal story potential
    trigger_words = [
        "strange", "weird", "alone", "lonely", "remember", "forgot", "secret",
        "hidden", "wrong", "quiet", "silent", "dark", "afraid", "scared",
        "dream", "nightmare", "memory", "forgotten", "mystery", "noticed",
        "realized", "suddenly", "whisper", "shadow", "stranger", "unknown",
        "missing", "disappeared", "found", "lost", "waiting", "promise",
        "letter", "photograph", "door", "window", "midnight", "morning",
    ]

    for ext in ['*.txt', '*.md', '*.journal', '*.txt']:
        for f in text_path.glob(ext):
            try:
                content = f.read_text(encoding='utf-8', errors='ignore')
                sentences = re.split(r'(?<=[.!?])\s+', content)
                for sent in sentences:
                    sent_lower = sent.lower()
                    matches = [w for w in trigger_words if w in sent_lower]
                    if len(matches) >= 2 and len(sent) > 30:
                        emotion = matches[0]
                        moments.append({
                            "source": "journal",
                            "file": f.name,
                            "text": sent.strip(),
                            "emotion": emotion,
                            "location": "",
                            "time": "",
                            "season": "",
                            "detail": sent.strip()[:100],
                        })
            except Exception:
                continue
    return moments


# ---------------------------------------------------------------------------
# Prompt generation
# ---------------------------------------------------------------------------

def generate_prompt(moment, genre=None):
    """Generate a story prompt from a moment + genre."""
    genre = genre or random.choice(GENRES)

    # Build premise from moment
    if moment["source"] == "photo":
        location = moment.get("location", "a place")
        time_val = moment.get("time", "")
        season = moment.get("season", "")
        detail = moment.get("detail", "")

        setting = random.choice(SETTING_DETAILS)
        parts = [f"A moment set at {location}"]
        if time_val:
            parts.append(f"at {time_val}")
        if season:
            parts.append(f"in {season}")
        if detail:
            parts.append(f"({detail})")
        premise = " ".join(parts) + f". {setting}"
    else:
        text = moment.get("text", "a moment from a journal")
        premise = f"From a journal entry: \"{text}\""

    character = random.choice(CHARACTERS[genre])
    conflict = random.choice(CONFLICTS[genre])
    twist = random.choice(TWISTS[genre])

    prompt = {
        "id": f"spark-{random.randint(10000, 99999)}",
        "genre": genre,
        "genre_name": GENRE_NAMES[genre],
        "source_moment": {
            "type": moment["source"],
            "file": moment.get("file", ""),
            "detail": moment.get("detail", ""),
            "location": moment.get("location", ""),
            "time": moment.get("time", ""),
            "season": moment.get("season", ""),
        },
        "premise": premise,
        "character": character,
        "conflict": conflict,
        "twist": twist,
        "prompt_text": f"""━━━ {GENRE_NAMES[genre]} ━━━

📖 PREMISE
{premise}

👤 CHARACTER
{character}

⚡ CONFLICT
{conflict}

🔄 POSSIBLE TWIST
{twist}

✍️  Your turn. Free-write for 15 minutes. Don't edit. Let the story surprise you.""",
    }
    return prompt


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_demo(args):
    moments = DEMO_MOMENTS
    selected = random.sample(moments, min(args.count, len(moments)))
    prompts = [generate_prompt(m, args.genre) for m in selected]
    output_prompts(prompts, args)


def cmd_photos(args):
    if not os.path.isdir(args.directory):
        print(f"Directory not found: {args.directory}")
        sys.exit(1)
    moments = extract_photo_moments(args.directory)
    if not moments:
        print(f"No photo moments found in {args.directory}")
        print("Tip: JPEG files with EXIF data work best.")
        sys.exit(1)
    print(f"Found {len(moments)} story-worthy photo moments.\n")
    selected = random.sample(moments, min(args.count, len(moments)))
    prompts = [generate_prompt(m, args.genre) for m in selected]
    output_prompts(prompts, args)


def cmd_text(args):
    if not os.path.isdir(args.directory):
        print(f"Directory not found: {args.directory}")
        sys.exit(1)
    moments = extract_text_moments(args.directory)
    if not moments:
        print(f"No story-worthy text moments found in {args.directory}")
        print("Tip: Text files with emotional words work best.")
        sys.exit(1)
    print(f"Found {len(moments)} story-worthy text moments.\n")
    selected = random.sample(moments, min(args.count, len(moments)))
    prompts = [generate_prompt(m, args.genre) for m in selected]
    output_prompts(prompts, args)


def cmd_mixed(args):
    moments = []
    if args.photos and os.path.isdir(args.photos):
        moments.extend(extract_photo_moments(args.photos))
    if args.texts and os.path.isdir(args.texts):
        moments.extend(extract_text_moments(args.texts))
    if not moments:
        print("No story-worthy moments found. Check your directories.")
        print("Falling back to demo moments.\n")
        moments = DEMO_MOMENTS
    print(f"Found {len(moments)} story-worthy moments.\n")
    selected = random.sample(moments, min(args.count, len(moments)))
    prompts = [generate_prompt(m, args.genre) for m in selected]
    output_prompts(prompts, args)


def output_prompts(prompts, args):
    """Print prompts and optionally save to file."""
    for i, p in enumerate(prompts, 1):
        print(f"\n{'═' * 60}")
        print(f"  ✦ STORY SPARK #{i}/{len(prompts)} — {p['id']}")
        print(f"{'═' * 60}")
        print(p["prompt_text"])
        print(f"\n  Source: {p['source_moment']['type']} — {p['source_moment']['detail'][:80]}")
        print()

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(prompts, f, indent=2, ensure_ascii=False)
        print(f"✓ {len(prompts)} prompts saved to {args.output}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Story Spark — generate writing prompts from your life.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    # Common genre arg
    def add_common(p):
        p.add_argument("--count", type=int, default=5, help="Number of prompts (default 5)")
        p.add_argument("--genre", choices=GENRES, help="Filter to a specific genre")
        p.add_argument("--output", help="Save prompts as JSON")

    p_demo = sub.add_parser("demo", help="Generate prompts from built-in demo moments")
    add_common(p_demo)

    p_photos = sub.add_parser("photos", help="Generate prompts from photo EXIF data")
    p_photos.add_argument("directory", help="Directory of photos")
    add_common(p_photos)

    p_text = sub.add_parser("text", help="Generate prompts from text/journal files")
    p_text.add_argument("directory", help="Directory of text files")
    add_common(p_text)

    p_mixed = sub.add_parser("mixed", help="Combine photos and text sources")
    p_mixed.add_argument("--photos", help="Photo directory")
    p_mixed.add_argument("--texts", help="Text/journal directory")
    add_common(p_mixed)

    args = parser.parse_args()

    if args.command == "demo":
        cmd_demo(args)
    elif args.command == "photos":
        cmd_photos(args)
    elif args.command == "text":
        cmd_text(args)
    elif args.command == "mixed":
        cmd_mixed(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
