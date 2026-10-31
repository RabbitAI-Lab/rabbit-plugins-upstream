## Description:

Randomly generate a one-week menu from a self-contained dish library, with optional reproducibility through a seed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

People planning everyday meals can generate a week of breakfast, lunch, and dinner ideas from the bundled dish library, with a seed available to reproduce a menu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writing a menu with --output can overwrite an existing file at the chosen path.

Mitigation: Check the destination path before running the command and choose a new path when you need to preserve an existing file.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-weekly-menu)
- [Publisher profile](https://clawhub.ai/user/wlc-dev)
- [Usage Guide](artifact/references/usage-guide.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [A weekly meal plan as Markdown, plain text, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Day count, meal slots, random seed, repeat handling, dish library, and optional output file can be selected.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
