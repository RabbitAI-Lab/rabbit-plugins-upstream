## Description:

Set handling guidance for a content item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and workflow operators use this skill to turn a supplied content profile into concise handling guidance for the current content item.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may include content profile details that are broader than needed for the handling decision.

Mitigation: Provide only the content profile fields needed for the current request and omit unrelated private data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/content-review-mode-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [String]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the handling_guidance field for the supplied content_profile.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
