"""
Auto-generate routing.yaml from SKILL.md content.

Extracts keywords and patterns from skill metadata (name, description, trigger words)
to bootstrap a routing declaration without requiring manual configuration.
"""

import re
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    yaml = None


# Stopwords that should never be keywords (English + generic terms)
_STOPWORDS = {
    # English
    "the", "this", "that", "with", "from", "into", "when", "where", "what",
    "which", "will", "would", "should", "could", "have", "been", "being",
    "they", "them", "their", "then", "than", "also", "only", "just", "more",
    "most", "some", "such", "very", "well", "much", "many", "each", "both",
    "other", "like", "make", "made", "does", "done", "used", "uses", "using",
    "use", "and", "the", "for", "are", "but", "not", "you", "all", "can",
    "had", "her", "was", "one", "our", "out", "any", "its", "let", "get",
    "has", "him", "his", "how", "may", "new", "now", "old", "see", "way",
    "who", "did", "got", "say", "she", "too", "own",
    # Generic skill/agent terms
    "skill", "agent", "tool", "user", "based", "system", "support", "provide",
    "create", "generate", "help", "need", "want", "request", "action",
    "function", "method", "class", "type", "value", "data", "file", "name",
    "description", "author", "version", "category", "metadata",
    "professional", "quality", "important", "available", "required",
    "features", "includes", "provides", "supports", "allows",
    # Chinese generic
    "使用", "可以", "支持", "提供", "包含", "通过", "进行", "需要",
    "当前", "所有", "其他", "以及", "或者", "如果", "这个", "那个",
    "用于", "基于", "关于", "对于", "适用", "相关",
}


def _is_meaningful_keyword(word: str) -> bool:
    """Check if a word is meaningful enough to be a routing keyword."""
    w = word.lower().strip()
    if len(w) < 2:
        return False
    if w in _STOPWORDS:
        return False
    # Reject pure numbers
    if w.isdigit():
        return False
    # Reject single ASCII chars
    if len(w) <= 2 and w.isascii() and not w.isupper():
        return False
    return True


def _extract_quoted_triggers(text: str) -> list[str]:
    """Extract quoted strings that look like trigger phrases."""
    # Match: "xxx", 'xxx', 「xxx」, "xxx"
    patterns = [
        r'"([^"]+)"',
        r"'([^']+)'",
        r'\u300c([^\u300d]+)\u300d',
        r'\u201c([^\u201d]+)\u201d',
    ]
    results = []
    for pat in patterns:
        matches = re.findall(pat, text)
        for m in matches:
            m = m.strip()
            if 2 <= len(m) <= 30 and not m.startswith("http"):
                results.append(m)
    return results


def generate_routing_for_skill(skill_dir: Path, overwrite: bool = False) -> bool:
    """
    Generate routing.yaml for a skill by analyzing its SKILL.md.

    Strategy:
    1. Parse SKILL.md frontmatter for name, description, trigger keywords
    2. Extract trigger_keywords from frontmatter (highest priority)
    3. Extract quoted trigger phrases from body text
    4. Generate patterns from skill name
    5. Filter out stopwords and generic terms
    6. Write routing.yaml

    Returns True if file was generated, False otherwise.
    """
    if yaml is None:
        return False

    skill_md = skill_dir / "SKILL.md"
    routing_yaml = skill_dir / "routing.yaml"

    if routing_yaml.exists() and not overwrite:
        return False

    if not skill_md.exists():
        return False

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse frontmatter
    frontmatter = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2]
            except Exception:
                pass

    skill_name = frontmatter.get("name", skill_dir.name)
    description = frontmatter.get("description", "")
    summary = frontmatter.get("summary", "")

    # ─── Keyword extraction (priority order) ───

    keywords = []  # Ordered: higher priority first
    seen = set()

    def _add(word):
        w = word.strip()
        if w and w.lower() not in seen and _is_meaningful_keyword(w):
            keywords.append(w)
            seen.add(w.lower())

    # Priority 1: Explicit trigger_keywords in frontmatter
    for field in ("trigger_keywords", "keywords", "tags"):
        val = frontmatter.get(field)
        if isinstance(val, list):
            for item in val:
                if isinstance(item, str):
                    _add(item)
        elif isinstance(val, str):
            for item in val.split(","):
                _add(item.strip())

    # Priority 2: Skill name parts (meaningful ones)
    name_parts = re.split(r"[-_\s]+", skill_name)
    for part in name_parts:
        _add(part)

    # Priority 3: Quoted trigger phrases from description
    if description:
        for phrase in _extract_quoted_triggers(description):
            _add(phrase)

    # Priority 4: Quoted trigger phrases from body (trigger/use-when sections)
    trigger_patterns = [
        r"(?:trigger|triggers?|use when|触发|适用|当用户)[:\s：]*(.+?)(?:\n\n|\n#{1,3}\s|\Z)",
        r"(?:关键词|keywords?|trigger.?keywords?)[:\s：]*(.+?)(?:\n\n|\n#{1,3}\s|\Z)",
    ]
    for tp in trigger_patterns:
        match = re.search(tp, body, re.IGNORECASE | re.DOTALL)
        if match:
            section = match.group(1)
            # Extract quoted strings
            for phrase in _extract_quoted_triggers(section):
                _add(phrase)
            # Extract list items (- xxx)
            items = re.findall(r"^[\s]*[-*]\s*(.+)$", section, re.MULTILINE)
            for item in items[:15]:
                item = item.strip().strip('"').strip("'").strip("`")
                if 2 <= len(item) <= 25:
                    _add(item)

    # Priority 5: Chinese noun phrases from description (2-4 chars)
    if description:
        cn_phrases = re.findall(r"[\u4e00-\u9fff]{2,6}", description)
        for phrase in cn_phrases[:20]:
            _add(phrase)

    # Priority 6: Domain-specific English terms (3+ chars, capitalized or technical)
    if description:
        en_terms = re.findall(r"\b[A-Z][a-zA-Z]{2,}\b|\b[a-z]+[A-Z]\w+\b", description)
        for term in en_terms[:10]:
            _add(term)

    # ─── Pattern generation ───

    patterns = []

    # Generate patterns from skill name (if meaningful)
    meaningful_parts = [p for p in name_parts if _is_meaningful_keyword(p) and len(p) >= 2]
    if len(meaningful_parts) >= 2:
        # Create a loose OR pattern for skill name parts
        escaped = [re.escape(p) for p in meaningful_parts]
        patterns.append(f"({'|'.join(escaped)})")

    # If description has Chinese, try to extract verb+noun patterns
    if description:
        # Look for "动词+名词" structures in Chinese
        verb_noun = re.findall(r"([\u4e00-\u9fff]{1,2})([\u4e00-\u9fff]{2,4})", description[:200])
        if verb_noun:
            # Take first few as candidate patterns
            for v, n in verb_noun[:3]:
                if _is_meaningful_keyword(v + n):
                    patterns.append(f"{re.escape(n)}")

    # ─── Anti-patterns from description ───

    anti_patterns = []
    # Look for explicit "不适用/不触发/don't use" sections
    anti_match = re.search(
        r"(?:不适用|不要|don't|do not|不触发|excluded?|except)[:\s：]*(.+?)(?:\n\n|\n#{1,3}\s|\Z)",
        body, re.IGNORECASE | re.DOTALL
    )
    if anti_match:
        section = anti_match.group(1)
        items = re.findall(r"^[\s]*[-*]\s*(.+)$", section, re.MULTILINE)
        for item in items[:5]:
            item = item.strip().strip('"').strip("'")
            if 2 <= len(item) <= 30:
                anti_patterns.append(item)

    # ─── Build final config ───

    routing_data = {
        "name": skill_name,
        "description": (summary or description or f"Auto-generated routing for {skill_name}")[:200],
        "routing": {
            "keywords": keywords[:15],  # Cap at 15, already priority-ordered
            "patterns": patterns[:5],
            "anti_patterns": anti_patterns[:5],
            "priority": 50,
        }
    }

    # Write routing.yaml
    with open(routing_yaml, "w", encoding="utf-8") as f:
        yaml.dump(routing_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    return True
