## Description:

Security checkup for this agent. Scores the machine 0-100 (exposed gateway, plaintext secrets, risky skills and MCP servers, broad tool scopes) and gives exact fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[securemyagent](https://clawhub.ai/user/securemyagent)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and developers use this skill to check an agent environment for security issues, review risky skills or MCP servers, and get remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The weekly workflow calls for uploading security findings without first confirming that reporting was opted into.

Mitigation: Keep checks local by omitting --upload unless the user explicitly opts into external reporting; explain that uploaded reports include security metadata and identity score/status can be publicly checked.

Risk: Fix commands and installing the persistent Guard hook can change the user's machine settings.

Mitigation: Show the proposed changes and get the user's approval before running fixes or installing the Guard hook.

## Reference(s):

- [SecureMyAgent](https://securemyagent.ai)
- [SecureMyAgent documentation](https://securemyagent.ai/docs)
- [Guard documentation](https://securemyagent.ai/docs/guard)
- [Security reporting](https://securemyagent.ai/security)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown report or JSON, with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Security score from 0-100, findings, and suggested fixes]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
