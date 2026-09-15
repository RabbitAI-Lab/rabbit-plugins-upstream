## Description:

Together AI lets agents use an OOMOL-connected Together AI account to create chat completions, generate embeddings, and list available models through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route Together AI tasks through an OOMOL-connected account, including non-streaming chat completions, text embeddings, and model listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could execute downloaded scripts.

Mitigation: Install the oo CLI through a trusted, verified method and inspect downloaded scripts before running them; do not allow an agent to run installer commands automatically.

Risk: Write actions can create Together AI chat completions or embeddings through the connected account.

Mitigation: Fetch the live action schema and confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [Together AI homepage](https://www.together.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Together AI skill on ClawHub](https://clawhub.ai/oomol/skills/oo-together-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; JSON command responses include connector data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
