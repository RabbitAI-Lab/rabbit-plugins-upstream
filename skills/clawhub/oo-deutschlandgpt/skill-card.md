## Description:

DeutschlandGPT lets an agent use an OOMOL-connected DeutschlandGPT account to list enabled models, create synchronous chat completions, and generate embeddings through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they want an agent to work with DeutschlandGPT through their OOMOL-connected account, including model discovery, chat completion, and embedding generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chat completion and embedding actions may send user-provided content to DeutschlandGPT and may consume account credits.

Mitigation: Review payloads before approving these actions, and use the connected account only for content appropriate to share with the service.

Risk: Write-tagged actions create service-side outputs through the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [DeutschlandGPT homepage](https://www.deutschlandgpt.de/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-deutschlandgpt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands and JSON request payloads; chat completions and embeddings may send user-provided content to DeutschlandGPT and consume connected account credits.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
