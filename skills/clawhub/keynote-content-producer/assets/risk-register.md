# Risk Register & Contingency Matrix

Maintain throughout the project. Review weekly in Phase 1–4, daily in Phase 5–6, every rehearsal in Phase 7.

---

**Event:** ________________ **Last updated:** ________________ **Owner:** Keynote producer

## Risk table

| # | Risk | Trigger | Likelihood (L/M/H) | Impact (L/M/H) | Score | Prevention | Owner | Save-the-show play | Status |
|---|---|---|---|---|---|---|---|---|---|
| R01 | Demo failure | Network drop, model error, login fail | H | H | 9 | Caged net, backup recording, failover op | Demo eng | Cut to DEMO_BACKUP_v2.mov; narrate over | Mitigated |
| R02 | Speaker freeze | Memory / prompter / nerves | M | M | 4 | Multi-rehearsal, confidence mon, paper script | Producer | Show caller cues prompter; jump to next beat after 5s | Mitigated |
| R03 | Wrong slide file | Version control miss | M | M | 4 | Filename convention, dress lock check | Tech dir | Operator advances; speaker pauses, says "let me come back to that" | Open |
| R04 | Playback outage | HW/SW failure | L | H | 6 | Hot-swap backup machine, B-roll loop | Tech dir | Hot-swap; host vamps if needed | Mitigated |
| R05 | Late exec script change | Exec sees script the day before | H | M | 6 | Multi-rehearsal; sponsor expectations set | Producer | Triage: accept / defer / counter-propose | Open |
| R06 | Legal / PR landmine | Unapproved claim, embargo break | M | H | 6 | T-3w legal review; no unsourced claims | Legal | Pull moment; rewrite bridge | Mitigated |
| R07 | Breaking news | External event during show | L | H | 6 | Modular opening, comms+legal standby | Producer | Sponsor huddle; modify open / tone / CTA | Open |
| R08 | Captioning failure | ASR errors on key term | M | M | 4 | Glossary preload, human captioner backup | Stream vendor | Producer escalates; correct on-demand later | Mitigated |
| R09 | Music IP issue | Unlicensed track for stream | L | H | 6 | Music supervisor review; library default | Music sup | Swap to licensed cue | Mitigated |
| R10 | Executive ego conflict | Two execs vie for same moment | M | M | 4 | Pre-wired speaker map, sponsor adjudication | Exec Comms | Triangulate via sponsor; never reaches stage | Mitigated |

## Score key
- **Score = Likelihood × Impact** (where L=1, M=2, H=3 → range 1–9)
- **Action thresholds:**
  - 1–2: Monitor
  - 3–4: Active mitigation plan
  - 5–6: Weekly review by producer
  - 7–9: Daily review by producer + sponsor

## Standing contingencies (always pre-built)
- **Delay package** — 2–10 min of branded loop content for unexpected start slip
- **Host vamp script** — 60–90 second bridge to fill any unexpected gap
- **B-roll loop** — generic visuals if a segment collapses
- **"Save the show" comms protocol** — one voice on comms, short clear calls

## Show-day risk runbook
1. Producer reviews top 5 risks at green room call (T-60 min)
2. Each owner confirms readiness verbally on comms
3. Backup files confirmed loaded
4. Producer confirms reset states (demo, captioning, stream)
5. Hard go / no-go decision at T-15 min
