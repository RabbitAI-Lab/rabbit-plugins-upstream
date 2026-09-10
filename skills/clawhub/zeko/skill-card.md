## Description:

Use when a user needs to use or build on Zeko, including bridge workflows, faucet funding, endpoint discovery, GraphQL or curl queries, sequencer and archive-node guidance, and zkApp development with o1js or OCaml.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hebilicious](https://clawhub.ai/user/hebilicious)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, builders, and agents use this skill to perform terminal-driven Zeko workflows, inspect network state, bridge assets, request faucet funds, and find the right documentation or endpoint for user and builder tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses private keys and GitHub tokens for bridge, SDK, and faucet workflows.

Mitigation: Use low-value testnet keys, avoid putting secrets directly in shell commands, and use narrowly scoped short-lived GitHub tokens.

Risk: The skill references unpinned command-line packages for blockchain operations.

Mitigation: Pin package versions where possible and independently verify tool packages before using them with valuable accounts.

Risk: Bridge or payment commands can broadcast irreversible transactions.

Mitigation: Require explicit confirmation before broadcasts and prefer documented high-level commands with machine-readable output for inspection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hebilicious/skills/zeko)
- [Zeko agent skills documentation](https://docs.zeko.io/developers/tools/agent-skills)
- [Zeko documentation](https://docs.zeko.io)
- [Bridge CLI documentation](https://docs.zeko.io/developers/tools/bridge-cli)
- [Bridge SDK documentation](https://docs.zeko.io/developers/guides/bridge-sdk)
- [Faucet CLI documentation](https://docs.zeko.io/developers/guides/faucet-cli)
- [Developer getting started](https://docs.zeko.io/developers/getting-started)
- [o1js documentation](https://docs.o1labs.org/o1js/)
- [Zeko protocol repository](https://github.com/zeko-labs/zeko)
- [Agent workflows reference](references/10-agent-workflows.md)
- [Navigation reference](references/10-navigation.md)
- [User flows reference](references/20-user-flows.md)
- [Bridge and faucet reference](references/30-bridge-and-faucet.md)
- [Endpoints and curl reference](references/40-endpoints-and-curl.md)
- [Build on Zeko reference](references/50-build-on-zeko.md)
- [Sequencer, archive, and DA reference](references/60-sequencer-archive-and-da.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, GraphQL, curl, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include executable CLI commands, endpoint values, environment variable guidance, and configuration snippets.]

## Skill Version(s):

0.0.1-main.18.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
