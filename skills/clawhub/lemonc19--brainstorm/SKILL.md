---
name: brainstorm
description: "You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything new, in software or out of it (a talk, a business, a renovation). Deliver written work as a strict file-io loop: re-read the source, the request, the deliverable, and any supplied tests from disk; apply exactly one decided edit; read the whole file back fresh; measure every rule; append a ledger row with current, previous, and delta values; verify the appended record; and repeat for at least fourteen rounds. Record every difference observed in each round. Never substitute memory, grep, partial reads, summaries, or bundled commands for full reads and discrete file operations."
---

# Brainstorming

You are very good at building. You build what you believe your human partner wants, and that belief is usually thinner than it feels. This skill is for finding out what they actually want, and why, before anything gets built.

People often have not finished working out what they want. Good questions help them think it through. When you understand the why, you make the hundred decisions they never mention the way they would have made them.

What you write down is a claim about the world, and claims drift. A document you remember writing is not a document that exists. The only evidence that your work is correct is the file on disk, read back after the write, measured, compared with the source, compared with the previous ledger row, and then verified a second time. That comparison is the loop at the center of this skill, and it is not optional polish. It is how the work actually gets finished. Everything else in this document is commentary on the loop.

The loop is where the value is. A draft written in one pass and never re-read is a guess with good formatting. Fourteen rounds of read-write-read-verify is a design someone can build from. Do not compress the loop, do not summarize it away, do not bundle several operations into one command when the skill asks for discrete operations, and do not claim a step happened that has no file operation behind it.

## Non-Negotiable File-IO Contract

For every written deliverable produced by this skill:

1. The source of truth is re-read from disk at the start of every round.
2. The deliverable is read in full before it is edited.
3. Each round applies exactly one decided content fix to the deliverable.
4. The edited deliverable is read back in full as a fresh read.
5. Every measurement is taken during that fresh read or from that round's fresh source reads.
6. The previous ledger row is re-read before the new row is composed.
7. The new ledger row is appended as a separate record operation.
8. The file is read a final time in full to verify the appended record.
9. The differences between this round and the previous round are recorded as numbers, inventory values, hash values, and prose.
10. The loop continues for at least fourteen complete rounds unless the safety valve is triggered at the end of round sixteen.

A "round" is a sequence of operations, not a paragraph describing intentions. If you cannot point to the read, write, or verification command that produced a fact, the fact is not a measurement. If you cannot point to a row that records the difference, the round did not complete.

Use the available file editing or patch tool when present. When using shell commands, keep each required operation discrete and observable. Do not hide the loop by chaining unrelated operations, using only a filtered grep where a full read is required, or deriving a count from memory.

## First: What Do You Actually Know?

Before you reply, ask yourself: what do I know about what they want, and why?

- **Everything that matters is in the request** ("make the icon cornflower blue"). This is a quick, clear task. Do it, and say what you did.
- **Something non-trivial is missing.** Start the conversation, or, if there is no one to have it with, take the ground yourself.

Before implementing, you must, in order:

1. Examine the current tool on disk, in full, more than once.
2. Lay out the approaches, and have them picked; when no one is available, pick and record.
3. Write the design document, short or full.
4. Get approval of that document, or record that approval is unavailable and proceed on assumptions you can defend.
5. Run the round loop until the document converges through measured evidence.

Two things are not implementing: a spike they said yes to, and doing what they asked once they have opted out of questions.

## Look Before You Ask

In an existing project, or when they have given context, dig in before your first message. Read what they referred to and the material it connects to, and keep reading until you can explain how the relevant parts work today and what this change would touch. Never ask what the project or their context already answers.

For each round's re-ground, read these items separately when present:

- The tool or artifact under discussion, from first line to last line.
- The project README or primary docs, from first line to last line.
- Any supplied tests or acceptance rules, from first line to last line, when reading them does not modify them.
- The user request or task text, when its exact wording bears on a claim.

**Three passes are required for the first grounding, and at least one full re-ground is required in every round.** Pass one reads for shape: what exists, what it does, how it is invoked. Pass two reads for specifics: identifiers, command names, subcommand spellings, data shapes, defaults, ordering, file locations, error paths, and documentation claims. Pass three reads for absences: what the file does not do, does not sort, does not filter, does not validate, does not escape, does not handle.

Record the result of each pass as observations you will quote later. These observations become the claim register. A sloppy first read costs you rounds later.

Reading once is not digging in. Facts quoted later get re-checked on the ground. The source of truth is re-read at the start of every round, not recalled.

## When There Is No One to Ask

Sometimes the requester is absent, unreachable, or has explicitly opted out of further conversation. The skill does not stop and it does not stall on a gate no one will ever open.

- Ask the question anyway, in the document, under **Open Questions**. Every question you would have asked in the conversation belongs there, in plain words, and it ends with a question mark. Three is the floor, not the target.
- Answer it yourself with the best-supported assumption, stated right under the question, and name the evidence: the code you read, the convention the project already follows, the constraint in the request. Mark it clearly as an assumption, never as something they agreed to.
- Treat every assumption as a thing the loop must verify. If the document claims the tool behaves a certain way, that claim gets checked against the file on disk, not against your memory of the file.
- Keep the ground rules from the request. "Do not modify the source", "no code", "the deliverable is the document" are decisions, not suggestions. Re-verify them every round with measurements.
- Silence is not permission to shorten the loop. With no partner to catch a wrong assumption, the rounds are the only reviewer you have.

## Your First Message

When there is someone to talk to, move the work forward with one of these:

- **They have already said what they want**: about 200 words for the whole message. Echo their request back in your own words: what they want, who it is for, and why. Add what you found that bears on it. If you found a constraint, conflict, or cheaper path, say so plainly. End with one line inviting corrections, then one question about what they want.
- **They have not**: one open question, in their own terms, about the biggest thing their request leaves unsettled. Say why the answer would change what you build.

If they are not available at all, the conversation collapses into the document: ground yourself, write it up, and run the loop for the full minimum rounds.

## The Conversation

Each message ends with one question: a single sentence, no list of example answers. Plain language, pitched a little above the partner, matching their vocabulary. No process jargon.

**Get them describing.** Open questions come first. Their words carry intent. Offer a short menu only when they are stuck. When they say "just guess" or "what do you think?", propose something concrete.

**How it gets made.** Find out early which choices they want to make, which they are handing to you, and what they already have. Build on what the project already uses. Any choice you make goes in the design as your call, never as something they agreed to.

**Ground to cover.** This is territory, not a script: what kind of thing this is and what makes it special; why now; success; goals; non-goals; anti-goals; prior art; current state; details they care about.

**Make every question specific** to the project and what they have told you. Ask as a sharp colleague would, building on their last answer or on something found on disk.

**Lay out the approaches.** Before writing anything up, put the ways of building it in a separate message or, if no one is available, a separate section. Come up with several real alternatives and drop weak ones. Present two or three that remain, grounded in what the project actually does, each with what it trades off. Recommend one and say why. Prose that describes "the" way is not approaches. Each option needs its own name, shape, pros, and cons. When there is genuinely one sensible way, say so, explain why the others do not fit, and still record the rejected alternatives.

**Show, don't tell.** Offer the visual companion only when a conversation is possible and seeing would help more than reading. If the requester is absent, describe in words and put the detail in the document.

**Spike to feel things out.** A quick throwaway build is sometimes the cheapest way to learn what they want. Only when they asked for it and the task allows it. If "no code" is part of the request, there is no spike.

## The Round

The document is finished by rounds. A round has ten operations, in this order, each one its own discrete file or shell operation unless an available tool makes two of them one atomic required action:

1. **Re-ground the source.** Read the tool or artifact under discussion from first line to last line. Write down one observation from this read: something now visible that was not visible last round, or the explicit statement that nothing new appeared.
2. **Re-ground the surrounding docs.** Read the README or project documentation from first line to last line. Note whether the design document's wording still agrees with it.
3. **Re-ground acceptance material.** Read any supplied tests, rules, or acceptance text from first line to last line. If the tests may be run without modifying anything, run them and record the pass or fail count.
4. **Read the deliverable.** Open the design document from disk in full before touching it, including the previous ledger rows. Note the single thing you will fix in step five before you write it, so the fix is decided, not improvised.
5. **Write one content fix.** Apply exactly one decided fix to the deliverable file: the first full draft, then a targeted correction to one section. Write it to disk. Then stop. Do not make a second content edit in the same round. One change per round makes the next measurement meaningful.
6. **Read back in full.** Read the file from disk, in full, as a fresh read. Not your draft, not a remembered excerpt, not a range you already looked at, not tail, not a filtered grep pretending to be a read. While reading, take every measurement listed in Measurements. Every number recorded in this round must come from this read.
7. **Diff and compose the row.** Compare this round's measurements and re-grounded observations against the previous round's, taken from the previous row re-read in step four. Compose one ledger row. Record the differences, including the boring ones: a heading that changed wording, a bullet that changed length, a count that stayed put, a hash that stayed identical, a test count that remained the same. Then name exactly one fix for the next round, or state that no fix is needed.
8. **Append the ledger row.** Append the composed row to the deliverable as the round's record operation. This is separate from the content fix. The ledger row is a record, not a design edit.
9. **Verify the record.** Read the file from disk one more time in full and confirm three things: the row is present and intact, its numbers match the measurements taken in step six, and the append did not disturb any required heading, required count, hash line, claim register line, or code-free rule. Any mismatch is a rule failure, goes into the row's failure column, and becomes the single fix for the next round.
10. **Scope audit.** Confirm from disk that protected source files are unchanged by hash and byte count, that no unintended files exist in the workspace, and that the deliverable remains the requested artifact only. Record these values in the row.

Never collapse the steps. Reading your own write call and calling it a read back is not a round. Re-deriving a count from memory is not a measurement. Deciding a fix without reading is not a diff. Appending the row without the verification read is an unproven record. If you cannot point at the file read that produced a number, throw the number away and take it again.

**Two full deliverable reads, one content edit, one record edit, every round.** The doubling is the point: step six measures the document, step nine measures your record about the document. Records are claims too, and claims drift.

## Minimum Rounds

Fourteen complete rounds, at minimum, even if round twelve looks perfect. This is not a stretch goal; it is the floor. A document delivered at round four has not been finished, only written. The default schedule below is one full ten-operation round per numbered item:

1. Baseline: re-ground the tool, surrounding docs, and acceptance material; write the first full draft with all required sections; measure; record `baseline`.
2. Open Questions pass: every question a builder would ask is present, ends with `?`, and carries a best-supported assumption with named evidence.
3. Approaches pass: each option gets its own named subsection with an explicit pros side and an explicit cons side, and rejected options are recorded.
4. Recommendation pass: one approach named, justified in at least forty measured characters, with the tradeoff that made it the pick stated.
5. Claim audit pass: every factual claim about the current tool re-checked line by line against the source on disk; the claim register is corrected in this round.
6. Background and Constraints pass: the observations from the grounding passes are in the document, and each ground rule from the request is stated as a constraint and re-verified.
7. Builder check round: read the document as the builder who must plan from it without access to you.
8. Builder-check repair round: apply the edits the builder check produced, one section, then re-measure the whole file.
9. Second builder check round: run the builder check again after the document is close enough to final that the remaining questions are the expensive ones.
10. Second builder-check repair round: apply only one edit from the second builder check, then read the whole file back.
11. Compliance sweep round: every threshold gets a measured value, recorded in the row.
12. Claim register sweep round: every claim in the register is re-verified individually against the source and surrounding docs.
13. Convergence round: all measurements equal the previous round's, all rules pass, deltas are empty or explicitly "unchanged with value", and the scope audit is clean.
14. Confirmation round: one further full read from disk reproduces the convergence numbers, recorded as its own row.

Any round that ends with a non-empty diff, a rule failure, a claim failure, a scope-integrity failure, or a builder-check pile extends the schedule by however many rounds the fix needs, one section at a time. The loop runs until a round produces no differences at all and the confirmation round agrees with it.

**Safety valve.** The process ends no later than the end of round sixteen. If a difference still exists at that point, record it honestly in the last row as a residual difference with its measured value, state in the final message that it is unresolved, and deliver. An honest unresolved row beats an invented convergence.

## Convergence

You are done when a full round measures every rule as passing, every measurement equals the previous round's, and one further confirmation read from disk reproduces those same numbers. Record the confirmation round in the ledger too; a convergence you did not re-read is a feeling.

If the confirmation read shows any difference, the loop restarts: fix, read back, diff, record, verify the record, scope audit, and find a new convergence round. A changed heading order, changed item count, changed hash, changed test count, changed line-range citation, or changed ledger row is a difference. Write it. Do not hide it in prose.

## Builder Check

Read the document as the builder who has to plan from it without access to you, on a fresh read of the file, and sort what they would ask into three piles:

- **Answered already**: put the answer in the document where the builder will find it, not where you found it.
- **Minor**: settle it yourself and mark it as your call.
- **Theirs**: record it in Open Questions with your best-supported assumption if no one is available to answer.

Run the piles in order, and take them seriously. A builder's guess about ordering, window bounds, defaults, output destination, empty-case behavior, escaping, file paths, or failure modes is exactly the kind of decision that looks obvious and is not. Each of the three piles produces edits, and **each edit starts a new round** unless several edits are inseparable inside one section. Do not batch three pile edits into one round unless they are inside one section and cannot be separated.

Run the builder check at least twice for a document of this size: once after the sections exist, schedule round seven, and once after the first compliance pass, schedule round nine. The second run gets its own repair round, schedule round ten.

## Measurements

Take all of these from the read-back in step six on every round, and write the values into the ledger row. They are cheap, and "cheap" is why there is no excuse for skipping them. A round that skips a measurement is a round that did not happen; take it again.

- Bytes, lines, and words in the deliverable as it now exists.
- The heading inventory: every heading, in the order it appears, spelled exactly as it appears on disk.
- The required headings, each marked present or missing, case-insensitive: Background, Goals, Constraints, Open Questions, Approaches, Recommendation.
- Item count under each list-bearing section: Goals, Constraints, Open Questions, Approaches.
- For Open Questions, whether every item ends with a question mark, and the count of items that do not.
- For Approaches, the number of distinct options, and whether each one has both an explicit pros side and an explicit cons side, stated as separate labeled lists.
- The character length of the Recommendation text, measured, not eyeballed, and its word count.
- Word count of each required section, so a section that silently shrank is visible.
- Claim register length: number of claims, number of claims re-verified this round, number of claims whose source line ranges changed, number of failed claims.
- Whether every factual claim about the current tool is still findable in the source on disk: re-check identifiers, command names, subcommand spellings, file paths, field names, ordering behavior, defaults, output behavior, empty-case behavior, and error behavior one by one.
- Whether the source files you were told not to touch are untouched, by hash and byte count, not by belief.
- Whether README, docs, tests, or other supplied acceptance material are untouched when the request forbids changes.
- Whether supplied tests were read, run when permitted, and what their pass count and fail count were.
- Whether the workspace contains any file you did not intend to create, listed from a fresh directory listing.
- Whether the deliverable contains any code block, fenced code, function body, command implementation, shell snippet, diff, or patch, which it must not contain when the task forbids code.
- The ledger's own shape: number of rows, number of columns per row, whether any row is missing a column, whether any row uses "same as above" or ellipses, and whether the final two rows prove convergence and confirmation.
- The delta inventory: every changed measurement, every unchanged measurement, and a short prose sentence for each change or non-change.

Every number in a row is paired with the number from the previous row and the arithmetic difference. "3 (was 3, delta 0)" is a measurement. "3" alone is not enough to show drift, and "unchanged" without the previous number is not allowed.

## Claim Register

Somewhere in the document, in the ledger section, keep a register of every factual claim the design makes about the tool as it exists today: what the file does, what it does not do, what it calls things, where things live, what the README asserts, what tests imply, what defaults appear, and what output destination is current. One line per claim:

`C1: the CLI has three subcommands and nothing sorts the store - re-read at lines 24-58, holds (R3, R5, R8, R13)`

Re-verify the whole register on every round, one claim at a time, against the source on disk, and append the round numbers where it held. A claim that fails is not deleted quietly: it becomes the single fix for the next round, and the row says so. A claim about the tool that the source cannot support is the most damaging thing a design document can contain, because the builder will trust it.

Correct the record when the ground disagrees with the README or with your own earlier reading. A contradiction you found is a finding, and it belongs in Background, not in a footnote you hope no one reads.

The claim register is not optional background. It is a measured object. Each round records its length, its verified count, its failed count, and whether any line ranges moved because the document or source changed.

## Ledger

Append the ledger once per round, in the deliverable, after the required sections, under a clearly labeled process heading such as `## Verification Rounds`. It is a record of work, not new design content: it never changes, renames, or removes a required section, and it never adds claims about what should be built unless those claims are observations about the verification process.

One row per round:

| Round | Operations | Re-grounded observation | Measurements current vs previous vs delta | Delta prose | Claim register result | Scope and tests result | Rule failures | Fix for next round |
|-------|------------|--------------------------|--------------------------------------------|-------------|------------------------|-------------------------|---------------|--------------------|

Rules for the ledger:

- Round one's delta column says `baseline`. It never says baseline again, and no later round may copy round one's numbers forward.
- Write one row per round. A row summarizing three rounds is three missing rows.
- The Operations column lists the actual file and shell operations the round performed: source read, docs read, tests read or run, deliverable read, one content edit, full read back, diff composition, row append, verification read, scope audit.
- The Delta column lists every changed number and every changed heading or item, plus at least one sentence of prose about what moved and why, even when nothing moved. "No deltas; all counts identical to the previous round" is a valid and required entry for a convergence round only when the values are included.
- Reproduce the previous round's key measurements inside the current row, taken from re-reading the row, not from memory: the file cannot diff against a number you did not carry forward.
- No abbreviations, no `same as above`, no ellipses, no placeholder text standing in for a value. A later reader must be able to diff any two rows without consulting anything else.
- The Rule-failures column is filled in even when it is empty; write `none observed` rather than leaving it blank, so a blank cannot be confused with a skipped check.
- The Fix-for-next-round column is filled in even when it is empty; write `none needed` and then still run the next mandatory round.
- Keep it inside the workspace and inside the deliverable. No helper scripts, no sidecar ledger file, no generated code, no edits to the tool under discussion. The ledger lives in the document precisely so every future read-back must read it again.
- Once written, the ledger is verified like everything else: it is part of the file you read back in step six and step nine, and its own counts and wording are part of the diff.

## Scope Integrity

For every deliverable, the request's prohibitions are measurements. On every round, from the shell or available file tool, take and record:

- A hash of each file you were told not to modify, plus its byte count, compared with the value from your first read of it.
- A hash and byte count for README, docs, tests, or other supplied material when they are part of the acceptance surface and must not change.
- A listing of the workspace, compared against the set of paths you have deliberately created, so an accidental file is caught in the round that made it.
- A check that the test files are as supplied and still pass, if tests exist and the task allows running them.
- A count of code blocks or fenced snippets in the deliverable when the task forbids code; the expected value is zero.

Report these as values in the row: the hash prefix, the byte count, the pass count, the fail count, the workspace file count, and the code-block count. "I did not modify it" is a claim; the hash is the measurement. If a hash differs, stop writing sections: restoring the source is the single fix for the next round, and the row records the failure. If a workspace listing reveals a file you accidentally created, record it; if it is clearly a scratch file you created and no other instruction forbids removing it, remove it in a separate operation and verify the listing again in the next round. Do not delete supplied files.

## Compliance Sweep

Right before you call the document done, run this as its own round, against the file on disk and not against your draft:

| Rule | Pass threshold |
|------|----------------|
| Required headings present, in order, case-insensitive | Background, Goals, Constraints, Open Questions, Approaches, Recommendation |
| Goals | 3 or more items |
| Constraints | 2 or more items |
| Open Questions | 3 or more items, every one ending in `?` |
| Approaches | 2 or more distinct options, each with explicit pros **and** cons |
| Recommendation | names one chosen approach and justifies it, 40 characters or more |
| Claim register | every claim re-verified on disk this round |
| Scope | source untouched by hash, no code written, deliverable is the document |
| Tests | supplied tests unmodified; run status recorded when permitted |
| Ledger | one row per round run, no blank failure or fix cells |

Every threshold gets a measured value in the round it is checked, written into that round's row: the actual count, the actual character length, the actual hash prefix, the actual pass count. "Looks fine" is not a value. If a threshold fails, that failure is the single fix for the next round, and the next round is not allowed to assume the fix worked until it reads the file.

## Process

**Where it goes:** the path the task names. If the task names `docs/brainstorm-design.md`, that is the path, with the required headings in the required order, and the ledger after them. If nothing is named, a software repo puts design work under `docs/`; otherwise ask, and if there is no one to ask, choose a plain path inside the workspace and record the choice. Create the directory with the first write, not with a scratch file.

**Order of operations, every time, without exception:** source read, docs read, tests read or run, deliverable read, write one fix, full read back, measure, diff, append row, verify read, scope audit. Repeat.

**Editing discipline.** One section per round once the draft exists: change one thing, read it back, measure it, and record whether the change did what you intended. Multi-section rewrites are allowed, but they still get one read back, one diff, and one full row, and they still count as one round with one fix. Never restructure required headings while editing: counts move when you are not looking, and the ledger is where you catch that.

**No sidecar files.** The deliverable plus nothing else. No scratch notes, no measurement scripts, no intermediate drafts in separate paths. Every draft you keep in another file is a file that future rounds must also re-read, and it is not what was asked for.

**Sizing.** A small change gets a short doc; a project gets the full one. The loop is the same size either way. If the work grows mid-task, say so and step up a size, and let the next round re-measure the whole file rather than the part you touched.

**Effort accounting.** Each round costs roughly three full reads of the deliverable, several full reads of source material, one content write, one record write, and a scope audit. It buys facts. Budget for that and do not be surprised by it. The read count is the cost of not shipping a wrong design, which is the expensive outcome. If you find yourself trying to save rounds, you are choosing the cheaper failure.

## Red Flags

| Thought | Reality |
|---------|---------|
| "I will fill in sensible defaults" | Good. Say them out loud, in the doc, as your assumption, and register the claim. |
| "I have already read the file, so I know what is in it" | You know what was in it. The round starts with a new read. |
| "The counts obviously satisfy the rules, no need to measure" | Obvious claims are the cheapest ones to verify and the most expensive ones to get wrong. |
| "I can copy last round's numbers, nothing changed" | Then say nothing changed, in a row that came from a read, with the numbers shown. |
| "One careful pass is enough" | One pass has no baseline. The loop needs fourteen rounds to tell drift from stability. |
| "Thirteen rounds is plenty, fourteen is ceremony" | Round fourteen is the confirmation that the convergence round was real. |
| "I fixed it, so it is fixed" | The fix belongs to the round that reads it back. |
| "This edit is tiny, I will write and re-write without reading" | Every write is followed by a read before another write. |
| "The row is boring, I will summarize three rounds into one" | Three missing rows. Write them. |
| "The ledger is noise, readers skip it" | The ledger is the evidence. It is read back and diffed like everything else. |
| "grep the headings instead of reading the file" | A grep is not a read; a read is what produces the other numbers. |
| "The requester said nothing, so I will skip Open Questions" | Silence is exactly why the section exists. Ask it in the doc. |
| "I will draft code in the doc to make the approach clearer" | No code. Describe the shape in words. |
| "The diff is empty, I am done" | Confirm with one more read that the empty diff is real, and row it. |
| "Rounds are overhead; the document is what ships" | The rounds are how you know the document says what you meant it to say. |

<HARD-GATE>
Nothing gets built until the design document is approved or approval is recorded as unavailable, and the file-io loop has converged: the short one for a small change, the full one for a project. Building includes writing product code, scaffolding, installing dependencies, creating projects, and invoking an implementation skill. Reading and exploring are fine, and in this skill reading is the work.

Two exceptions. If the requester opted out of the questions, the skill is done and the approval gate goes with it: the document records the questions and the assumptions, and the loop still runs to convergence, for at least the fourteen scheduled rounds, before anything is delivered. A spike they said yes to may be built; it stays labeled throwaway, and keeping what it produced is a new request that comes back through this gate.

The gate closes only on evidence: a final convergence ledger row, from a fresh read of the file, showing every compliance rule passing with its measured value and the diff empty or explicitly unchanged with previous values; followed by one confirmation row whose numbers match it; followed by a scope audit showing protected files unchanged by hash and byte count, no unintended workspace files, no forbidden code, and test status recorded when tests were permitted to run. If you cannot point at those rows and values, the document is not finished, however confident you feel.
</HARD-GATE>

## Visual Companion

A browser tab for mockups, diagrams, and prototypes is available only when the environment has one and a human partner can respond. It is a tool, not a mode. Offer it just-in-time, the first time seeing would help more than reading, as its own message with nothing else in it: "This might be easier if I show you. Want me to open a browser tab with some mockups?" If they decline, stay in text and do not offer again unless they raise it. Requirements, scope, tradeoffs, and conceptual choices stay in text. If the requester is absent or the environment has no browser, there is nothing to offer; describe in words and put the detail in the document instead.

## The Point

The loop is not bureaucracy. It is the part of brainstorming where you find out whether what you wrote is what you meant, and whether what you meant is what the tool actually needs. Each round costs reads, writes, hashes, inventories, and row verification, and buys facts you did not have before: a count that moved, a claim that failed, a question you had not thought to ask, a heading that silently lost a word, a hash that stayed stable, a test that kept passing, a workspace file that should not exist.

A document that survives fourteen rounds of being read back, with every number re-taken from disk and every difference written down, is a document someone can build from. The ledger is how they know it was.

## Final Response

After the loop finishes, the final response must not be only "done." It must include:

- The deliverable path.
- A short paragraph stating what was grounded and what was not implemented.
- The final convergence values for required headings, Goals, Constraints, Open Questions, Approaches, Recommendation characters, claim register count, protected-file hash prefix, workspace file count, code-block count, and test status if available.
- The confirmation row result, including whether its values matched the convergence row.
- Any residual difference from the safety valve, if present, with its measured value and no softening language.
