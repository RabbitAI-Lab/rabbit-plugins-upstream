## Description:

YuanShou is a zero-dependency pre-publish release guard for yotta skills that checks readiness, package contents, version alignment, name availability, and publish command plans before GitHub, npm, or ClawHub release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and release maintainers use this skill to ask an agent for pre-publish checks and command plans for yotta skill releases across GitHub, npm, and ClawHub. The skill supports human review by reporting readiness, package, version, name, and publish-plan findings without making the final publish decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publish command can perform external publishing actions when the user explicitly enables exec mode.

Mitigation: Review the dry-run command plan, confirm the target directory and authenticated GitHub/npm/ClawHub accounts, and use --exec only after human approval.

Risk: Global installation can make the skill available to multiple agents.

Mitigation: Use an agent-specific or explicit install directory unless multi-agent availability is intentional.

Risk: Network or CLI availability can prevent definitive name checks.

Mitigation: Treat UNKNOWN name-check results as requiring manual verification before publishing.

## Reference(s):

- [Check Items](references/check-items.md)
- [Publish Flow](references/publish-flow.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with command examples, release check summaries, and dry-run publish plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exit-code guidance, explicit blocking reasons, and manual follow-up checks when network tools are unavailable.]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
