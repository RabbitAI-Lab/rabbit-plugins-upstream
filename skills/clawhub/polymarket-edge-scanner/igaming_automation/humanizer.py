#!/usr/bin/env python3
"""Humanizer pass: strips AI writing tells from content before it goes public.

Implements the super-humanizer skill rules as a fixed pipeline step, so every
article, review, refresh, and link edit reads like a person wrote it.
"""

import re

from config import HUMANIZER_ENABLED
from llm_client import chat

HUMANIZER_SYSTEM_PROMPT = """You are an expert editor for a South African iGaming site. You rewrite AI-sounding text so it reads like a knowledgeable human wrote it.

Hard rules:
- No em dashes anywhere. Replace them with commas, periods, or parentheses.
- 9th grade reading level. Short, clear sentences. Plain words first.
- European date format (14/06/2026) if dates appear.
- Vary sentence rhythm. Mix short punchy lines with longer ones. AI writes every sentence at the same length; do not.
- Cut AI vocabulary: delve, landscape (figurative), seamless, robust, cutting-edge, leverage (verb), navigate (figurative), realm, myriad, plethora, foster, underscore, showcase, testament, pivotal, vibrant, nestled, journey, tapestry, elevate, unlock, unleash, groundbreaking.
- Cut filler transitions: Moreover, Furthermore, Additionally, In conclusion, That said, It's worth noting, When it comes to.
- Cut promo puffery: world-class, state-of-the-art, best-in-class, stands out, takes X to the next level, exciting times.
- Cut generic positive endings like "The future looks bright". End on a specific fact or just stop.
- Prefer plain verbs: "is" and "has" over "serves as", "stands as", "boasts", "features".
- Keep contractions natural (it's, you'll, they're).

Never change:
- Facts, numbers, bonus terms, wagering requirements, operator names, dates, or legal/compliance wording.
- HTML tags or structure. Keep every tag exactly as-is, including <blockquote class="key-takeaways">.
- URLs and href attributes. Internal links stay intact.
- Heading hierarchy.

Return ONLY the rewritten HTML. No preamble, no commentary, no markdown code fences."""


def _strip_fences(text: str) -> str:
    """Remove markdown code fences if the model added them."""
    stripped = re.sub(r"^```(?:html)?\s*|\s*```$", "", text.strip())
    return stripped


def _em_dash_safety_net(text: str) -> str:
    """Replace any em dashes the model missed."""
    return text.replace(" — ", ", ").replace("—", ", ")


def humanize_html(content: str) -> str:
    """Run the humanizer pass over HTML content. No-op if disabled or empty."""
    if not HUMANIZER_ENABLED or not content or not content.strip():
        return content

    original_len = len(content)
    messages = [
        {"role": "system", "content": HUMANIZER_SYSTEM_PROMPT},
        {"role": "user", "content": f"Rewrite this article HTML so it reads human. Keep all rules.\n\n{content}"},
    ]
    rewritten = chat(messages, temperature=0.3, max_tokens=8000)
    rewritten = _strip_fences(rewritten)
    rewritten = _em_dash_safety_net(rewritten)

    # Guard: if the model returned something far shorter, it likely cut content. Keep the original.
    if len(rewritten) < original_len * 0.6:
        print("Humanizer guard: output too short, keeping original content.")
        return content

    return rewritten
