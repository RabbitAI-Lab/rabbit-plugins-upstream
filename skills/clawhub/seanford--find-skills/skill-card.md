## Description:

Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to discover relevant installable agent skills, assess candidate quality, and optionally install selected skills with the Skills CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends unpinned remote CLI commands, which can change behavior between runs.

Mitigation: Use pinned CLI versions or reviewed package sources before running search, install, check, or update commands.

Risk: The skill includes a global install command with confirmation skipping, which can create persistent user-level changes.

Mitigation: Avoid `-g -y` unless the user explicitly accepts the persistent impact; inspect each target skill before installation or update.

Risk: Skill recommendations may point users to third-party packages with unknown source reputation.

Mitigation: Verify install counts, source reputation, repository signals, and skill contents before recommending or installing a candidate.

## Reference(s):

- [Find Skills on ClawHub](https://clawhub.ai/seanford/skills/find-skills)
- [seanford publisher profile](https://clawhub.ai/user/seanford)
- [Skills leaderboard](https://skills.sh/)
- [Example skills.sh skill page](https://skills.sh/vercel-labs/agent-skills/react-best-practices)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include skill recommendations, install commands, quality checks, and links to skill listings.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
