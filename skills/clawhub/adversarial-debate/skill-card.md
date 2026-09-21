## Description:

Runs a cross-vendor adversarial review of a plan, proposal, or design, with explicit user consent before sending briefs or approved source excerpts to another vendor's model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and reviewers use this skill to send a scoped proposal or design to an external model for adversarial critique, then classify the outcome into disputed, unresolved, and verified-consensus items. It is intended only when the user explicitly asks for cross-vendor review and approves any source material shared with another vendor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Briefs and approved source excerpts are sent to another model vendor and may remain in that provider's session history under its retention terms.

Mitigation: Keep the default brief-only mode for sensitive work, share only explicitly approved minimal excerpts, and redact secrets or personal data before transfer.

Risk: Attached source files can disclose more than the review brief if the staged material is too broad.

Mitigation: Confirm every file per debate, stage only throwaway copies, resolve paths inside the project root, scan staged copies before sending, and record which files were shared.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with optional shell command blocks and structured debate categories]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include attack findings, defense rulings with evidence tags, final-round categories, fresh-judge findings when triggered, and proposed handoff destinations that require user confirmation before recording.]

## Skill Version(s):

2.4.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
