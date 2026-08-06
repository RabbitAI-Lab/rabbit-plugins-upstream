#!/usr/bin/env python3
"""
Flashcard Forge — Text → Flashcards
====================================

Convert any text (PDF excerpts, lecture notes, articles, textbook chapters)
into Anki-importable flashcards using regex-based extraction and sentence
analysis. Supports Q&A and cloze-deletion modes.

Usage:
    python3 flashcard_forge.py <input.txt>                           # auto mode → stdout
    python3 flashcard_forge.py notes.txt -o deck.csv                 # Q&A → CSV
    python3 flashcard_forge.py notes.txt --mode cloze -o cloze.csv   # cloze → CSV
    python3 flashcard_forge.py notes.txt --mode auto --format json -o deck.json
    python3 flashcard_forge.py --help

Output formats:
    csv  (default) — Anki-importable semicolon-separated CSV
    json           — JSON array of {front, back, type, source} objects

No third-party dependencies. Python 3.8+ stdlib only.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Card:
    """A single flashcard."""
    front: str
    back: str
    card_type: str  # "qa" or "cloze"
    source: str = ""  # the sentence it was extracted from

    def to_dict(self) -> dict:
        return {
            "front": self.front,
            "back": self.back,
            "type": self.card_type,
            "source": self.source,
        }


# ---------------------------------------------------------------------------
# Text processing
# ---------------------------------------------------------------------------

def clean_text(text: str) -> str:
    """Normalize whitespace and strip common markdown artifacts."""
    # Remove markdown headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r'\*{1,2}(.+?)\*{1,2}', r'\1', text)
    text = re.sub(r'_{1,2}(.+?)_{1,2}', r'\1', text)
    # Remove inline code backticks
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Normalize whitespace
    text = re.sub(r'\r\n', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def split_sentences(text: str) -> List[str]:
    """Split text into sentences using punctuation-aware tokenization."""
    # Protect common abbreviations from being split
    abbreviations = {
        'mr', 'mrs', 'ms', 'dr', 'prof', 'sr', 'jr', 'st',
        'vs', 'etc', 'e.g', 'i.e', 'fig', 'no', 'vol',
        'inc', 'ltd', 'co', 'corp',
    }
    for abbr in abbreviations:
        text = re.sub(
            rf'\b{abbr}\.',
            f'{abbr}<DOT>',
            text,
            flags=re.IGNORECASE,
        )

    # Split on sentence-ending punctuation followed by space + capital
    raw = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"])', text)

    sentences: List[str] = []
    for s in raw:
        s = s.replace('<DOT>', '.').strip()
        if s and len(s) > 1:
            sentences.append(s)
    return sentences


# ---------------------------------------------------------------------------
# Extraction patterns
# ---------------------------------------------------------------------------

# --- Definition patterns ---

P_DEF_IS_A = re.compile(
    r'\b([A-Z][\w\s]{2,40}?)\s+is\s+(?:a|an|the)\s+(.{5,120}?)[.]',
    re.IGNORECASE,
)

P_DEF_DEFINED_AS = re.compile(
    r'\b(.{2,50}?)\s+is\s+defined\s+as\s+(.{5,120}?)[.]',
    re.IGNORECASE,
)

P_DEF_REFERS_TO = re.compile(
    r'\b(.{2,50}?)\s+(?:refers\s+to|means)\s+(.{5,120}?)[.]',
    re.IGNORECASE,
)

P_DEF_COLON = re.compile(
    r'^([A-Z][^:]{2,40}):\s+(.{5,120}?)[.]?$',
    re.MULTILINE,
)

P_STANDS_FOR = re.compile(
    r'\b([A-Z]{2,6})\s+stands\s+for\s+(.{3,100}?)[.]',
)

# --- Q&A patterns ---

P_EXPLICIT_QUESTION = re.compile(
    r'(What|Why|How|When|Where|Who|Which)\s+(.{2,80}?)\?\s*(.{3,120}?)[.]?',
    re.IGNORECASE,
)

# --- List patterns ---

P_THERE_ARE_TYPES = re.compile(
    r'\bThere\s+are\s+(\w+)\s+(?:types|kinds|categories|forms|phases|stages)\s+of\s+(.{2,60}?):\s*(.{10,200}?)[.]',
    re.IGNORECASE,
)

# --- Cause / effect patterns ---

P_CAUSE_EFFECT = re.compile(
    r'\b(.{3,60}?)\s+(?:causes|leads\s+to|results\s+in|produces|triggers)\s+(.{3,100}?)[.]',
    re.IGNORECASE,
)

# --- Comparison patterns ---

P_COMPARISON = re.compile(
    r'\b(?:Unlike|Whereas)\s+(.{3,60}?),\s+(.{3,60}?)\s+(.{5,100}?)[.]',
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

def extract_definitions(sentences: List[str]) -> List[Card]:
    """Extract definition-style Q&A cards."""
    cards: List[Card] = []

    for sent in sentences:
        # "X is defined as Y"
        for m in P_DEF_DEFINED_AS.finditer(sent):
            term = m.group(1).strip().capitalize()
            definition = m.group(2).strip().rstrip('.')
            if len(term) > 2 and len(definition) > 5:
                cards.append(Card(
                    front=term,
                    back=definition,
                    card_type="qa",
                    source=sent,
                ))

        # "X is a/the Y"
        for m in P_DEF_IS_A.finditer(sent):
            term = m.group(1).strip().capitalize()
            definition = m.group(2).strip().rstrip('.')
            # Filter out pronouns and trivial terms
            if term.lower() in ('this', 'that', 'it', 'there', 'here', 'he', 'she', 'they'):
                continue
            if len(term) > 2 and len(definition) > 5:
                cards.append(Card(
                    front=f"What is {term}?",
                    back=definition,
                    card_type="qa",
                    source=sent,
                ))

        # "X refers to Y" / "X means Y"
        for m in P_DEF_REFERS_TO.finditer(sent):
            term = m.group(1).strip().capitalize()
            definition = m.group(2).strip().rstrip('.')
            if len(term) > 2 and len(definition) > 5:
                cards.append(Card(
                    front=term,
                    back=definition,
                    card_type="qa",
                    source=sent,
                ))

        # "X stands for Y"
        for m in P_STANDS_FOR.finditer(sent):
            acronym = m.group(1).strip()
            expansion = m.group(2).strip().rstrip('.')
            cards.append(Card(
                front=f"What does {acronym} stand for?",
                back=expansion,
                card_type="qa",
                source=sent,
            ))

    # Colon definitions (multiline scan over full text)
    return cards


def extract_colon_definitions(text: str) -> List[Card]:
    cards: List[Card] = []
    for m in P_DEF_COLON.finditer(text):
        term = m.group(1).strip()
        definition = m.group(2).strip().rstrip('.')
        if len(term) > 2 and len(definition) > 5:
            cards.append(Card(
                front=term,
                back=definition,
                card_type="qa",
                source=m.group(0).strip(),
            ))
    return cards


def extract_qa(sentences: List[str]) -> List[Card]:
    """Extract explicit question-answer pairs."""
    cards: List[Card] = []
    for sent in sentences:
        for m in P_EXPLICIT_QUESTION.finditer(sent):
            q_word = m.group(1)
            q_rest = m.group(2).strip()
            answer = m.group(3).strip().rstrip('.') if m.group(3) else ""
            if len(answer) > 3:
                cards.append(Card(
                    front=f"{q_word} {q_rest}?",
                    back=answer,
                    card_type="qa",
                    source=sent,
                ))
    return cards


def extract_lists(sentences: List[str]) -> List[Card]:
    """Extract list-type cards from 'There are N types of X: A, B, C'."""
    cards: List[Card] = []
    for sent in sentences:
        m = P_THERE_ARE_TYPES.search(sent)
        if m:
            count_word = m.group(1)
            category = m.group(2).strip()
            items_str = m.group(3).strip().rstrip('.')
            items = [it.strip() for it in re.split(r'[;,]', items_str) if it.strip()]
            for item in items:
                # Clean the item
                item = re.sub(r'^(?:and|or)\s+', '', item, flags=re.IGNORECASE).strip()
                if len(item) > 1:
                    cards.append(Card(
                        front=f"What is {item} in the context of {category}?",
                        back=f"{item} is one of the {count_word} types of {category}.",
                        card_type="qa",
                        source=sent,
                    ))
    return cards


def extract_cause_effect(sentences: List[str]) -> List[Card]:
    """Extract cause-effect cards."""
    cards: List[Card] = []
    for sent in sentences:
        for m in P_CAUSE_EFFECT.finditer(sent):
            cause = m.group(1).strip().rstrip(',').strip()
            effect = m.group(2).strip().rstrip('.')
            if len(cause) > 2 and len(effect) > 2:
                cards.append(Card(
                    front=f"What does {cause} cause?",
                    back=effect,
                    card_type="qa",
                    source=sent,
                ))
    return cards


def extract_comparisons(sentences: List[str]) -> List[Card]:
    """Extract comparison cards."""
    cards: List[Card] = []
    for sent in sentences:
        for m in P_COMPARISON.finditer(sent):
            x = m.group(1).strip()
            y = m.group(2).strip()
            detail = m.group(3).strip().rstrip('.')
            if len(detail) > 5:
                cards.append(Card(
                    front=f"How does {y} differ from {x}?",
                    back=detail,
                    card_type="qa",
                    source=sent,
                ))
    return cards


# ---------------------------------------------------------------------------
# Cloze generation
# ---------------------------------------------------------------------------

# Cloze target patterns (ordered by priority)
CLOZE_PATTERNS = [
    # Years
    (re.compile(r'\b(?:1[5-9]\d{2}|20\d{2})\b'), 'year'),
    # Percentages
    (re.compile(r'\b\d+(?:\.\d+)?\s?%'), 'percentage'),
    # Numbers with units
    (re.compile(r'\b\d+(?:\.\d+)?\s?(?:kg|g|mg|m|cm|km|s|ms|min|hour|°C|°F|Hz|W|V|mol|L|mL)\b'), 'number'),
    # Plain numbers
    (re.compile(r'\b\d{1,6}\b'), 'number'),
    # Acronyms (2+ uppercase)
    (re.compile(r'\b[A-Z]{2,}\b'), 'acronym'),
]

# Proper nouns (multi-word capitalized terms, excluding sentence starts)
P_PROPER_NOUN = re.compile(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b')

# Words to skip as cloze targets
CLOZE_SKIP_WORDS = {
    'The', 'This', 'That', 'These', 'Those', 'There', 'Here',
    'It', 'He', 'She', 'They', 'We', 'You', 'I',
    'What', 'When', 'Where', 'Why', 'How', 'Who', 'Which',
    'A', 'An', 'And', 'But', 'Or', 'So', 'If', 'Then',
    'In', 'On', 'At', 'To', 'For', 'Of', 'With', 'By', 'From',
    'Unlike', 'Whereas', 'While',
}


def generate_cloze_cards(sentences: List[str], max_cloze: int = 1) -> List[Card]:
    """Generate cloze-deletion cards by masking key terms."""
    cards: List[Card] = []
    cloze_counter = 1

    for sent in sentences:
        # Skip very short or very long sentences
        if len(sent) < 20 or len(sent) > 200:
            continue

        clozed_sent = sent
        clozes_made = 0

        # First, try priority patterns (years, numbers, acronyms)
        for pattern, label in CLOZE_PATTERNS:
            if clozes_made >= max_cloze:
                break
            matches = list(pattern.finditer(clozed_sent))
            for m in matches:
                if clozes_made >= max_cloze:
                    break
                term = m.group(0)
                replacement = f"{{{{c{cloze_counter}::{term}}}}}"
                clozed_sent = clozed_sent[:m.start()] + replacement + clozed_sent[m.end():]
                clozes_made += 1
                cloze_counter += 1
                # Adjust subsequent match positions — simplest: break and re-match
                break

        # If no priority pattern matched, try proper nouns
        if clozes_made == 0:
            for m in P_PROPER_NOUN.finditer(sent):
                if clozes_made >= max_cloze:
                    break
                term = m.group(1)
                # Skip sentence-starting words and common words
                if term in CLOZE_SKIP_WORDS:
                    continue
                # Skip if the word starts the sentence (likely subject, not a cloze target)
                if sent.strip().startswith(term):
                    continue
                # Only cloze multi-word proper nouns or known terms
                if ' ' in term or len(term) > 4:
                    replacement = f"{{{{c{cloze_counter}::{term}}}}}"
                    # Find in current clozed_sent
                    idx = clozed_sent.find(term)
                    if idx >= 0:
                        clozed_sent = clozed_sent[:idx] + replacement + clozed_sent[idx + len(term):]
                        clozes_made += 1
                        cloze_counter += 1

        if clozes_made > 0 and '{{c' in clozed_sent:
            cards.append(Card(
                front=clozed_sent,
                back="",  # Cloze cards use the Text field, not Front/Back
                card_type="cloze",
                source=sent,
            ))

    return cards


# ---------------------------------------------------------------------------
# Scoring & deduplication
# ---------------------------------------------------------------------------

def score_card(card: Card) -> int:
    """Score a card's information density (higher = better)."""
    score = 0
    combined = (card.front + " " + card.back).lower()

    if re.search(r'\d', combined):
        score += 2
    if 'defined' in combined or 'definition' in combined:
        score += 3
    if any(w in combined for w in ['unlike', 'whereas', 'differ', 'compare']):
        score += 2
    if any(w in combined for w in ['cause', 'result', 'lead to', 'trigger']):
        score += 2

    # Length scoring
    total_len = len(card.front) + len(card.back)
    if 15 <= total_len <= 80:
        score += 1
    elif total_len > 120:
        score -= 1

    return score


def normalize_for_dedup(s: str) -> str:
    """Normalize text for dedup comparison."""
    return re.sub(r'[^a-z0-9 ]', '', s.lower()).split()


def jaccard_similarity(a: str, b: str) -> float:
    """Jaccard similarity between two strings (word-level)."""
    set_a = set(normalize_for_dedup(a))
    set_b = set(normalize_for_dedup(b))
    if not set_a or not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)


def deduplicate(cards: List[Card], threshold: float = 0.85) -> List[Card]:
    """Remove near-duplicate cards based on Jaccard similarity of front text."""
    if not cards:
        return []

    unique: List[Card] = []
    for card in cards:
        is_dup = False
        for existing in unique:
            sim = jaccard_similarity(card.front, existing.front)
            if sim >= threshold:
                is_dup = True
                break
        if not is_dup:
            unique.append(card)
    return unique


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def to_csv(cards: List[Card], mode: str) -> str:
    """Format cards as Anki-importable CSV."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';', quoting=csv.QUOTE_ALL)

    if mode == 'cloze':
        writer.writerow(['Text', 'Extra'])
        for card in cards:
            if card.card_type == 'cloze':
                writer.writerow([card.front, card.back or ""])
    else:
        # qa or auto: output Q&A cards
        writer.writerow(['Front', 'Back'])
        for card in cards:
            if card.card_type == 'qa':
                writer.writerow([card.front, card.back])

    return output.getvalue()


def to_json(cards: List[Card]) -> str:
    """Format cards as JSON array."""
    return json.dumps([c.to_dict() for c in cards], indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def generate_flashcards(
    text: str,
    mode: str = 'auto',
    max_cards: int = 200,
    max_cloze: int = 1,
    min_length: int = 10,
    min_score: int = 0,
) -> List[Card]:
    """Generate flashcards from text."""
    cleaned = clean_text(text)
    sentences = split_sentences(cleaned)

    # Filter by minimum length
    sentences = [s for s in sentences if len(s) >= min_length]

    all_cards: List[Card] = []

    if mode in ('qa', 'auto'):
        qa_cards: List[Card] = []
        qa_cards.extend(extract_definitions(sentences))
        qa_cards.extend(extract_colon_definitions(cleaned))
        qa_cards.extend(extract_qa(sentences))
        qa_cards.extend(extract_lists(sentences))
        qa_cards.extend(extract_cause_effect(sentences))
        qa_cards.extend(extract_comparisons(sentences))
        all_cards.extend(qa_cards)

    if mode in ('cloze', 'auto'):
        cloze_cards = generate_cloze_cards(sentences, max_cloze=max_cloze)
        all_cards.extend(cloze_cards)

    # Score and filter
    scored = [(c, score_card(c)) for c in all_cards]
    if min_score > 0:
        scored = [(c, s) for c, s in scored if s >= min_score]
    scored.sort(key=lambda x: x[1], reverse=True)

    # Deduplicate
    cards = deduplicate([c for c, _ in scored])

    # Cap at max_cards
    if max_cards > 0:
        cards = cards[:max_cards]

    return cards


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Convert text into Anki-importable flashcards."
    )
    p.add_argument('input', type=Path,
                   help="Path to the input text file.")
    p.add_argument('-o', '--output', type=Path, default=None,
                   help="Output file path. Default: stdout.")
    p.add_argument('--mode', choices=['qa', 'cloze', 'auto'], default='auto',
                   help="Extraction mode. Default: auto (Q&A + cloze).")
    p.add_argument('--format', choices=['csv', 'json'], default='csv',
                   help="Output format. Default: csv.")
    p.add_argument('--max-cards', type=int, default=200,
                   help="Maximum number of cards to output. Default: 200.")
    p.add_argument('--max-cloze', type=int, default=1,
                   help="Maximum cloze deletions per card. Default: 1.")
    p.add_argument('--min-length', type=int, default=10,
                   help="Minimum sentence length to process. Default: 10.")
    p.add_argument('--min-score', type=int, default=0,
                   help="Minimum card quality score. Default: 0.")
    args = p.parse_args(argv)

    if not args.input.is_file():
        print(f"error: input file not found: {args.input}", file=sys.stderr)
        return 2

    text = args.input.read_text(encoding='utf-8', errors='replace')

    cards = generate_flashcards(
        text,
        mode=args.mode,
        max_cards=args.max_cards,
        max_cloze=args.max_cloze,
        min_length=args.min_length,
        min_score=args.min_score,
    )

    if args.format == 'json':
        output = to_json(cards)
    else:
        output = to_csv(cards, args.mode)

    if args.output:
        args.output.write_text(output, encoding='utf-8')
        qa_count = sum(1 for c in cards if c.card_type == 'qa')
        cloze_count = sum(1 for c in cards if c.card_type == 'cloze')
        print(f"Generated {len(cards)} cards ({qa_count} Q&A, {cloze_count} cloze)")
        print(f"Written to: {args.output}")
    else:
        print(output)

    return 0


if __name__ == '__main__':
    sys.exit(main())
