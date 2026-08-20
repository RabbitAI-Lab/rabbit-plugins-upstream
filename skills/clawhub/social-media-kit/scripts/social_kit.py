#!/usr/bin/env python3
"""
Social Media Kit — Generate a complete week of social media content
for all major platforms from a single topic or brand.

Usage:
  python social_kit.py generate --topic 'sustainable fashion' --brand 'EcoThreads'
  python social_kit.py generate --topic 'AI productivity' --days 14 --platforms twitter,linkedin
  python social_kit.py calendar content.json --output calendar.html
  echo 'organic coffee roastery in Brooklyn' | python social_kit.py --auto

Author: Denis Voronin
License: MIT
Version: 1.0.0
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta


VERSION = "1.0.0"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ──────────────────────────────────────────────
# Platform definitions
# ──────────────────────────────────────────────

PLATFORMS = {
    "twitter": {
        "label": "Twitter/X",
        "icon": "𝕏",
        "icon_emoji": "🐦",
        "char_limit": 280,
        "optimal_chars": "71-100",
        "hashtag_count": "1-2",
        "hashtag_max": 2,
        "best_times": ["9:00 AM", "12:00 PM", "5:00 PM"],
        "best_days": "Tue-Thu",
        "color": "#1DA1F2",
        "bg_color": "#E8F5FE",
    },
    "instagram": {
        "label": "Instagram",
        "icon": "📷",
        "icon_emoji": "📷",
        "char_limit": 2200,
        "optimal_chars": "138-150",
        "hashtag_count": "10-15",
        "hashtag_max": 15,
        "best_times": ["11:00 AM", "1:00 PM", "7:00 PM"],
        "best_days": "Wed, Fri",
        "color": "#E4405F",
        "bg_color": "#FCE4EC",
    },
    "linkedin": {
        "label": "LinkedIn",
        "icon": "in",
        "icon_emoji": "💼",
        "char_limit": 3000,
        "optimal_chars": "1,200-1,900",
        "hashtag_count": "3-5",
        "hashtag_max": 5,
        "best_times": ["8:00 AM", "10:00 AM", "12:00 PM"],
        "best_days": "Tue-Thu",
        "color": "#0A66C2",
        "bg_color": "#E3F2FD",
    },
}

# ──────────────────────────────────────────────
# Content types — 70-20-10 rule + BTS + UGC
# ──────────────────────────────────────────────

CONTENT_TYPES = {
    "educational": {
        "label": "Educational",
        "emoji": "📚",
        "color": "#2563EB",
        "bg_color": "#EFF6FF",
        "border_color": "#3B82F6",
        "target_pct": 0.40,
    },
    "promotional": {
        "label": "Promotional",
        "emoji": "🟢",
        "color": "#16A34A",
        "bg_color": "#F0FDF4",
        "border_color": "#22C55E",
        "target_pct": 0.15,
    },
    "engaging": {
        "label": "Engaging",
        "emoji": "❓",
        "color": "#EA580C",
        "bg_color": "#FFF7ED",
        "border_color": "#F97316",
    },
    "behind_the_scenes": {
        "label": "Behind-the-Scenes",
        "emoji": "🎬",
        "color": "#7C3AED",
        "bg_color": "#F5F3FF",
        "border_color": "#8B5CF6",
    },
    "user_generated": {
        "label": "User-Generated",
        "emoji": "👥",
        "color": "#0D9488",
        "bg_color": "#F0FDFA",
        "border_color": "#14B8A6",
    },
}

# Weekly content rotation: indexes into a sequence of content types
# Designed to roughly follow 70-20-10 with BTS and UGC
WEEKLY_ROTATION = [
    "educational",
    "educational",
    "engaging",
    "educational",
    "promotional",
    "behind_the_scenes",
    "user_generated",
]

DAY_THEMES = {
    0: {"name": "Awareness", "desc": "Introduce the week's theme and educate"},
    1: {"name": "Deep Dive", "desc": "Go deeper — establish authority"},
    2: {"name": "Community", "desc": "Engage, share social proof, UGC"},
    3: {"name": "Value Bomb", "desc": "High-impact tips and insights"},
    4: {"name": "Promotion", "desc": "Soft pitch, showcase value"},
    5: {"name": "Behind-the-Scenes", "desc": "Authenticity and personality"},
    6: {"name": "Reflection", "desc": "Recap, inspire, set up next week"},
}

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ──────────────────────────────────────────────
# Hooks and CTAs by content type
# ──────────────────────────────────────────────

HOOKS = {
    "educational": [
        "Here's something most people get wrong about {topic}:",
        "Did you know that {topic} can transform your daily routine?",
        "The #1 mistake people make with {topic}:",
        "5 things you didn't know about {topic}:",
        "Let's talk about {topic} — and why it matters more than you think.",
        "Everyone talks about {topic}. But nobody mentions THIS:",
        "The truth about {topic} that experts won't tell you:",
        "Stop scrolling if you care about {topic}. Here's why:",
    ],
    "promotional": [
        "🚀 Exciting news from {brand}!",
        "Meet the {topic} solution you've been waiting for:",
        "What if {topic} could be 10x easier?",
        "{brand} just changed the game.",
        "Ready to level up your {topic} experience?",
        "Introducing the future of {topic} →",
        "Your {topic} journey starts here:",
        "We built {brand} for one reason: to make {topic} effortless.",
    ],
    "engaging": [
        "Hot take: {topic} is misunderstood. Agree or disagree?",
        "What's your biggest challenge with {topic}? 👇",
        "Quick question for the {topic} community:",
        "Unpopular opinion about {topic}:",
        "Let's settle this: what's the BEST approach to {topic}?",
        "If you could change ONE thing about {topic}, what would it be?",
        "Drop a 🔥 if you're passionate about {topic}",
        "What's your {topic} hot take? Reply and let's debate 👇",
    ],
    "behind_the_scenes": [
        "Ever wonder what goes on behind {brand}? 👀",
        "Behind every great {topic} is a story. Here's ours:",
        "A day in the life at {brand}:",
        "We get this question a lot: 'how does {brand} work?' Here's the answer:",
        "Real talk from the {brand} team:",
        "How we built {brand} from scratch — the untold story:",
        "This is what it really takes to build something in {topic}:",
        "Peek behind the curtain at {brand} 🎬",
    ],
    "user_generated": [
        "You spoke, we listened. Here's what the {brand} community is saying:",
        "Our community is INCREDIBLE. Here's proof:",
        "Real stories from real {brand} users 📣",
        "This review made our entire week:",
        "When we say {brand} changes lives, we mean it:",
        "The {brand} community never ceases to amaze us. Here's why:",
        "Your wins are our wins. Check this out:",
        "We love hearing from our {brand} family 💬",
    ],
}

CTAS = {
    "twitter": {
        "educational": ["Save this thread 📌", "Retweet to share the knowledge ♻️", "Follow for more {topic} insights 👀"],
        "promotional": ["Try it free → link in bio", "Learn more: link in bio 🔗", "Don't miss out → link in bio"],
        "engaging": ["Reply with your thoughts 👇", "RT if you agree ♻️", "What's your take? Comment below"],
        "behind_the_scenes": ["Follow our journey 👀", "Want more BTS? Follow us ✨", "What should we show next? Tell us 👇"],
        "user_generated": ["Join the conversation 💬", "Share your story — DM us!", "Tag someone who needs to see this 🙌"],
    },
    "instagram": {
        "educational": ["Save this for later 📌", "Share with someone who needs this 💛", "Double-tap if this helped!"],
        "promotional": ["Link in bio to learn more 🔗", "Tap the link in our bio →", "Don't wait — link in bio! ✨"],
        "engaging": ["Comment your thoughts below 👇", "Which do you agree with? Comment 1 or 2", "Tag a friend who needs to see this 🙌"],
        "behind_the_scenes": ["Follow for more BTS content ✨", "What should we show next? Comment! 👀", "Swipe to see more →"],
        "user_generated": ["Share your story and tag us!", "Use our hashtag to be featured 📸", "Join our community — link in bio"],
    },
    "linkedin": {
        "educational": ["What's your experience? Share below 👇", "Do you agree? Let's discuss.", "Follow for more insights on {topic}"],
        "promotional": ["Learn more: link in the comments below", "DM us to schedule a demo", "Visit our page to learn more"],
        "engaging": ["What's your take? I'd love to hear different perspectives.", "Comment your thoughts — let's start a conversation.", "Agree or disagree? Share your reasoning below."],
        "behind_the_scenes": ["Follow our company page for more updates", "What aspects of our journey interest you most?", "Connect with us to stay in the loop"],
        "user_generated": ["Are you using {brand}? We'd love to hear your story.", "Share your experience in the comments", "Follow our page for more customer stories"],
    },
}

HASHTAG_POOL = {
    "general": ["#trending", "#viral", "#content", "#community", "#inspiration", "#growth", "#tips", "#daily"],
    "twitter": ["#thread", "#tips", "#today"],
    "instagram": ["#instagood", "#instadaily", "#explore", "#reels", "#viral", "#trending", "#contentcreator", "#inspiration", "#instacommunity", "#explorepage", "#carrousel"],
    "linkedin": ["#leadership", "#innovation", "#strategy", "#growth", "#professional", "#industry", "#future", "#trends"],
}

# Image suggestion templates for Instagram
IMAGE_SUGGESTIONS = {
    "educational": [
        "Carousel post: {n} slides with key tips, bold text overlays, brand colors",
        "Infographic with key statistics about {topic}",
        "Before/after comparison graphic",
        "Step-by-step tutorial graphic with numbered steps",
    ],
    "promotional": [
        "Product hero shot with clean background and brand colors",
        "Lifestyle photo showing {brand} in use",
        "Promo graphic with offer text and CTA button",
        "Short demo video / Reel (15-30s)",
    ],
    "engaging": [
        "Bold text graphic with the question — high contrast, eye-catching",
        "This or That carousel with two options per slide",
        "Poll-style graphic with vote buttons overlay",
        "Eye-catching photo with text overlay question",
    ],
    "behind_the_scenes": [
        "Candid team photo or workspace shot",
        "Time-lapse video of your process (Reel)",
        "Before/after of a project or product being made",
        "Screenshot of real team conversation or whiteboard session",
    ],
    "user_generated": [
        "Repost a customer photo (with permission) in brand frame",
        "Collage of multiple customer testimonials",
        "Screenshot of a glowing review or DM",
        "User photo carousel — 5 happy customers",
    ],
}

# ──────────────────────────────────────────────
# Topic parsing
# ──────────────────────────────────────────────


def detect_brand(text):
    """Try to extract a brand name from a text snippet."""
    patterns = [
        r"called\s+([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+)?)",
        r"named\s+([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+)?)",
        r"brand\s+([A-Z][a-zA-Z0-9]+)",
        r"for\s+([A-Z][a-zA-Z0-9]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return m.group(1).strip()
    return None


def parse_input(text):
    """Parse a free-form input string into topic and brand."""
    text = text.strip().strip("\"'")
    brand = detect_brand(text)
    topic = text

    # Clean up: remove "called X" and "named X" from topic
    if brand:
        topic = re.sub(r"\s*(called|named)\s+" + re.escape(brand), "", topic, flags=re.IGNORECASE)
        topic = re.sub(r"\s*brand\s+" + re.escape(brand), "", topic, flags=re.IGNORECASE)

    # Clean up leading words
    topic = re.sub(r"^(an?|the)\s+", "", topic.strip(), flags=re.IGNORECASE).strip()
    if not topic:
        topic = brand or "your business"

    return topic, brand or topic


def slugify(text):
    """Convert text to a URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def topic_keywords(topic):
    """Extract keywords from topic for hashtag generation."""
    words = re.findall(r"[a-zA-Z]{3,}", topic.lower())
    stop = {"the", "and", "for", "with", "that", "this", "from", "your", "about", "called", "named", "brand", "app", "company", "business", "based"}
    return [w for w in words if w not in stop]


def generate_hashtags(topic, brand, platform, content_type):
    """Generate platform-appropriate hashtags."""
    kws = topic_keywords(topic)
    max_count = PLATFORMS[platform]["hashtag_max"]

    # Build topic-specific hashtags
    topic_tags = []
    if kws:
        # Multi-word: join
        joined = "".join(w.capitalize() for w in kws[:3])
        topic_tags.append("#" + joined)
    for kw in kws[:4]:
        topic_tags.append("#" + kw)

    # Brand tag
    brand_tag = "#" + slugify(brand).replace("-", "") if brand else ""

    # Platform-specific pool
    platform_pool = HASHTAG_POOL.get(platform, [])
    general_pool = HASHTAG_POOL["general"]

    # Content-type-specific tags
    type_tags_map = {
        "educational": ["#learn", "#education", "#knowledge", "#howto", "#guide"],
        "promotional": ["#new", "#launch", "#deal", "#offer", "#innovative"],
        "engaging": ["#discussion", "#community", "#opinion", "#debate"],
        "behind_the_scenes": ["#bts", "#behindthescenes", "#process", "#team"],
        "user_generated": ["#testimonial", "#review", "#community", "#repost"],
    }
    type_tags = type_tags_map.get(content_type, [])

    # Combine uniquely, respecting platform max
    all_tags = []
    seen = set()
    for tag_list in ([brand_tag], topic_tags, type_tags, platform_pool, general_pool):
        for tag in tag_list:
            t = tag.lower()
            if t not in seen and tag:
                seen.add(t)
                all_tags.append(tag)

    return all_tags[:max_count]


def generate_weekly_theme(topic, brand, start_date=None):
    """Generate a weekly theme/storyline."""
    kws = topic_keywords(topic)
    primary_kw = kws[0] if kws else topic
    themes = [
        f"The Future of {primary_kw.title()}",
        f"{brand} Week: Mastering {primary_kw.title()}",
        f"Level Up Your {primary_kw.title()}",
        f"The {primary_kw.title()} Revolution",
        f"Rethinking {primary_kw.title()}",
    ]
    # Pick deterministically based on topic hash
    idx = int(hashlib.md5(topic.encode()).hexdigest(), 16) % len(themes)
    theme = themes[idx]

    storyline = (
        f"This week at {brand}, we're exploring '{theme}'. "
        f"We'll start with foundational {primary_kw} knowledge, dive deep into strategies, "
        f"engage our community, drop high-value tips, showcase our latest offering, "
        f"go behind the scenes, and reflect on the journey. "
        f"Follow along — it's going to be an incredible week!"
    )
    return {"name": theme, "description": storyline}


# ──────────────────────────────────────────────
# Post generation per platform
# ──────────────────────────────────────────────


def pick(items, seed_str):
    """Deterministically pick an item from a list based on a seed string."""
    idx = int(hashlib.md5(seed_str.encode()).hexdigest(), 16) % len(items)
    return items[idx]


def generate_twitter_post(topic, brand, content_type, day_idx, post_idx, hashtags):
    """Generate a Twitter-optimized post (<=280 chars)."""
    hook_template = pick(HOOKS[content_type], f"{topic}-{content_type}-{day_idx}-{post_idx}")
    hook = hook_template.replace("{topic}", topic).replace("{brand}", brand)

    body_templates = {
        "educational": [
            f"\n\n• Start with the fundamentals\n• Practice consistently\n• Track your progress\n• Iterate and improve\n• Share what you learn",
            f"\n\n1. Focus on quality over quantity\n2. Build sustainable habits\n3. Learn from experts\n4. Embrace failure as feedback",
            f"\n\nThe key insight? Consistency beats intensity every time. Small daily actions compound into remarkable results.",
            f"\n\nMost people overcomplicate {topic}. The basics are simple:\n\n→ Clear goals\n→ Daily action\n→ Measure results\n→ Adjust",
        ],
        "promotional": [
            f"\n\n✨ {brand} is designed to make {topic} effortless.\n\n→ Smart features\n→ Beautiful design\n→ Real results\n\nSee for yourself:",
            f"\n\n{brand} helps you:\n✅ Save time\n✅ Get better results\n✅ Stay consistent\n\nReady to start?",
            f"\n\nStop struggling with {topic}. {brand} makes it simple.\n\n→ Try it today\n→ See results fast\n→ Join thousands of users",
        ],
        "engaging": [
            f"\n\nLet's hear it — what's working for you and what isn't?\n\nThe best answers get featured 🔥",
            f"\n\nDrop your thoughts below. No wrong answers 👇\n\nLet's learn from each other!",
            f"\n\nI genuinely want to know your perspective.\n\nWhat's been your experience?",
        ],
        "behind_the_scenes": [
            f"\n\nBuilding {brand} taught us:\n→ Start before you're ready\n→ Done > perfect\n→ Feedback is gold\n→ Team is everything",
            f"\n\nHere's what nobody tells you about building in {topic}:\n\nIt's 10% inspiration, 90% iteration.",
            f"\n\nLate nights. Hard decisions. Big bets.\n\nBut seeing users succeed makes it ALL worth it.",
        ],
        "user_generated": [
            f"\n\n'{brand} changed how I approach {topic}. I can't imagine going back.'\n\n— Real user feedback 💬",
            f"\n\nOur users are seeing REAL results:\n\n'It just works. I've never been more consistent.'\n\nJoin them →",
            f"\n\nNothing motivates us more than YOUR wins. Keep them coming! 🙌",
        ],
    }

    body = pick(body_templates[content_type], f"{topic}-{content_type}-body-{day_idx}-{post_idx}")
    cta_template = pick(CTAS["twitter"][content_type], f"{topic}-cta-{day_idx}-{post_idx}")
    cta = cta_template.replace("{topic}", topic).replace("{brand}", brand)

    tag_str = " ".join(hashtags[:2])
    post = f"{hook}{body}\n\n{cta} {tag_str}".strip()

    # Truncate if needed
    if len(post) > 280:
        post = post[:277] + "..."

    return post


def generate_instagram_post(topic, brand, content_type, day_idx, post_idx, hashtags):
    """Generate an Instagram-optimized post with caption and image suggestion."""
    hook_template = pick(HOOKS[content_type], f"{topic}-{content_type}-{day_idx}-{post_idx}")
    hook = hook_template.replace("{topic}", topic).replace("{brand}", brand)

    body_templates = {
        "educational": [
            f"\n\nLet's break it down simply:\n\n1️⃣ Start with why — know your motivation\n2️⃣ Build the foundation — master the basics\n3️⃣ Create systems — consistency over willpower\n4️⃣ Track progress — what gets measured improves\n5️⃣ Keep evolving — growth never stops\n\nThis isn't theory. This is the blueprint for {topic} success. 💪",
            f"\n\nHere are {n_tips()} truths about {topic} that change everything:\n\n→ Progress beats perfection\n→ Consistency creates momentum\n→ Small steps compound fast\n→ Community accelerates growth\n→ Mindset matters most\n\nWhich one resonates with you? 💭",
            f"\n\nThe {topic} approach nobody talks about:\n\nIt's not about doing MORE. It's about doing the RIGHT things consistently.\n\nQuality over quantity. Always.\n\nHere's how to put it into practice 👆",
        ],
        "promotional": [
            f"\n\nMeet {brand} — your new {topic} companion. ✨\n\nWhat makes us different?\n\n🌟 Designed with YOU in mind\n⚡ Effortless to use\n📈 Built for real results\n🤝 Backed by an amazing community\n\nReady to transform your {topic} experience?\n\nLink in bio to get started →",
            f"\n\n🚀 BIG NEWS from {brand}!\n\nWe've been working on something special — and it's finally here.\n\nImagine having everything you need for {topic} in one place. That's what we built.\n\nTap the link in our bio to see what's new ✨",
            f"\n\nWhat if {topic} could be... effortless?\n\nThat's what {brand} delivers.\n\n✅ Smart features that adapt to you\n✅ Beautiful, intuitive design\n✅ Real results, real fast\n\nYour journey starts at the link in bio 🔗",
        ],
        "engaging": [
            f"\n\nLet's settle this once and for all 👀\n\nWhen it comes to {topic}, what matters MORE?\n\n1️⃣ Consistency — showing up every day\n2️⃣ Intensity — going all in when you do\n\nDrop your answer in the comments. And tell us WHY! 👇",
            f"\n\nReal question for the {brand} community 💭\n\nWhat's the ONE piece of advice you'd give someone just starting with {topic}?\n\nWe'll feature our favorite answers in our stories! 📸",
            f"\n\nOkay, time for a hot take \U0001f525\n\nThe BEST approach to {topic} is the one you will actually stick with.\n\nNot the most popular. Not the most optimized. The one that works for YOU.\n\nAgree or disagree? Let us debate \U0001f447",
        ],
        "behind_the_scenes": [
            f"\n\nEver wonder what happens behind the scenes at {brand}? 👀\n\nHere's the truth: it's not always glamorous.\n\nLate nights 🌙 Countless iterations 🔄 Hard conversations 💬 Moments of doubt.\n\nBut every challenge makes us better. And seeing YOU succeed makes it all worth it.\n\nThis is our journey. Thanks for being part of it 💛",
            f"\n\nSWIPE to see how {brand} comes to life →\n\nFrom idea to reality, every step is intentional. We obsess over the details because YOU deserve the best.\n\nThis is what passion looks like behind the scenes 🎬",
            f"\n\nReal talk from the {brand} team:\n\nWe didn't start this because it was easy. We started it because {topic} deserved better.\n\nEvery late night, every tough decision, every breakthrough — it all leads here. To you.\n\nThank you for believing in us 🙏",
        ],
        "user_generated": [
            f"\n\nWE LOVE THIS SO MUCH 🥹\n\nA {brand} community member just shared their {topic} transformation and we are SO proud!\n\n'I never thought I could stay this consistent. {brand} made it feel effortless.'\n\nThis is why we do what we do. Thank you for trusting us! 💛\n\nShare YOUR story — DM us or use our hashtag!",
            f"\n\nYour wins = our wins 🙌\n\nWe just hit an incredible milestone, and it's all because of YOU.\n\nThe {brand} community is proof that when people come together around {topic}, amazing things happen.\n\nThank you for being part of this journey! Let's keep growing together 🚀",
            f"\n\nWhen we say {brand} works, we mean it.\n\nReal people. Real results. Real {topic} transformations.\n\nSwipe to see what our community is achieving →\n\nWant to be featured? Share your story and tag us! 📸",
        ],
    }

    body = pick(body_templates[content_type], f"{topic}-{content_type}-igbody-{day_idx}-{post_idx}")
    cta_template = pick(CTAS["instagram"][content_type], f"{topic}-igcta-{day_idx}-{post_idx}")
    cta = cta_template.replace("{topic}", topic).replace("{brand}", brand)

    tag_str = " ".join(hashtags)
    caption = f"{hook}{body}\n\n{cta}\n\n.\n.\n.\n{tag_str}".strip()

    # Image suggestion
    image_template = pick(IMAGE_SUGGESTIONS[content_type], f"{topic}-img-{content_type}-{day_idx}-{post_idx}")
    image_suggestion = image_template.replace("{topic}", topic).replace("{brand}", brand)
    # Replace {n} with number
    image_suggestion = image_suggestion.replace("{n}", str(pick([3, 5, 7], f"n-{day_idx}-{post_idx}")))

    return {"caption": caption, "image_suggestion": image_suggestion, "full": f"📷 Image: {image_suggestion}\n\n{caption}"}


def generate_linkedin_post(topic, brand, content_type, day_idx, post_idx, hashtags):
    """Generate a LinkedIn-optimized professional post (longer form)."""
    hook_template = pick(HOOKS[content_type], f"{topic}-{content_type}-{day_idx}-{post_idx}")
    hook = hook_template.replace("{topic}", topic).replace("{brand}", brand)

    body_templates = {
        "educational": [
            f"""
After years of studying {topic}, I've identified the patterns that separate those who succeed from those who don't.

It's not talent. It's not luck. It's strategy.

Here are the 5 principles that matter most:

1. START WITH THE PROBLEM, NOT THE SOLUTION
Most people jump straight into tactics. But if you don't understand the problem you're solving, you're just spinning your wheels. Clarity comes first.

2. BUILD SYSTEMS, NOT WILLPOWER
Willpower is finite. Systems are infinite. Design your environment so that doing the right thing is the easy thing.

3. MEASURE WHAT MATTERS
Vanity metrics are seductive but misleading. Focus on leading indicators — the actions that actually drive results.

4. EMBRACE THE COMPOUND EFFECT
Small improvements, made consistently, create extraordinary results over time. A 1% daily improvement compounds to 37x in a year.

5. LEARN IN PUBLIC
Share your journey. Teach what you learn. You'll attract opportunities, feedback, and a community that accelerates your growth.

These principles aren't complicated. But they're rarely practiced consistently.

Which one resonates most with your experience?""",
            f"""
I recently analyzed how the most successful people approach {topic}.

The findings surprised me.

It turns out, the biggest differentiator isn't resources, intelligence, or even experience.

It's MINDSET.

Here's what I mean:

The people who excel at {topic} share three key beliefs:

→ THEY VIEW FAILURE AS DATA
Every setback is feedback. Not a verdict.

→ THEY PRIORITIZE PROGRESS OVER PERFECTION
They ship imperfect work and iterate. Perfectionism is the enemy of momentum.

→ THEY INVEST IN RELATIONSHIPS
Success in {topic} — like everything else — is a team sport. The strongest networks are built on generosity, not transaction.

The best part? These beliefs can be developed intentionally.

What's one mindset shift that transformed how you approach {topic}?""",
        ],
        "promotional": [
            f"""
We built {brand} to solve a real problem.

For too long, {topic} has been needlessly complicated. Fragmented tools. Confusing processes. Steep learning curves.

We knew there had to be a better way.

That's why we created {brand} — a solution that makes {topic} simple, intuitive, and genuinely enjoyable.

Here's what makes it different:

✓ PURPOSE-BUILT DESIGN
Every feature exists for a reason. No bloat. No clutter.

✓ ADAPTIVE INTELLIGENCE
It learns from your behavior and adapts to your needs.

✓ COMMUNITY-DRIVEN
Built with input from real users, not just engineers in a vacuum.

The early results have been remarkable: users report higher consistency, better outcomes, and — most importantly — they actually enjoy the process.

If you're looking to transform how you approach {topic}, I'd love to show you what {brand} can do.

DM me or visit our page to learn more.""",
            f"""
Introducing a new way to think about {topic}.

At {brand}, we believe that {topic} shouldn't be a struggle. It should be seamless, intuitive, and even enjoyable.

Over the past year, our team has worked tirelessly to build something that lives up to that vision.

The result is a product that doesn't just meet expectations — it redefines them.

Key features:
→ Smart automation that saves hours each week
→ Beautiful, intuitive interface that anyone can use
→ Real-time insights that help you make better decisions
→ A thriving community of users supporting each other

We're just getting started. But the feedback so far has been incredible.

If {topic} matters to you, I think {brand} will too.

Check it out — link in the comments below.""",
        ],
        "engaging": [
            f"""
I have a question for my network:

What's the single biggest challenge you face with {topic}?

I've been researching this space extensively, and I keep finding the same themes:

→ Lack of clarity on where to start
→ Overwhelming number of options
→ Difficulty staying consistent
→ Measuring progress effectively

But I want to hear from YOU.

What's the obstacle that, if removed, would make the biggest difference in your {topic} journey?

Drop your answer below. I read every response and I'm genuinely curious about different perspectives.

Let's start a conversation.""",
            f"""
Unpopular opinion: Most advice about {topic} is wrong.

Not wrong in the "it's bad" sense. Wrong in the "it's incomplete" sense.

We're bombarded with tips, hacks, and frameworks. But most of them focus on tactics without addressing the foundation.

Here's what I think matters more than any tactic:

1. SELF-AWARENESS
Knowing what actually works for YOU — not what worked for someone else.

2. CONSISTENCY
Showing up regularly beats showing up intensely.

3. PATIENCE
Meaningful results take time. Period.

4. CURIOSITY
The best people I know in {topic} are endlessly curious. They never stop learning.

Agree or disagree? What would you add?

I'd love to hear your perspective — especially if you disagree.""",
        ],
        "behind_the_scenes": [
            f"""
Building {brand} has been the most challenging and rewarding experience of my career.

I want to share some lessons from the journey:

1. START BEFORE YOU'RE READY
We launched {brand} when it was 60% done. Not 100%. And that was the right call. Perfection is the enemy of impact.

2. FEEDBACK IS A GIFT
The hardest conversations led to the best improvements. We learned to crave criticism, not avoid it.

3. CULTURE IS STRATEGY
How your team works together matters more than any individual decision. We invest heavily in culture.

4. MISSION DRIVES EVERYTHING
When things get hard — and they will — a clear mission is what keeps you going.

Building something meaningful in {topic} is hard. But it's also the most fulfilling work I've ever done.

To anyone building something: keep going. The world needs what you're creating.""",
            f"""
People often ask me: "What does a typical day look like at {brand}?"

Here's the honest answer: there's no such thing as typical.

But there ARE constants:

→ We start every day with a team standup. Alignment is everything.
→ We spend 20% of our time talking to users. Their feedback shapes our roadmap.
→ We make decisions quickly. Speed is a competitive advantage.
→ We celebrate small wins. Momentum builds on momentum.

Building a company in {topic} is messy, unpredictable, and occasionally terrifying.

But I wouldn't trade it for anything.

What aspects of building a company interest you most? Happy to share more.""",
        ],
        "user_generated": [
            f"""
The best part of building {brand} isn't the product launches or the metrics.

It's the messages from users.

Last week, we received this note:

"I've been using {brand} for three months. In that time, I've made more progress with {topic} than I did in the previous two years combined. I feel like a different person."

That's why we do this.

Every late night. Every hard decision. Every iteration.

It's all worth it when we see real people achieving real results.

To everyone in the {brand} community: thank you for trusting us. Your success is our success.

And to anyone considering starting their {topic} journey: there's no better time than now.

Are you working on {topic}? I'd love to hear about your experience.""",
            f"""
Our community never ceases to amaze me.

Since launching {brand}, we've seen users achieve things that exceed our wildest expectations:

→ Professionals who doubled their consistency in 30 days
→ Beginners who went from confused to confident in weeks
→ Teams that transformed how they approach {topic} together

But the numbers only tell part of the story. Behind every data point is a person who decided to try something new — and stuck with it.

That takes courage.

If you're using {brand}, I'd love to hear your story. What's changed for you since you started?

And if you're on the fence: the community is here to support you. You don't have to do it alone.""",
        ],
    }

    body = pick(body_templates[content_type], f"{topic}-{content_type}-libody-{day_idx}-{post_idx}")
    cta_template = pick(CTAS["linkedin"][content_type], f"{topic}-lictia-{day_idx}-{post_idx}")
    cta = cta_template.replace("{topic}", topic).replace("{brand}", brand)

    tag_str = " ".join(hashtags[:5])
    post = f"{hook}\n{body}\n\n{cta}\n\n{tag_str}".strip()

    return post


def n_tips():
    return "5"


# ──────────────────────────────────────────────
# Week generation
# ──────────────────────────────────────────────


def generate_content_calendar(topic, brand=None, days=7, platform_list=None, start_date=None):
    """Generate a full content calendar."""
    if platform_list is None:
        platform_list = ["twitter", "instagram", "linkedin"]

    if brand is None:
        brand = topic

    if start_date is None:
        start_date = datetime.now()

    weekly_theme = generate_weekly_theme(topic, brand, start_date)

    posts = []
    for day_idx in range(days):
        date = start_date + timedelta(days=day_idx)
        day_of_week = date.weekday()  # 0=Monday
        day_name = DAYS_OF_WEEK[day_of_week]

        # Content type rotation
        content_type = WEEKLY_ROTATION[day_of_week]
        day_theme = DAY_THEMES[day_of_week]

        for platform in platform_list:
            post_idx = day_idx * len(platform_list) + platform_list.index(platform)

            hashtags = generate_hashtags(topic, brand, platform, content_type)
            best_time = pick(PLATFORMS[platform]["best_times"], f"{platform}-{day_idx}")

            post_data = {
                "id": f"post-{day_idx+1}-{platform}",
                "day": day_idx + 1,
                "day_name": day_name,
                "date": date.strftime("%Y-%m-%d"),
                "platform": platform,
                "platform_label": PLATFORMS[platform]["label"],
                "content_type": content_type,
                "content_type_label": CONTENT_TYPES[content_type]["label"],
                "content_type_emoji": CONTENT_TYPES[content_type]["emoji"],
                "best_time": best_time,
                "hashtags": hashtags,
                "week_theme": weekly_theme["name"],
            }

            if platform == "twitter":
                post_data["content"] = generate_twitter_post(topic, brand, content_type, day_idx, post_idx, hashtags)
                post_data["char_count"] = len(post_data["content"])
                post_data["char_limit"] = 280
            elif platform == "instagram":
                ig = generate_instagram_post(topic, brand, content_type, day_idx, post_idx, hashtags)
                post_data["content"] = ig["caption"]
                post_data["image_suggestion"] = ig["image_suggestion"]
                post_data["char_count"] = len(post_data["content"])
                post_data["char_limit"] = 2200
            elif platform == "linkedin":
                post_data["content"] = generate_linkedin_post(topic, brand, content_type, day_idx, post_idx, hashtags)
                post_data["char_count"] = len(post_data["content"])
                post_data["char_limit"] = 3000

            posts.append(post_data)

    calendar = {
        "metadata": {
            "topic": topic,
            "brand": brand,
            "days": days,
            "platforms": platform_list,
            "total_posts": len(posts),
            "week_theme": weekly_theme["name"],
            "week_storyline": weekly_theme["description"],
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "start_date": start_date.strftime("%Y-%m-%d"),
            "version": VERSION,
        },
        "weekly_theme": weekly_theme,
        "posts": posts,
    }

    return calendar


# ──────────────────────────────────────────────
# HTML Calendar Generation
# ──────────────────────────────────────────────


def generate_html_calendar(calendar_data, output_path=None):
    """Generate a beautiful HTML content calendar from calendar data."""
    meta = calendar_data["metadata"]
    posts = calendar_data["posts"]
    theme = calendar_data["weekly_theme"]

    # Group posts by day and platform
    grid = {}
    for post in posts:
        day = post["day"]
        platform = post["platform"]
        if day not in grid:
            grid[day] = {}
        grid[day][platform] = post

    # Determine number of days and platforms
    num_days = meta["days"]
    platforms = meta["platforms"]

    # Build cards HTML
    cards_html = ""
    for day_idx in range(1, num_days + 1):
        date_str = ""
        day_name = ""
        for post in posts:
            if post["day"] == day_idx:
                date_str = post["date"]
                day_name = post["day_name"]
                break

        for platform in platforms:
            post = grid.get(day_idx, {}).get(platform)
            if post:
                cards_html += _build_post_card(post) + "\n"
            else:
                cards_html += '<div class="card empty-card"><span class="no-post">—</span></div>\n'

    # Stats
    type_counts = {}
    for post in posts:
        ct = post["content_type"]
        type_counts[ct] = type_counts.get(ct, 0) + 1

    stats_html = ""
    for ct_key, ct_data in CONTENT_TYPES.items():
        count = type_counts.get(ct_key, 0)
        if count > 0:
            pct = (count / len(posts) * 100) if posts else 0
            stats_html += f"""
                <div class="stat-item" style="border-left: 4px solid {ct_data['border_color']};">
                    <span class="stat-emoji">{ct_data['emoji']}</span>
                    <span class="stat-label">{ct_data['label']}</span>
                    <span class="stat-count">{count}</span>
                    <span class="stat-pct">{pct:.0f}%</span>
                </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta['brand']} — Social Media Content Calendar</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #1a1a2e;
        }}

        .container {{
            max-width: 1600px;
            margin: 0 auto;
        }}

        /* ─── Header ─── */
        .header {{
            background: white;
            border-radius: 20px;
            padding: 30px 40px;
            margin-bottom: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        }}

        .header h1 {{
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }}

        .header .brand {{
            font-size: 36px;
            font-weight: 900;
            color: #1a1a2e;
            margin-bottom: 4px;
        }}

        .header .topic {{
            font-size: 16px;
            color: #666;
            margin-bottom: 16px;
        }}

        .header .theme-badge {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 12px;
        }}

        .header .storyline {{
            font-size: 14px;
            line-height: 1.6;
            color: #555;
            max-width: 800px;
        }}

        .header .meta-row {{
            display: flex;
            gap: 30px;
            margin-top: 16px;
            flex-wrap: wrap;
        }}

        .header .meta-item {{
            font-size: 13px;
            color: #888;
        }}

        .header .meta-item strong {{
            color: #333;
        }}

        /* ─── Stats Bar ─── */
        .stats {{
            background: white;
            border-radius: 16px;
            padding: 20px 30px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            justify-content: space-between;
        }}

        .stats-title {{
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #999;
            width: 100%;
            margin-bottom: 8px;
        }}

        .stat-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 16px;
            border-radius: 10px;
            background: #f8f9fa;
            flex: 1;
            min-width: 150px;
        }}

        .stat-emoji {{ font-size: 18px; }}
        .stat-label {{ font-size: 13px; font-weight: 600; color: #555; }}
        .stat-count {{ font-size: 20px; font-weight: 800; color: #1a1a2e; margin-left: auto; }}
        .stat-pct {{ font-size: 12px; color: #999; }}

        /* ─── Calendar Grid ─── */
        .calendar {{
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            overflow-x: auto;
        }}

        .calendar-title {{
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 20px;
            color: #1a1a2e;
        }}

        .grid {{
            display: grid;
            grid-template-columns: repeat({num_days}, minmax(200px, 1fr));
            gap: 16px;
        }}

        /* ─── Platform Rows ─── */
        .platform-section {{
            margin-bottom: 24px;
        }}

        .platform-label {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
            padding: 8px 16px;
            border-radius: 8px;
            display: inline-block;
        }}

        /* ─── Cards ─── */
        .card {{
            border-radius: 12px;
            padding: 16px;
            min-height: 200px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            transition: transform 0.2s, box-shadow 0.2s;
            border-top: 4px solid #ddd;
            position: relative;
        }}

        .card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.12);
        }}

        .card.empty-card {{
            background: #f9f9f9;
            border: 2px dashed #eee;
            justify-content: center;
            align-items: center;
        }}

        .no-post {{
            color: #ccc;
            font-size: 24px;
        }}

        .card-day {{
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #999;
        }}

        .card-date {{
            font-size: 11px;
            color: #bbb;
        }}

        .card-type {{
            display: inline-block;
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding: 3px 10px;
            border-radius: 50px;
            color: white;
            align-self: flex-start;
        }}

        .card-content {{
            font-size: 12px;
            line-height: 1.5;
            color: #444;
            max-height: 120px;
            overflow: hidden;
            position: relative;
        }}

        .card-content::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 30px;
            background: linear-gradient(transparent, white);
        }}

        .card-hashtags {{
            font-size: 10px;
            color: #888;
            line-height: 1.4;
            word-break: break-word;
        }}

        .card-time {{
            font-size: 11px;
            color: #aaa;
            display: flex;
            align-items: center;
            gap: 4px;
            margin-top: auto;
        }}

        .card-charcount {{
            font-size: 10px;
            color: #ccc;
        }}

        /* ─── Footer ─── */
        .footer {{
            text-align: center;
            padding: 20px;
            color: rgba(255,255,255,0.8);
            font-size: 13px;
        }}

        .footer a {{
            color: white;
            text-decoration: none;
            font-weight: 600;
        }}

        /* ─── Print ─── */
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .header, .calendar, .stats {{
                box-shadow: none;
                border-radius: 0;
                border-bottom: 1px solid #ddd;
            }}
            .card {{
                min-height: auto;
                border: 1px solid #ddd;
                border-radius: 8px;
                page-break-inside: avoid;
            }}
            .card:hover {{
                transform: none;
                box-shadow: none;
            }}
            .card-content {{
                max-height: none;
            }}
            .card-content::after {{
                display: none;
            }}
        }}

        /* ─── Responsive ─── */
        @media (max-width: 768px) {{
            .grid {{
                grid-template-columns: 1fr;
            }}
            .stats {{
                flex-direction: column;
            }}
        }}

        /* Content type badge colors */
        .type-educational {{ background: {CONTENT_TYPES['educational']['color']} !important; }}
        .type-promotional {{ background: {CONTENT_TYPES['promotional']['color']} !important; }}
        .type-engaging {{ background: {CONTENT_TYPES['engaging']['color']} !important; }}
        .type-behind_the_scenes {{ background: {CONTENT_TYPES['behind_the_scenes']['color']} !important; }}
        .type-user_generated {{ background: {CONTENT_TYPES['user_generated']['color']} !important; }}

        /* Card backgrounds */
        .bg-educational {{ background: {CONTENT_TYPES['educational']['bg_color']}; border-top-color: {CONTENT_TYPES['educational']['border_color']}; }}
        .bg-promotional {{ background: {CONTENT_TYPES['promotional']['bg_color']}; border-top-color: {CONTENT_TYPES['promotional']['border_color']}; }}
        .bg-engaging {{ background: {CONTENT_TYPES['engaging']['bg_color']}; border-top-color: {CONTENT_TYPES['engaging']['border_color']}; }}
        .bg-behind_the_scenes {{ background: {CONTENT_TYPES['behind_the_scenes']['bg_color']}; border-top-color: {CONTENT_TYPES['behind_the_scenes']['border_color']}; }}
        .bg-user_generated {{ background: {CONTENT_TYPES['user_generated']['bg_color']}; border-top-color: {CONTENT_TYPES['user_generated']['border_color']}; }}

        /* Platform label colors */
        .plat-twitter {{ background: {PLATFORMS['twitter']['bg_color']}; color: {PLATFORMS['twitter']['color']}; }}
        .plat-instagram {{ background: {PLATFORMS['instagram']['bg_color']}; color: {PLATFORMS['instagram']['color']}; }}
        .plat-linkedin {{ background: {PLATFORMS['linkedin']['bg_color']}; color: {PLATFORMS['linkedin']['color']}; }}

    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>📱 Social Media Content Calendar</h1>
            <div class="brand">{_esc(meta['brand'])}</div>
            <div class="topic">Topic: {_esc(meta['topic'])} · {meta['total_posts']} posts · {meta['days']} days · {', '.join(p.title() for p in platforms)}</div>
            <div class="theme-badge">🎯 {theme['name']}</div>
            <div class="storyline">{_esc(theme['description'])}</div>
            <div class="meta-row">
                <span class="meta-item"><strong>📅 Start:</strong> {meta['start_date']}</span>
                <span class="meta-item"><strong>🔄 Generated:</strong> {meta['generated_at']}</span>
                <span class="meta-item"><strong>📦 Version:</strong> {meta['version']}</span>
            </div>
        </div>

        <!-- Stats -->
        <div class="stats">
            <div class="stats-title">Content Mix Breakdown</div>
            {stats_html}
        </div>

        <!-- Calendar Grid -->
        <div class="calendar">
            <div class="calendar-title">📋 Weekly Content Grid</div>
"""

    # Build grid per platform
    for platform in platforms:
        plat = PLATFORMS[platform]
        html += f"""
            <div class="platform-section">
                <span class="platform-label plat-{platform}">{plat['icon_emoji']} {plat['label']}</span>
                <div class="grid">
"""
        for day_idx in range(1, num_days + 1):
            post = grid.get(day_idx, {}).get(platform)
            if post:
                html += _build_post_card(post) + "\n"
            else:
                html += '                    <div class="card empty-card"><span class="no-post">—</span></div>\n'

        html += """                </div>
            </div>"""

    html += f"""
        </div>

        <div class="footer">
            Generated by <strong>Social Media Kit v{VERSION}</strong> · MIT License · Denis Voronin<br>
            📱 Export <code>content.json</code> for scheduling tools · 🖨️ Print-friendly layout
        </div>
    </div>
</body>
</html>"""

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

    return html


def _esc(text):
    """HTML-escape text."""
    if not text:
        return ""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def _build_post_card(post):
    """Build an HTML card for a single post."""
    ct = post["content_type"]
    platform = post["platform"]

    # Truncate content for preview
    content = post.get("content", "")
    preview = content[:300]
    if len(content) > 300:
        preview += "..."

    hashtags = " ".join(post.get("hashtags", []))

    image_html = ""
    if post.get("image_suggestion"):
        image_html = f'<div class="card-hashtags">📷 {_esc(post["image_suggestion"])}</div>'

    return f"""                    <div class="card bg-{ct}">
                        <div class="card-day">{_esc(post['day_name'])} · Day {post['day']}</div>
                        <div class="card-date">{_esc(post['date'])} · ⏰ {_esc(post['best_time'])}</div>
                        <span class="card-type type-{ct}">{post['content_type_emoji']} {post['content_type_label']}</span>
                        <div class="card-content">{_esc(preview)}</div>
                        {image_html}
                        <div class="card-hashtags">{_esc(hashtags)}</div>
                        <div class="card-charcount">{post.get('char_count', '?')} / {post.get('char_limit', '?')} chars</div>
                    </div>"""


# ──────────────────────────────────────────────
# Console Summary
# ──────────────────────────────────────────────


def print_summary(calendar_data):
    """Print a console summary of the content calendar."""
    meta = calendar_data["metadata"]
    theme = calendar_data["weekly_theme"]
    posts = calendar_data["posts"]

    print()
    print("=" * 70)
    print(f"  📱 SOCIAL MEDIA KIT — CONTENT CALENDAR")
    print("=" * 70)
    print(f"  Brand:   {meta['brand']}")
    print(f"  Topic:   {meta['topic']}")
    print(f"  Theme:   🎯 {theme['name']}")
    print(f"  Posts:   {meta['total_posts']} ({meta['days']} days × {len(meta['platforms'])} platforms)")
    print(f"  Start:   {meta['start_date']}")
    print()
    print("  " + "-" * 66)
    print("  📅 WEEKLY OVERVIEW")
    print("  " + "-" * 66)

    for day_idx in range(1, meta["days"] + 1):
        day_posts = [p for p in posts if p["day"] == day_idx]
        if not day_posts:
            continue
        day_name = day_posts[0]["day_name"]
        date = day_posts[0]["date"]
        day_theme = DAY_THEMES[(day_idx - 1) % 7]
        print()
        print(f"  📆 {day_name} ({date}) — {day_theme['name']}")
        print(f"     {day_theme['desc']}")
        for post in day_posts:
            ct_emoji = post["content_type_emoji"]
            print(f"     {ct_emoji} {post['platform_label']:12s} | ⏰ {post['best_time']:8s} | {post['content_type_label']}")

    print()
    print("  " + "-" * 66)
    print("  📊 CONTENT MIX")
    print("  " + "-" * 66)

    type_counts = {}
    for post in posts:
        ct = post["content_type"]
        type_counts[ct] = type_counts.get(ct, 0) + 1

    for ct_key, ct_data in CONTENT_TYPES.items():
        count = type_counts.get(ct_key, 0)
        if count > 0:
            pct = count / len(posts) * 100
            bar = "█" * int(pct / 3) + "░" * (33 - int(pct / 3))
            print(f"  {ct_data['emoji']} {ct_data['label']:20s} {bar} {count:3d} ({pct:.0f}%)")

    print()
    print("=" * 70)
    print("  ✅ Output: content.json + calendar.html")
    print("  📦 Ready for scheduling tools (Buffer, Hootsuite, Later)")
    print("=" * 70)
    print()


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────


def cmd_generate(args):
    """Generate content calendar."""
    topic = args.topic
    brand = args.brand if args.brand else topic
    days = args.days
    platforms = args.platforms.split(",") if args.platforms else ["twitter", "instagram", "linkedin"]
    platforms = [p.strip().lower() for p in platforms]

    # Validate platforms
    for p in platforms:
        if p not in PLATFORMS:
            print(f"Error: Unknown platform '{p}'. Choose from: {', '.join(PLATFORMS.keys())}", file=sys.stderr)
            sys.exit(1)

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n🎨 Generating {days} days × {len(platforms)} platforms = {days * len(platforms)} posts...")
    print(f"   Topic: {topic}")
    print(f"   Brand: {brand}")
    print(f"   Platforms: {', '.join(platforms)}\n")

    calendar_data = generate_content_calendar(topic, brand, days, platforms)

    # Write JSON
    json_path = os.path.join(output_dir, "content.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(calendar_data, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved: {json_path}")

    # Write HTML
    html_path = os.path.join(output_dir, "calendar.html")
    generate_html_calendar(calendar_data, html_path)
    print(f"✅ Saved: {html_path}")

    # Print summary
    print_summary(calendar_data)

    return calendar_data


def cmd_calendar(args):
    """Build HTML calendar from JSON file."""
    json_path = args.json_path
    output_path = args.output

    if not os.path.exists(json_path):
        print(f"Error: File not found: {json_path}", file=sys.stderr)
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        calendar_data = json.load(f)

    generate_html_calendar(calendar_data, output_path)
    print(f"\n✅ HTML calendar saved to: {output_path}\n")


def cmd_auto(args):
    """Auto-detect topic from stdin."""
    if sys.stdin.isatty():
        print("Error: --auto requires input via stdin.", file=sys.stderr)
        print('Example: echo "organic coffee in Brooklyn" | python social_kit.py --auto', file=sys.stderr)
        sys.exit(1)

    text = sys.stdin.read().strip()
    if not text:
        print("Error: No input received on stdin.", file=sys.stderr)
        sys.exit(1)

    topic, brand = parse_input(text)
    print(f"\n🔍 Auto-detected:")
    print(f"   Topic: {topic}")
    print(f"   Brand: {brand}\n")

    # Generate as if called with generate
    args = argparse.Namespace(
        topic=topic,
        brand=brand,
        days=7,
        platforms="twitter,instagram,linkedin",
        output_dir="./output",
    )
    return cmd_generate(args)


def main():
    parser = argparse.ArgumentParser(
        prog="social_kit",
        description="📱 Social Media Kit — Generate a complete week of social media content",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python social_kit.py generate --topic 'sustainable fashion' --brand 'EcoThreads'
  python social_kit.py generate --topic 'AI productivity' --days 14 --platforms twitter,linkedin
  python social_kit.py calendar content.json --output calendar.html
  echo 'organic coffee roastery in Brooklyn' | python social_kit.py --auto
        """,
    )
    parser.add_argument("--version", action="version", version=f"Social Media Kit v{VERSION}")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # generate subcommand
    gen = subparsers.add_parser("generate", help="Generate content calendar")
    gen.add_argument("--topic", "-t", required=True, help="Topic, niche, or description")
    gen.add_argument("--brand", "-b", default=None, help="Brand or product name (defaults to topic)")
    gen.add_argument("--days", "-d", type=int, default=7, help="Number of days (default: 7)")
    gen.add_argument("--platforms", "-p", default="twitter,instagram,linkedin", help="Comma-separated platforms")
    gen.add_argument("--output-dir", "-o", default="./output", help="Output directory (default: ./output)")
    gen.set_defaults(func=cmd_generate)

    # calendar subcommand
    cal = subparsers.add_parser("calendar", help="Build HTML calendar from JSON")
    cal.add_argument("json_path", help="Path to content.json")
    cal.add_argument("--output", "-o", default="calendar.html", help="Output HTML path")
    cal.set_defaults(func=cmd_calendar)

    # --auto flag (stdin)
    parser.add_argument("--auto", action="store_true", help="Auto-detect topic from stdin")

    args = parser.parse_args()

    if args.auto:
        return cmd_auto(args)

    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
