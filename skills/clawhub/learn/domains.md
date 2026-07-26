# Domains — Same Loop, Different Ratios

Read when a topic starts, and whenever the standard loop is producing less than expected. The system does not change by subject; the drill/project mix, the review load, the feedback substitute and the characteristic failure do.

**Contents:** [The Six Types](#the-six-types) · [Languages](#languages) · [Programming](#programming) · [Mathematics and Formal Subjects](#mathematics-and-formal-subjects) · [Music and Physical Skills](#music-and-physical-skills) · [Fact-Dense Fields](#fact-dense-fields) · [Judgement and Taste Domains](#judgement-and-taste-domains) · [Mixed Topics](#mixed-topics)

## The Six Types

Classify the topic before planning it; most topics are a mix, and the mix decides the ratios.

| Type | Queue load | Drills : projects | Feedback substitute | Characteristic failure |
|---|---|---|---|---|
| Language | Very high | 40 : 60 | Native speaker, recordings, graded readers | Recognition trained, production absent |
| Programming | Low | 25 : 75 | Tests, compiler, reference implementations | Tutorial hell; copied code, no model |
| Formal (maths, proofs, logic) | Medium | 60 : 40 | Worked solutions, symbolic checkers | Reading solutions instead of producing them |
| Motor (music, sport, craft) | Very low | 70 : 30 | Recording, metronome, coach | Practising mistakes at speed |
| Fact-dense (medicine, law, taxonomy) | Very high | 80 : 20 | Question banks, past papers | Volume without organising structure |
| Judgement (design, writing, strategy) | Low | 20 : 80 | Rubric, expert diff, critique | Confident output, no calibration |

Common to all six: retrieval before re-exposure, ~85% difficulty, feedback inside its latency budget, and a production step per session.

## Languages

- **Frequency is the whole curriculum at the start.** The first ~1,000 words carry most of ordinary speech; the next 1,000 buy far less. Learn them by frequency list, not by textbook theme order.
- **Comprehensible input needs ~90%+ known words** to work as input. Below that it is noise consumed effortfully — use graded material until the threshold, then immerse (SKILL.md, Where Experts Disagree).
- **Four skills, four training paths.** Listening, reading, speaking, writing improve nearly independently. A learner who reads well and cannot speak has not lost anything; they trained two of the four. Speaking is trained by speaking, from week one, badly.
- **Production drills**: output with a constraint — describe the room using only the past tense; retell the paragraph you just read without looking; keep a five-sentence daily journal that a partner corrects.
- **Pronunciation early, not later.** Errors fossilise, and self-review cannot catch what the ear does not distinguish. This is the strongest case in any domain for paying a human for a few hours (`practice.md`).
- Queue: vocabulary both directions (reverse pairs), collocations rather than isolated words, and whole sentences over single terms — a sentence carries grammar and usage in one item (`capture.md`).

## Programming

- **The compiler is a feedback loop with near-zero latency**; use it. Predict the error before running, then run. The prediction is the learning event, and skipping it wastes the best feedback loop any domain has.
- **Low queue load**: most syntax is looked up constantly and lives in muscle memory or the editor. Queue only what stops the flow — semantics, the standard library's shape, error meanings, command flags used weekly.
- **Read code as a path, not a plane** (`sources.md`): one entry point, one path to the end.
- **The debugging skill is separate from the language** and is trained separately: hypothesis before reading, bisect, minimal reproduction. Most self-taught developers never train it deliberately and it is the largest single differentiator in daily speed.
- **Rung 4 of the scaffolding ladder is where programming is actually learned** (`projects.md`). Everything before it is preparation.

## Mathematics and Formal Subjects

- **Reading a proof is not learning it.** Cover the proof, attempt it, then read. The gap between what you produced and what is written is the entire lesson.
- **Definitions are queue items; theorems are drills.** A definition must be produced verbatim-equivalent; a theorem must be applied and, at higher levels, re-derived.
- **Do the exercises, all of the odd ones with answers.** Density of graded feedback per hour is higher here than in any other domain, and it is free.
- **Errors are almost always in one of three places**: a mis-stated definition, an unchecked hypothesis of the theorem used, or algebra. Tag error-log rows with which — the distribution tells you what to drill.
- Difficulty control is by problem selection, not by time spent staring; below the 85% band, drop a difficulty tier rather than persisting for hours (`practice.md`).

## Music and Physical Skills

- **Slow practice is the technique**, not a warm-up for it. Speed acquired above the error-free tempo installs the error. Rule: raise the metronome ~5% only after three consecutive clean repetitions.
- **Small units.** Two bars, one transition, one movement — repeated with attention, not the whole piece repeated with hope.
- **Record and review after ≥1 day** (`practice.md`). The gap between how it felt and how it sounds is where the improvement is, and same-day review excuses it.
- **Consolidation is sleep-dependent and time-dependent**: motor skills improve measurably between sessions, so short daily practice beats a weekly block far more sharply here than elsewhere (`time.md`).
- **Almost no queue.** What little there is: notation, fingerings, terminology, chord shapes as image occlusion.
- Motor skills decay slowest of all types once acquired, which is why maintenance intervals here are long (`maintenance.md`).

## Fact-Dense Fields

- **Volume is the problem, so the ratio in Rule 3 is binding rather than advisory.** At 20 new items a day the steady-state review load is ~200/day; decide that before starting, not in month three (`schedule.md`).
- **Organise before memorising.** Facts hung on a structure — a mechanism, a taxonomy, a timeline, a chain of causes — cost a fraction of the same facts held individually, and they transfer. Build the structure first, then attach.
- **Question banks are the primary resource**, not the textbook: they are graded practice at scale, and they reveal what the examiner or the field actually asks.
- **Reverse and contrast items** carry most of the value: pairs that are easily confused are what the field's errors are made of (`capture.md`).
- Retire aggressively. Facts that stop being used should leave the queue; the queue is not a completeness obligation.

## Judgement and Taste Domains

Design, writing, strategy, negotiation, product sense — the hard cases, because there is no key.

- **Build the rubric before producing**, and grow it from every external critique (`practice.md`). Without one, self-review is mood.
- **Expert diff is the highest-fidelity feedback available**: attempt the brief, then compare against a strong practitioner's solution to the same brief. The difference is the curriculum.
- **Volume beats deliberation early.** Twenty attempts with critique beats two agonised ones; the calibration comes from the spread.
- **Verification is by transfer to an unseen brief**, judged by someone who is not you — or by the rubric applied cold a day later (`verification.md`).
- Queue load is low: principles, not instances. Instances go in a swipe file, which is an artifact, not a queue.

## Mixed Topics

Most real goals are mixes: a clinical skill is fact-dense plus motor; a data role is programming plus formal plus judgement; a musical instrument is motor plus formal notation.

1. Split the exit test by component type.
2. Apply each component's ratios to its own stages — do not average them into one mediocre loop.
3. Interleave components only once each is past the ~80% within-session threshold (`practice.md`).
4. Expect the components to progress at different speeds; that is not imbalance, and forcing them level slows the whole thing.

Record the topic's type mix in its row in `## Topics` (or in the plan's header when it is a mix), because the ratios are what a future session needs in order to design a drill without re-deriving them. Anything the type mix changed — a queue policy, a drill/project split, a feedback substitute chosen — goes into `plans/<topic>.md` as a dated revision line. Formats in `memory-template.md`.
