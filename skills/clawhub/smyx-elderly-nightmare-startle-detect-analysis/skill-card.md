## Description:

Analyzes fixed-camera nighttime sleep audio/video for sudden sitting up, screams, arm thrashing, and related events, then reports event timing, frequency, duration, risk signals, and caregiver-oriented next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, elder-care teams, and developers use this skill to analyze consented nighttime bedroom audio/video for observable sleep events and generate structured, non-diagnostic reports that can support care review or specialist follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Highly sensitive bedroom audio/video or video URLs may be sent to configured lifeemergence.com cloud services.

Mitigation: Use only with explicit consent from the elderly person, confirm that cloud processing is acceptable, and prefer minimized event clips or privacy-preserving modes when available.

Risk: The skill may create or reuse a persistent local identity and store service tokens in a workspace SQLite database.

Mitigation: Run in an isolated workspace, review generated local state before reuse, and remove persisted identity or token data when it is no longer needed.

Risk: Broad history-query phrases can retrieve cloud-stored analysis reports.

Mitigation: Use history-query wording only when report retrieval is intended, and review returned report links before sharing them.

Risk: Sleep event classifications and risk signals could be mistaken for medical diagnosis.

Mitigation: Present outputs as observable behavior statistics and care-review guidance only; defer diagnosis, medication changes, and treatment decisions to qualified clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured text, Markdown tables, and JSON report fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event timelines, frequency statistics, sleep-continuity scores, risk signal levels, report links, and specialist follow-up suggestions.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter and changelog mention 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
