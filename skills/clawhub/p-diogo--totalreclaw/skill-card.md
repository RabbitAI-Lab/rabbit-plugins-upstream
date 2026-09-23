## Description:

End-to-end encrypted, decentralized memory for OpenClaw, with automatic recall through memory_search and memory_get and background fact capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[p-diogo](https://clawhub.ai/user/p-diogo)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and agent developers use TotalReclaw to add persistent encrypted memory, automatic recall, explicit memory saves, account pairing, import, export, and curation workflows to an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The plugin has broad background access to local OpenClaw conversations, credentials, host configuration, and persistent instructions under the same OS account.

Mitigation: Install only on a dedicated machine or OS user, use a dedicated recovery phrase, and use a narrowly scoped LLM provider key.

Risk: The security evidence flags remotely downloaded executable code as something users should review carefully.

Mitigation: Avoid shared multi-agent or multi-user gateways until polling and credential access are limited to the active agent and remote executable loading is removed or verified with a stronger trust root.

## Reference(s):

- [ClawHub TotalReclaw listing](https://clawhub.ai/p-diogo/skills/totalreclaw)
- [TotalReclaw homepage](https://totalreclaw.xyz)
- [OpenClaw setup guide](https://github.com/p-diogo/totalreclaw/blob/main/docs/guides/openclaw-setup.md)
- [Release 3.4.1](https://github.com/p-diogo/totalreclaw/releases/tag/v3.4.1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and agent tool instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for OpenClaw memory setup, recall, explicit saves, pairing, import, export, and curation.]

## Skill Version(s):

3.4.1 (source: SKILL.md frontmatter, package.json, skill.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
