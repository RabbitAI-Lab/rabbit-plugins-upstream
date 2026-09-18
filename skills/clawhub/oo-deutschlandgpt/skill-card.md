## Description:

DeutschlandGPT (deutschlandgpt.de) lets an agent use an OOMOL-connected DeutschlandGPT account for reading, creating, and updating data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access DeutschlandGPT through an OOMOL-connected account, including chat completions, embedding generation, and model discovery without managing raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that execute directly in a shell.

Mitigation: Use a verified, versioned installer or official package path reviewed before execution; avoid running curl-to-shell or PowerShell invoke-expression commands as written.

Risk: Write actions can create chat completions or embeddings through the connected DeutschlandGPT workspace.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged [write], and fetch the live action schema before constructing data.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/oomol/skills/oo-deutschlandgpt)
- [DeutschlandGPT homepage](https://www.deutschlandgpt.de/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads; command responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
