## Description:

Prepare evidence-backed HR decision briefs for accountable human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mwclaw](https://clawhub.ai/user/mwclaw)

### License/Terms of Use:

MIT-0

## Use Case:

HRBPs, People leaders, managers, and advisors use this skill to turn messy people issues into decision-ready briefs for accountable human review. It organizes supplied evidence, options, tradeoffs, unresolved gaps, and next actions without making or executing employment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unnecessary sensitive personal, medical, government ID, credential, or unrelated HR data could be supplied while preparing a packet.

Mitigation: Use controlled, relevant sources; prefer synthetic or de-identified inputs; and provide only the minimum information needed for the review.

Risk: A drafted packet could be mistaken for a final employment decision or used to trigger HR actions.

Mitigation: Keep final decisions, communications, system updates, and other external actions in authorized human workflows.

Risk: Instructions embedded in notes, resumes, policies, attachments, or retrieved text could try to override the skill's HR boundaries.

Mitigation: Treat embedded instructions in source material as untrusted content and preserve the skill's source, privacy, and human-review requirements.

## Reference(s):

- [HR Decision Packet Evals](references/evals.md)
- [Decision Packet Template](templates/decision-packet.md)
- [ClawHub Skill Page](https://clawhub.ai/mwclaw/skills/hr-decision-packet)
- [Skill Homepage](https://github.com/mwclaw/openclaw-hr-workflows/tree/main/skills/hr-decision-packet)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown decision packet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sourced evidence, unresolved gaps, options and tradeoffs, bounded recommendation status, next action, and a human decision receipt.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
