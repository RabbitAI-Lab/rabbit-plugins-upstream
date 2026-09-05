# Extraction Patterns & Confidence Scoring

## Input normalization

1. Strip timestamp prefixes: `10:42` / `10:42:15` / `[10:42]` at line start
2. Detect speaker prefixes: `Name:` at line start (Name = 1-3 capitalized tokens)
   → speaker becomes an owner candidate for that line's commitments
3. Strip markdown bullets (`-`, `*`, `•`) and checkboxes (`- [ ]`, `- [x]`)
4. Split on sentence boundaries (. ! ?) for pattern matching

## Action item grammar

Priority order (first match wins per clause):

```
1. SECTION   : ^(action items?|next steps?|follow.?ups?|todos?)\s*:?$
              → every subsequent list item is an action until a non-list line
2. ASSIGNED  : assign(ed)? to <OWNER>          → owner=<OWNER>
3. COMMIT    : <OWNER> (will|'ll|shall|should|is going to|agreed to|committed to) <ACTION>
4. VOLUNTEER : (I|we)'ll <ACTION>              → owner = line speaker, or Unassigned
5. DELEGATE  : <OWNER> (can you|could you|please) <ACTION>?
              → question-flagged action (needs acceptance), confidence 0.6
6. IMPERATIVE: bare verb phrase in a list      → Unassigned
```

Owner vocabulary: capitalized names, @handles, role aliases (PM, TL, design,
legal, marketing — mapped to `role:<name>`), "me"/"I" → line speaker.

## Negations and non-actions

Excluded from actions:

- "will not", "won't", "decided against", "no longer"
- Past-tense status reports ("sent the deck", "already did") → status notes
- Conditionals: "if X happens, we might" → open question instead
- "We should probably / consider / think about" → action with confidence 0.4
  ("weak") — surfaced for review, never silently promoted

## Date parsing (resolved against meeting date)

| Pattern | Resolution |
|---|---|
| `YYYY-MM-DD`, `MM/DD/YYYY`, `DD.MM.YYYY` | absolute |
| `today` / `tomorrow` | meeting_date (+1) |
| `next <weekday>` | next occurrence strictly after meeting date |
| `<weekday>` / `by <weekday>` | the upcoming occurrence (≥ meeting date; if today is that weekday → +7) |
| `end of (the )?week/month/quarter` | Friday of this week / last day of month/quarter |
| `in N (days\|weeks\|months)` | meeting_date + N |
| `next week` | Monday of next week |
| `EOD` / `COB` | meeting_date |
| `a.s.a.p`, `asap`, `urgent` | meeting_date + urgency flag |

Unparseable dates stay verbatim with `due_raw` preserved and a flag.

## Confidence scoring

| Score | Meaning | Display |
|---|---|---|
| 0.9+ | explicit pattern + owner + date | normal |
| 0.7 | explicit pattern, missing owner or date | "needs owner" / "no deadline" |
| 0.6 | delegated-as-question ("can you…?") | "confirm acceptance" |
| ≤0.5 | weak verbs (should/probably/consider) | "review before sending" |

## Decisions

Triggers: `we (decided|agreed|chose|settled on|going with)`, `approved`,
`rejected`, `green.?light`, `sign.?off`, `deferred`, `postponed`,
`cancelled`. The clause after the trigger is the decision text.
"We discussed / talked about" explicitly does **not** create a decision.

## Open questions

Lines/clauses containing `?`, or starting `question:`, or containing `TBD`,
`TBD?`, `open question`, `unresolved`, `we don't know`, `need to figure out`.
If a line is both a question and contains a commitment verb, it becomes a
question-flagged action (pattern 5) — asking someone to do something is an
action pending acceptance.

## Deduplication

Two items merge when: normalized text Jaccard similarity ≥ 0.8 (token sets,
stopwords removed, lowercased) **and** same owner (or one unassigned → adopt
the assigned owner). Merged items keep the earliest deadline and max
confidence, and record `duplicates: N`.

## Carryover logic

Given previous JSON: any previous action whose normalized text matches
(≥0.7 similarity) a completed item in today's notes ("done", "sent",
"shipped", checkbox `[x]`) is closed. Others roll forward with:

- `age_meetings`: 1, 2, 3+…
- `stale` flag at 3+ with escalation note ("blocked or dead — decide")

New items never inherit completion.

## Output schema (JSON)

```json
{
  "meeting": {"title": "...", "date": "2026-08-12"},
  "decisions": [{"text": "...", "line": 14}],
  "actions": [{"description": "...", "owner": "Sarah", "due": "2026-08-14",
                "due_raw": "by Friday", "confidence": 0.95, "flags": [],
                "source_line": 23, "duplicates": 0}],
  "questions": [{"text": "...", "line": 31}],
  "carryover": [{"description": "...", "age_meetings": 2, "stale": false}]
}
```
