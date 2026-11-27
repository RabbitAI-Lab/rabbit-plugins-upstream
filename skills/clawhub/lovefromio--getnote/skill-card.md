## Description:

Connects an authorized GetNote account through the official CLI to save, find, read, and organize notes and knowledge-base content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovefromio](https://clawhub.ai/user/lovefromio)

### License/Terms of Use:

MIT-0

## Use Case:

GetNote users can ask the agent in natural language to connect their account and save, search, read, and organize notes and knowledge-base items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may synchronize other Skills without clear separate authorization.

Mitigation: Review the synchronization scope and confirm changes to other Skills before running setup; skip setup when those changes are not intended.

Risk: A generic phrase may trigger the skill unexpectedly.

Mitigation: Use it for clear GetNote requests and confirm the intended action before changing account data.

## Reference(s):

- [GetNote on ClawHub](https://clawhub.ai/lovefromio/skills/getnote)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries, note titles and links, and plain-text status or guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses IDs and links returned by GetNote; requested actions can change account data, with confirmation required for sensitive operations.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
