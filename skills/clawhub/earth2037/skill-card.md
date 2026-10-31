## Description:

Play Earth2037 using the current Account Center and bundled MCP/CLI. Inspect cities, buildings, heroes, tasks, troops and maps, then carry out player-authorized game actions. Use for Earth2037 registration, login and gameplay, not server administration or the Cocos editor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[windinwing](https://clawhub.ai/user/windinwing)

### License/Terms of Use:

MIT-0

## Use Case:

Earth2037 players use this skill to inspect their accounts, characters, cities, and game state, and to carry out authorized gameplay actions through MCP or the CLI. It also guides local account setup and migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: General write access also exposes under-disclosed account-deletion and payment-related commands.

Mitigation: Keep read-only mode enabled until account-cancellation and payment-related tools are removed or separately restricted.

Risk: The local credential file contains sensitive account credentials and tokens in plaintext.

Mitigation: Protect the credential file and keep it private.

Risk: Entering a character replaces its active browser or mobile session, including in read-only mode.

Mitigation: Use existing session-takeover authorization; otherwise explain the effect and confirm before connecting.

## Reference(s):

- [Earth2037 AI documentation](https://www.earth2037.com/ai/)
- [SETUP.md](references/SETUP.md)
- [WORKFLOWS.md](references/WORKFLOWS.md)

## Skill Output:

**Output Type(s):** [API Calls, Configuration, Guidance, Text]

**Output Format:** [MCP tool calls, CLI commands, configuration files, and concise gameplay guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Game actions depend on player authorization and the configured read-only setting.]

## Skill Version(s):

2.0.3 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
