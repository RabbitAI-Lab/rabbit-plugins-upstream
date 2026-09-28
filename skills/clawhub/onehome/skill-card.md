## Description:

Helps agents search private OneHome real-estate listings, retrieve property details and photos, compare homes, and estimate housing costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers with access to an agent-shared OneHome portal use this skill to find and compare listings, inspect photos and nearby schools, and estimate mortgage payments or affordability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome magic links, bearer tokens, and captured sessions grant access to private portal data.

Mitigation: Treat access credentials like passwords; do not share them in public chats, logs, or shared outputs, and prefer scoped environment variables when possible.

## Reference(s):

- [onehome on ClawHub](https://clawhub.ai/chrischall/skills/onehome)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include private listing information and locally calculated mortgage or affordability estimates.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
