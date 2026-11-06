## Description:

Randomly generates a weekly menu from a self-contained dish library and prints it as Markdown, plain text, or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

People planning everyday meals can use this skill to generate a varied week of breakfast, lunch, and dinner choices. A seed can be supplied to reproduce the same menu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writing to an existing --output destination replaces that file.

Mitigation: Choose a new output path or confirm the destination file before generating the menu.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-weekly-menu)
- [Publisher profile](https://clawhub.ai/user/wlc-dev)

## Skill Output:

**Output Type(s):** [Markdown, Plain text, JSON]

**Output Format:** [A weekly meal plan with one dish for each selected meal and day]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to seven days with breakfast, lunch, and dinner. An optional seed makes the result reproducible; repeated dishes within a meal slot are avoided when the dish pool allows.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
