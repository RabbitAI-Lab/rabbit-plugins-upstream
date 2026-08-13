## Description:

The ct-series total entry point helps clinical-development users answer methodology, design, compliance, QC, regulatory, statistics, tone, sample-size handoff, raw-data routing, and competitive-intelligence questions through local workflows and sibling clinical-trial skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, and medical students use this agent for conversational guidance across trial methodology, design, statistics, GCP, safety, regulatory, QC, writing tone, sample-size handoff, and competitive-intelligence routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive clinical-development prompts can be sent to a remote Coze service for non-simple questions.

Mitigation: Do not enter patient identifiers, unpublished trial details, sponsor confidential information, or regulated clinical-development material unless the deployment has approved that outbound processing.

Risk: A stable per-device query_origin can correlate requests from the same machine.

Mitigation: Use the skill only where stable per-device correlation is acceptable, or require a local-only mode before deployment.

Risk: Endpoint auto-approval reduces the user's runtime opportunity to review outbound processing.

Mitigation: Remove endpoint auto-approval or add an explicit consent gate for environments handling sensitive or regulated material.

Risk: Local memory behavior can retain operational preferences or context on the user's machine.

Mitigation: Disable silent memory promotion or review and clear local memory files according to the installing organization's data-handling policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Homepage](https://github.com/medstatstar/ct-advisor)
- [README](README.md)
- [Chinese README](README_zh-CN.md)
- [Workflow Steps](references/steps.md)
- [Reference Index](knowledge/reference-index.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown conversational answers with source labels, routing guidance, and occasional inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Simple questions can be answered locally; non-simple questions may use remote Coze refinement and sibling-skill outputs when available.]

## Skill Version(s):

0.9.60 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
