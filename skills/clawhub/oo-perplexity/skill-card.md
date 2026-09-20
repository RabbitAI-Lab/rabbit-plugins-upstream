## Description:

Operate Perplexity through an OOMOL-connected account using the oo CLI for chat completions, embeddings, model listing, and web search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Perplexity connector actions through an OOMOL-connected account, including web-grounded chat completions, raw search, model discovery, and embeddings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may execute a remote oo CLI installer script without checksum verification or version pinning.

Mitigation: Install the oo CLI separately from trusted OOMOL documentation or verify the installer before allowing the skill to run Perplexity connector actions.

Risk: Connector actions send task data through OOMOL and Perplexity.

Mitigation: Use the skill only when that data flow is intended for the task and the connected account is appropriate.

Risk: The embeddings action is tagged as a write action in the artifact.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-perplexity)
- [Perplexity Homepage](https://www.perplexity.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from Perplexity connector actions when commands are executed.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
