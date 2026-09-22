## Description:

Helps users build a personal music system for discovering music, organizing favorites, tracking concerts, and preserving listening memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to organize personal music discovery, favorites, concert tracking, and listening-memory workflows through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command-execution authority without clear music-specific limits.

Mitigation: Constrain tool permissions, review proposed commands and file changes before they run, and install only in a sandboxed agent environment.

Risk: The skill may involve API keys, external service calls, or user music-related data.

Mitigation: Verify API key handling, avoid exposing credentials in logs or version control, and review external calls before sharing personal data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/music)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, JSON, text]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file, command, API, and workflow actions that should be reviewed before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
