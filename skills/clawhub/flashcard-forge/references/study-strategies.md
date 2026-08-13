# Study Strategies for Flashcard-Based Learning

Flashcard Forge generates cards; these strategies help you use them effectively.

## Core Principles

### 1. Active Recall Over Recognition

Flashcards work because they force you to **retrieve** information, not just
recognize it. Always try to answer before flipping the card. If you just read
both sides passively, you're wasting the medium.

### 2. Spaced Repetition

Anki's algorithm schedules reviews at increasing intervals:
- New card → 1 day → 3 days → 7 days → 21 days → 60 days → ...

Trust the algorithm. Don't cram all cards daily — that defeats the spacing
effect. Review what Anki tells you to review, when it tells you.

### 3. One Idea Per Card

If a card has multiple facts, split it. "List the 3 types of muscle" is a poor
card; three separate cards (one per muscle type) are better.

Flashcard Forge's list-pattern extractor attempts to split lists into
individual cards, but review the output and split any that are still overloaded.

## Card Quality

### Good Cards

- **Specific**: "What enzyme unwinds DNA during replication?" → "Helicase"
- **Atomic**: One fact, one answer
- **Contextual**: Include just enough context to disambiguate
- **Varied**: Mix definitions, comparisons, cause/effect, and cloze

### Bad Cards

- **Vague**: "Tell me about cells" → too broad
- **Multi-answer**: "What are the 4 bases in DNA and how do they pair?" → split
- **Yes/No**: "Is the mitochondria the powerhouse?" → too easy to guess
- **Wall of text**: Front or back longer than 2 sentences

## Workflow

### Daily Review (15-30 minutes)

1. Open Anki, review all due cards.
2. Answer each card **before** flipping.
3. Rate honestly:
   - **Again** (red): didn't know it → resets to relearn
   - **Hard** (orange): barely got it → shorter interval
   - **Good** (green): normal → standard interval
   - **Easy** (blue): instant recall → longer interval
4. Aim for 85-95% retention. Lower = cards too hard. Higher = cards too easy.

### Weekly Deck Maintenance

1. Review flagged/difficult cards — are they poorly written?
2. Delete cards you consistently get right (they've served their purpose).
3. Add new cards for material you struggled with this week.
4. Check for duplicates (Anki's "Find Duplicates" tool).

### Pre-Exam Intensive

1. Import new material with Flashcard Forge 2-3 weeks before the exam.
2. Review daily, focusing on new and due cards.
3. In the final week, use Anki's "cram" mode to review all cards in the deck.
4. Don't add new cards in the last 3 days — focus on consolidating.

## Cloze vs Q&A

| Use Q&A When                          | Use Cloze When                        |
| ------------------------------------- | ------------------------------------- |
| Testing a definition                  | Testing recall within context         |
| Explicit question-answer structure    | Filling in a key term in a sentence   |
| The "answer" is a short phrase        | The fact is embedded in a sentence    |
| You want flexibility in phrasing      | You want to test recognition          |

Flashcard Forge's `auto` mode generates both and deduplicates, giving you a
mixed deck that engages different recall pathways.

## Pitfalls

1. **Card overload.** More cards ≠ better. 200 good cards beat 1000 mediocre
   ones. Cap output with `--max-cards` and curate aggressively.

2. **Passive review.** If you're not struggling to recall, the cards aren't
   working. If recall is effortless, the card may be too easy — delete or
   rephrase.

3. **Neglecting difficult cards.** Anki's "ease hell" happens when you mark
   cards "Again" repeatedly. Reset the ease or rewrite the card.

4. **Stale decks.** If you haven't reviewed a deck in months, the backlog can
   be demoralizing. Use Anki's "Forget" to reset cards to new, or archive the
   deck.

## Further Reading

- [Anki Manual](https://docs.ankiweb.net/) — official documentation
- [Augmenting Long-term Memory](https://supermemo.guru/wiki/Augmenting_Long-term_memory)
  by Michael Nielsen — excellent essay on spaced repetition
- [20 Rules of Formulating Knowledge](https://supermemo.guru/wiki/20_rules_of_formulating_knowledge)
  by Piotr Woźniak — the canonical guide to writing good flashcards
