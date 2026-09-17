## Description:

Perplexity operates Perplexity through an OOMOL-connected account for grounded Sonar chat completions, embeddings, model listing, and ranked web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Perplexity actions through an OOMOL-connected account, including chat completions, embeddings, model discovery, and raw web search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer scripts that could be run automatically by an agent.

Mitigation: Confirm setup commands manually, install the oo CLI only from a trusted source, and prefer version pinning or verification before use.

Risk: Write-tagged Perplexity actions can create chat completions or embeddings with user-provided payloads.

Mitigation: Review the live action schema and confirm the exact payload and intended effect with the user before running write-tagged actions.

## Reference(s):

- [Perplexity skill page on ClawHub](https://clawhub.ai/oomol/skills/oo-perplexity)
- [OOMOL publisher profile on ClawHub](https://clawhub.ai/user/oomol)
- [Perplexity homepage](https://www.perplexity.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Perplexity connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
