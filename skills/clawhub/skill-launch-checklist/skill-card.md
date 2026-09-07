## Description:

Skill Launch Checklist is a pre-publish checklist for ClawHub skills that reviews title, summary, categorization, examples, versioning, dry-run readiness, and public page credibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub skill creators and developers use this skill before publishing to check release metadata, storefront readiness, examples, versioning, and dry-run prerequisites. It helps decide whether a skill release is ready to publish, close but incomplete, or should wait.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested publish commands could be mistaken for completed dry-run or release results.

Mitigation: Treat the output as review guidance and run the shown dry-run publish command yourself before releasing.

Risk: The skill declares a dependency on the clawhub CLI.

Mitigation: Verify the clawhub CLI package through your normal package-trust process before installing or running it.

Risk: Checklist advice may miss deeper release, registry, or positioning issues.

Mitigation: Use the checklist as a pre-publish pass and switch to a deeper audit or troubleshooting skill when it identifies unresolved quality, Actions, registry, or positioning concerns.

## Reference(s):

- [Launch checklist reference](references/launch_checklist.md)
- [Launch readiness comparison example](examples/launch_ready_vs_rushed.md)
- [Launch review template](templates/launch_review.md)
- [OpenClaw publisher homepage](https://github.com/bonniegeng-max/openclaw-publisher)
- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/skill-launch-checklist)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown checklist or review with optional shell command block]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a launch conclusion, blockers, missing items, minimal fixes, and a dry-run ClawHub publish command.]

## Skill Version(s):

1.0.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
