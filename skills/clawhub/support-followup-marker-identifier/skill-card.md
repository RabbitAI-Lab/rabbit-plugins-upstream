## Description:

Prepare a structured support intake digest from a supplied support snippet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and agents use this skill to turn a supplied intake message into a case ID, priority, subject, and follow-up category for triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support snippets may contain information the user did not intend to process.

Mitigation: Use only support-intake text the user intends to provide; do not supply credentials or private files.

Risk: Field and keyword classification may not reflect the intended priority or follow-up category.

Mitigation: Review the extracted case details and category before using them for triage.

## Reference(s):

- [Support Intake Digest on ClawHub](https://clawhub.ai/wxt-ai/skills/support-followup-marker-identifier)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [JSON object containing support_digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The digest contains case_id, priority, subject, and follow_up_category; it does not create a support ticket.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
