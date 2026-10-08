## Description:

Helps agents plan and route YottaMeta skill combinations, inventory installed skills, and manage installation, updates, and local Hub distribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to select and route related skills, inspect local installations, and manage skill installation and distribution across supported agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install, link, and remove actions change local agent skill files and state.

Mitigation: Review dry-runs before acting and confirm the destination and proposed changes.

Risk: Skipping the install scan removes an intended safety check.

Mitigation: Avoid --skip-scan except for emergencies.

Risk: Configured providers and package lifecycle scripts can run trusted local code.

Mitigation: Use trusted providers and installation sources; prefer OpenClaw's official install/update path or an exact pinned npm version.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Project homepage (listed in release metadata)](https://github.com/YottaMeta/yotta-skills)
- [Skill orchestration guide](references/orchestration.md)
- [Local Hub guide](references/hub.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance and command examples; optional structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routing suggestions do not automatically install skills.]

## Skill Version(s):

0.29.7 (source: ClawHub release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
