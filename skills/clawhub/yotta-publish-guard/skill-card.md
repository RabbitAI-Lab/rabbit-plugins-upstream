## Description:

元守 yotta-publish-guard is a pre-publish release guard that helps agents check skill readiness, package contents, version alignment, name availability, and publish command plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill before publishing or updating agent skills to verify release readiness across validation, packaging, version alignment, name checks, and publish command planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Executing generated publish commands can affect GitHub, npm, or ClawHub releases when --exec is used.

Mitigation: Review the generated publish plan before execution and keep the default dry-run flow unless release changes are intended.

Risk: Using --force can bypass failed publish-readiness checks.

Mitigation: Avoid --force unless a reviewer has intentionally accepted the failed checks and documented the reason.

Risk: Installing through npx without a pinned version can pull a newer package than the reviewed release.

Mitigation: Pin the npm package version in higher-trust environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-publish-guard)
- [Project homepage](https://github.com/YottaMeta/yotta-publish-guard)
- [Check items](references/check-items.md)
- [Publish flow](references/publish-flow.md)
- [Tutorial](references/tutorial.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented guidance with shell commands and release-readiness reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run publishing is the default; command execution requires explicit user selection.]

## Skill Version(s):

0.4.2 (source: server release metadata, SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
