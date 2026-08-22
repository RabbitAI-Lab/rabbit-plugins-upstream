## Description:

RecallBase helps an agent recover context from local AI conversation history for same-day summaries, session resumption, and tracing past decisions to supporting history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[darinrowe](https://clawhub.ai/user/darinrowe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to query local RecallBase history, summarize recent work, resume prior coding or AI sessions, and identify the evidence behind earlier decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query local AI conversation history, which may include sensitive or private context.

Mitigation: Keep requests specific, summarize only the relevant evidence, and avoid exposing raw transcripts, secrets, local paths, tokens, cookies, headers, clipboard contents, or full URL queries.

Risk: Imports, package installation, and browser native-host setup can change local user configuration.

Mitigation: Require explicit user approval before running imports, installing packages, or configuring browser native-host support.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/DarinRowe/RecallBase/tree/main/skills/recallbase)
- [RecallBase ClawHub listing](https://clawhub.ai/darinrowe/skills/recallbase)
- [Local MCP](references/mcp.md)
- [Result reference](references/results.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON references when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should summarize retrieved history instead of reproducing full transcripts or raw JSON.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
