## Description:

Drive a real iPhone through macOS iPhone Mirroring with the mirroir MCP tools: read the screen, tap, type, swipe, open apps, and replay skills. Use whenever a task needs the user's phone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jfarcand](https://clawhub.ai/user/jfarcand)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use mirroir to inspect and operate their own iPhone through macOS iPhone Mirroring when a task requires phone interaction. The skill requires consent before actions such as sending, buying, deleting, or changing a setting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Phone text and screenshots may expose personal or sensitive information to the agent.

Mitigation: Consider the agent's data handling before opening sensitive apps.

Risk: Actions affect the user's real phone, and saved replays can repeat actions.

Mitigation: Ask for consent before consequential actions and review saved replays before running them.

Risk: Setup uses a separately downloaded server whose full behavior is outside this verdict, and setup commands carry a dependency-update risk.

Mitigation: Install a reviewed, pinned server version and grant permissions only to the intended host app.

## Reference(s):

- [mirroir homepage](https://mirroir.dev)
- [mirroir onboarding guide](https://github.com/jfarcand/mirroir-mcp/blob/main/docs/onboarding.md)
- [ClawHub release page](https://clawhub.ai/jfarcand/skills/mirroir)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown instructions with shell command examples and MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise iPhone interaction guidance; no fixed output artifact.]

## Skill Version(s):

0.44.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
