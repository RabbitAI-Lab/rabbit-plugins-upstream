## Description:

Guide for TeamAI, the CLI that syncs a team's AI skills, rules, docs, and environment settings across AI coding tools for setup, onboarding, management, contribution, troubleshooting, and uninstall flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeff-r2026](https://clawhub.ai/user/jeff-r2026)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and team administrators use this skill to set up and operate TeamAI so a team can share AI-agent skills, rules, docs, environment values, MCP configuration, and onboarding workflows across supported coding tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install and execute TeamAI-related command line tools and configure hooks across AI coding agents.

Mitigation: Install only from trusted sources, review each displayed command before execution, and limit setup to the intended tools when broad hook installation is not needed.

Risk: The skill may persist credentials, environment values, or hooks used by multiple AI agents.

Mitigation: Use narrowly scoped tokens, avoid broad long-lived credentials, and review environment changes before publishing or syncing them to a team.

Risk: The TGit provider guide includes an HTTP binary download path for the gf CLI.

Mitigation: Treat that installation path as unsafe unless the binary is fetched over HTTPS and verified with a checksum or signature.

## Reference(s):

- [TeamAI skill page](https://clawhub.ai/jeff-r2026/skills/teamai)
- [Setup admin guide](references/setup-admin.md)
- [Join member guide](references/join-member.md)
- [Manage admin guide](references/manage-admin.md)
- [Contribute member guide](references/contribute-member.md)
- [Troubleshooting guide](references/troubleshooting.md)
- [Tencent TGit provider guide](references/provider-tgit.md)
- [Uninstall guide](references/uninstall.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Menu-driven operational guidance that may ask for user choices, display commands before execution, and route to scenario-specific reference instructions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
