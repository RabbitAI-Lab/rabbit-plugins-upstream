## Description:

Set handling guidance for a content item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content reviewers and other users provide a content profile to receive a suggested handling tier and, when applicable, fields to mask.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the local helper on supplied content profiles may expose sensitive details in the request or produce guidance that needs review.

Mitigation: Provide only the necessary request JSON and review the returned handling tier before applying it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/content-review-mode-identifier)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON containing a handling_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The guidance names a handling tier and may list fields to mask.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
