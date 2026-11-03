## Description:

Checks skill release readiness, package contents, version alignment, and name availability, and prepares publishing commands for selected channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill before publishing a skill release to check its files, versions, and name availability, then prepare commands for GitHub, npm, or ClawHub. It supports release review but does not make the publishing decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The preview flag can be overridden, and unsafe command quoting can allow unintended commands.

Mitigation: Avoid automated publishing until these issues are fixed. Install a fixed, reviewed release; review ownership, channels, and staged files; independently check packaging and versions; inspect optional audit results; and confirm names manually after network failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-publish-guard)
- [Project homepage](https://github.com/YottaMeta/yotta-publish-guard)
- [Check items](artifact/references/check-items.md)
- [Publish flow](artifact/references/publish-flow.md)
- [Tutorial](artifact/references/tutorial.md)
- [FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Command-line reports and shell command plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports and command plans depend on the target skill and selected publishing channels.]

## Skill Version(s):

0.4.4 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
