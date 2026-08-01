# Risks & save-the-show plays

Load before tech rehearsal, on show day, or whenever an executive says "what if X happens?"

The job isn't to prevent every risk — it's to know which risks matter, prevent the preventable ones, and have a decisive play ready for the rest.

## Risk register format

For each risk, document: trigger, likelihood, impact, prevention, owner, and the save-the-show play.

## The catalog

### Demo failure
- **Trigger:** Network drop, latency spike, login issue, model nondeterminism, UI regression, dependency outage.
- **Likelihood:** High. Always assume it.
- **Impact:** Catastrophic for the moment; recoverable with a good play.
- **Prevention:** Happy path lock 72h pre-show. Reset script. Caged network. Wired backup. Pre-recorded backup of the exact same demo. Failover operator on comms.
- **Save:** Cut to backup recording. Speaker continues as if planned. Never apologize for "technical difficulties" — narrate over it. If recording also fails, narrate the outcome and move on.

### Speaker freeze
- **Trigger:** Memory blank, prompter scroll error, unfamiliar audience, nerves.
- **Likelihood:** Medium for inexperienced speakers; low for veterans.
- **Impact:** Audience awareness builds with every second of silence.
- **Prevention:** Multiple rehearsals. Confidence monitor with current bullet. Paper script in podium. Pre-agreed silent cue from producer = "skip to next beat."
- **Save:** Show caller cues prompter back. If freeze persists 5+ seconds, jump to next slide / video / demo. Co-host or off-stage voice bridges. After event, never single out the speaker in debrief documents.

### Slide misorder / wrong file
- **Trigger:** Version control failure, last-minute swap, duplicate filenames.
- **Likelihood:** Medium with weak version control.
- **Impact:** Confidence-shaking but survivable.
- **Prevention:** Single source of truth. Filename convention with date + version. Lock check at dress. Operator has the final master only.
- **Save:** Speaker pauses, says "let me come back to that." Show caller advances to next ready slide. Cue-to-cue resumes when corrected.

### Technical outage (playback, monitor, comms)
- **Trigger:** Hardware failure, signal drop, software crash, power.
- **Likelihood:** Low with proper redundancy; high without.
- **Impact:** Show-stopping if redundancy isn't designed in.
- **Prevention:** Two of everything critical (playback, prompter, mic, comms). Spare machines hot. Rehearse under load. Printed scripts in wing. Comms map.
- **Save:** Hot-swap to backup. Camera-only speech mode. Host vamps. B-roll delay package. Stage manager moves to plan B blocking.

### Breaking news during show
- **Trigger:** External event (market move, geopolitical event, tragedy, competitor announcement) lands during your keynote.
- **Likelihood:** Rare but real.
- **Impact:** Can make celebratory content feel tone-deaf.
- **Prevention:** Modular opening that can be swapped. Comms + legal on standby. Producer monitors news.
- **Save:** Producer + exec sponsor + comms huddle, decide whether to acknowledge, modify, or proceed. Shorter celebratory tone, updated CTA, prepared bridge language. Never ignore something the audience knows.

### Executive ego conflict
- **Trigger:** Two executives want the same moment, the same number, or veto each other.
- **Likelihood:** High at multi-speaker keynotes.
- **Impact:** Damages narrative coherence and team morale.
- **Prevention:** Pre-wired speaker map. Sponsor adjudication early. Document agreed handoffs.
- **Save:** Triangulate through Exec Comms / CMO sponsor. Never let the conflict reach the speaker on show day.

### Late executive script changes
- **Trigger:** Executive sees the final script the day before and rewrites their section.
- **Likelihood:** Very high.
- **Impact:** Cascades to slides, prompter, legal review, captioning, localization, demo setup.
- **Prevention:** Multiple rehearsals (so they're not seeing it fresh on day-of). Lock discipline. A clear "what late changes cost" cheat sheet for the exec sponsor.
- **Save:** Producer triages: accept (if low-risk and high-value), defer (if too late), or counter-propose (if intent is good but execution wrong). Document trade-offs to the sponsor.

### Legal / PR landmine
- **Trigger:** A claim, a competitive callout, an unapproved customer story, an unreleased feature mention, a forward-looking statement without safe-harbor language.
- **Likelihood:** Medium without disciplined review.
- **Impact:** Press cycles, regulatory exposure, customer trust damage.
- **Prevention:** Hard legal/PR/IR gate at T-minus 3 weeks. No claims enter the script without source attribution. Customer permissions in writing.
- **Save:** Pull the moment. Rewrite the bridge. If discovered post-show, coordinate corrected communication immediately.

### Demo "concept" vs. "real" mismatch
- **Trigger:** Marketing wants to show a feature that engineering hasn't built yet.
- **Likelihood:** High at product launches.
- **Impact:** Reputation damage if presented as live.
- **Prevention:** Clear labeling: "live demo" vs. "concept render" vs. "feature in development." Engineering signs off on demo claims.
- **Save:** Reposition framing on the fly. "Here's where we're headed" beats "here's what we have."

### Music / IP rights failure
- **Trigger:** Walk-on music, video soundtrack, or stock visual not properly licensed for live + stream + on-demand.
- **Likelihood:** Medium without rights audit.
- **Impact:** Stream takedown, lawsuit, brand damage.
- **Prevention:** Music supervisor or legal review of every audio cue. Licensed library default.
- **Save:** Swap to library cue. Acknowledge in post-event if needed.

### Captioning / accessibility failure
- **Trigger:** ASR mis-transcribes a key term, captioner falls behind, sign interpreter not in shot.
- **Likelihood:** Medium.
- **Impact:** Excludes audience segments; reputational risk.
- **Prevention:** Glossary for ASR. Human + AI captioning together. Pre-event walkthrough with interpreter.
- **Save:** Producer escalates to stream operator. Post-event, corrected captions on on-demand.

## The show-day mindset

When something breaks:

1. **Notice it before the audience does.** Producer's first job in the booth is situational awareness.
2. **Pick the play.** Don't deliberate. The play is in your risk register.
3. **Call it on comms.** One voice, clear and short. "Going to backup demo. Now."
4. **Brief the speaker between beats.** "We're going to backup, stay calm, you're great."
5. **Never apologize on stage.** The audience forgives what they don't notice. Narrate over the seam.
6. **Debrief after.** Document the trigger, the play, the outcome. Update the register.

## What separates senior producers

- They've been here before. The play is muscle memory.
- They make the call quickly and own it.
- They protect the speaker from blame.
- They debrief without theater — what failed, what to change, what to keep.
