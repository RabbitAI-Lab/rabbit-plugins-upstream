## Description:

Sets handling guidance for a content item and prepares a content review plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content reviewers and teams use this skill to set guidance from a supplied content profile and prepare a review plan from that guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive content in a request may be processed and written to a local review-plan file.

Mitigation: Only submit content intended for review and choose an appropriate, access-controlled output directory.

Risk: Running the skill executes local Python code.

Mitigation: Review the packaged code before execution and run it only in an environment you trust.

## Reference(s):

- [Content Review Handling Desk release](https://clawhub.ai/wxt-ai/skills/content-review-handling-desk)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Handling guidance as text; review plan as JSON and a local CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream step writes a review-plan CSV in the user-selected output directory.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
