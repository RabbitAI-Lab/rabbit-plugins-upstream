## Description:

Ontario Immigration Expert helps agents check official Ontario immigration sources, monitor policy updates, and calculate itemized OINP Ontario Workforce Priority and Sudbury RCIP/FCIP scoring for candidate profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[forrest-tech](https://clawhub.ai/user/forrest-tech)

### License/Terms of Use:

MIT

## Use Case:

External users and immigration support teams use this skill to evaluate candidate profiles against Ontario Workforce Priority and Sudbury RCIP/FCIP pathways, including eligibility gates, itemized EOI scoring, and update monitoring. Its outputs are reference material only and should be checked against official provincial sources before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scores or eligibility guidance may become stale because the skill combines live-policy claims with offline snapshot-based scoring.

Mitigation: Require a fresh check of the cited official Ontario and Sudbury sources before relying on any score, eligibility gate, or pathway recommendation.

Risk: Immigration outputs may be mistaken for authoritative legal advice or a government decision.

Mitigation: Present outputs as reference guidance only and defer final interpretation to official provincial sources or qualified immigration counsel.

Risk: Network behavior and monitoring claims may not match the local scorer's offline behavior.

Mitigation: Review the skill before installation and treat local scripts as reference calculators unless the agent has explicitly fetched and compared current official policy text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/forrest-tech/skills/ontario-immigration-expert)
- [Ontario Workforce Priority Stream](https://www.ontario.ca/page/ontario-workforce-priority-stream)
- [OINP 2026 updates](https://www.ontario.ca/page/2026-ontario-immigrant-nominee-program-updates)
- [O. Reg. 422/17](https://www.ontario.ca/laws/regulation/170422)
- [Sudbury RCIP/FCIP](https://investsudbury.ca/why-sudbury/newcomers/rcipfcip/)
- [Official OINP snapshot](data/snapshots/oinp-workforce-priority-OFFICIAL.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown reports with scoring tables, eligibility notes, local command examples, and JSON-profile-driven scoring output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses candidate profile JSON and cited official policy sources; results should be treated as reference guidance, not legal advice.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
