# Project Manifesto: Knowledge Base for an AI Psychological Consultant

## THE PURPOSE OF THE PROJECT

We are building a knowledge base for an AI psychological consultant on the znai.cloud platform.

But this is not just a collection of techniques. It is an attempt to create **integrated wisdom** — a system where different therapeutic schools do not compete, but complement one another.

**The core hypothesis:**
Different great therapists discovered different parts of one truth. If you bring them together in the right way, you get something greater than the sum of its parts.

---

## AUTHOR SELECTION CRITERION

**"Did the author live their own teaching?"**

We include only those who:
1. Went through suffering themselves
2. Applied their method to their own life
3. Lived in accordance with their principles to the very end

Why this matters: a theory not tested by life is empty words. We are looking for wisdom confirmed by biography.

**Examples:**
- **Frankl** — survived Auschwitz, lost his entire family, and still found meaning. Worked until the age of 92.
- **Rogers** — overcame a rigid religious upbringing and became the embodiment of acceptance. Nominated for the Nobel Peace Prize.
- **Beck** — conquered his childhood fears through cognitive reframing. Was working on a paper at 100 years old, confined to bed.
- **Ellis** — defeated paralyzing shyness with his own method at 19. Led workshops well into old age.

---

## SYSTEM ARCHITECTURE

**Roles of the authors:**

| Author | Role in the system | Answers the question |
|--------|--------------------|----------------------|
| Rogers | Tone, atmosphere | HOW to talk to a person |
| Frankl | Meaning, direction | WHY live, suffer, change |
| Beck | Tools for thoughts | HOW to change thinking |
| Ellis | Philosophy, core beliefs | WHAT to change at the foundation |

**The principle of complementarity:**
- Rogers creates safety → the person opens up
- Beck/Ellis provide tools → the person changes their thinking
- Frankl provides direction → the person understands why to change

Without Rogers — techniques will be cold and ineffective.
Without Beck/Ellis — acceptance without change.
Without Frankl — change without meaning.

---

## FILE CREATION METHODOLOGY

### Structure of each file:

1. **Author biography** — who they were, what they went through, why they can be trusted
2. **Core idea** — the essence of the approach in one sentence
3. **Key concepts** — theoretical foundation
4. **Techniques** — concrete tools with examples
5. **Real cases** — documented success stories
6. **When to apply** — indications and limitations
7. **Quotes** — the author's voice
8. **Dialogue examples** — how it sounds in practice
9. **Integration** — how it combines with other authors

### Writing principles:

**1. Self-sufficiency of chapters**
Each chapter must be understandable without the context of other chapters. This is critical for a RAG system that will extract individual fragments.

**2. Practicality**
Theory — only as a foundation for practice. The main thing is what to do, how to speak, what questions to ask.

**3. Concrete examples**
Abstract principles + concrete dialogues. The AI must see how it sounds.

**4. Honesty about limitations**
Every approach has boundaries. We state them.

**5. The author's voice**
Quotes, style, characteristic expressions. So that the wisdom stays alive.

---

## BREAKTHROUGH IDEA: THE CASE MATRIX

**The concept:**
Collect real successful cases from different authors → Group by problem type → Find intersections → Derive the "formula" of an effective intervention.

**Why this is new:**
- Schools are usually taught separately
- Integration happens intuitively in experienced therapists
- No one has systematized this at the level of concrete cases

**Example matrix:**

| Problem | Frankl | Rogers | Beck | Ellis |
|---------|--------|--------|------|-------|
| Anxiety | Paradoxical intention | Acceptance | Challenging thoughts | Exposure + MUST |
| Depression | Finding meaning | Unconditional acceptance | Cognitive triad | Catastrophizing |
| Low self-esteem | Meaning beyond oneself | Reflection | Core beliefs | Unconditional self-acceptance |
| Guilt | Reframing | Non-judgment | Thought records | Behavior ≠ the person |
| Grief | Suffering as achievement | Accompaniment | — | Acceptance of life |
| Addiction | Existential vacuum | — | Functional analysis | Low frustration tolerance |

**Next step:**
When enough cases accumulate — create a separate matrix file with recommendations: "For problem X — a combination of techniques Y from authors Z."

---

## CURRENT STATUS

| № | Author | File | Lines | Chapters | Status |
|---|--------|------|-------|----------|--------|
| 1 | Frankl | 01-frankl-logotherapy.md | 446 | 12 | ✅ Ready |
| 2 | Rogers | 02-rogers-client-centered.md | 383 | 10 | ✅ Ready |
| 3 | Beck | 03-beck-cognitive-therapy.md | 667 | 14 | ✅ Ready |
| 4 | Ellis | 04-ellis-rebt.md | 666 | 16 | ✅ Ready |

---

## POTENTIAL NEXT AUTHORS

**High priority (lived their teaching):**
- **Irvin Yalom** — existential therapy, group therapy. Wrote openly about his own fears of death.
- **Marsha Linehan** — DBT. Publicly acknowledged that she herself suffered from borderline personality disorder.
- **Milton Erickson** — hypnotherapy. Survived polio, learned to walk again through self-hypnosis.

**Medium priority:**
- **Fritz Perls** — Gestalt. A contradictory personality, but powerful techniques.
- **John Bowlby** — attachment theory. The foundation for understanding relationships.

**Specific areas:**
- **Francine Shapiro** — EMDR for trauma
- **Steven Hayes** — ACT (Acceptance and Commitment Therapy)

---

## HOW TO CONTINUE THE WORK (INSTRUCTIONS FOR THE NEXT SESSION)

### Step 1: Context
Read this file (00-project-manifesto.md) to understand the project.

### Step 2: Choosing an author
Ask the user whom to add next. Or propose one from the list above.

### Step 3: Research
Use web_search to gather materials:
- Biography (especially personal experience of suffering)
- Core concepts and techniques
- Real cases (session transcripts, studies)
- Quotes

### Step 4: Creating the file
Follow the structure of the existing files:
- Numbering: 05-author-method.md, 06-author-method.md, etc.
- Self-sufficient chapters
- Dialogue examples are mandatory
- Integration with other authors at the end

### Step 5: Updating the matrix
After each new author — add their cases to the shared problem/solution matrix.

---

## PROJECT PHILOSOPHY

**We believe that:**

1. **Suffering is part of life, but not all of life.** One can learn to relate to it differently.

2. **People are capable of change.** Not because they are broken and need fixing, but because it is in their nature to grow.

3. **Different approaches are different doors into the same room.** For some, thoughts are closer (Beck); for others, feelings (Rogers); for others, meaning (Frankl); for others, actions (Ellis).

4. **AI can be a bridge to wisdom.** Not a replacement for a therapist, but an entry point, first aid, daily support.

5. **Quality over quantity.** Better 5 deeply developed authors than 50 superficial ones.

---

## LIMITATIONS AND HONESTY

**What this project is NOT:**

- A replacement for professional psychotherapy
- A diagnostic tool
- A universal solution for all problems

**When to refer to a specialist:**

- Suicidal thoughts or plans
- Psychotic symptoms
- Severe disorders (bipolar, schizophrenia)
- Acute trauma
- Addiction in its active phase
- When AI support is not enough

**Ethical principles:**

- Do no harm
- Honesty about limitations
- Respect for the person's autonomy
- Confidentiality

---

## AFTERWORD

This project is an attempt to preserve and pass on the wisdom of people who devoted their lives to understanding human suffering and the ways to ease it.

Frankl found meaning in Auschwitz.
Rogers learned to accept without conditions.
Beck turned thoughts into a tool.
Ellis defeated his own fears with his own method.

Their knowledge must not remain in books that no one reads. It must work — helping people every day.

That is the meaning of our work.

---

*File updated: November 2024*
*Project: znai.cloud AI psychological consultant*
