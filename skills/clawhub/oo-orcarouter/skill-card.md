## Description:

OrcaRouter helps agents operate OrcaRouter through the OOMOL oo CLI for chat completions, embeddings, messages, and model listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect OrcaRouter action schemas and run OrcaRouter connector actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive prompts or embedded content may be sent to OrcaRouter or OOMOL during chat, message, or embedding actions.

Mitigation: Confirm user intent before submitting confidential content and avoid sending secrets, regulated data, or private prompts unless the user explicitly approves that transfer.

Risk: Chat, message, and embedding actions can consume paid OrcaRouter or OOMOL resources.

Mitigation: Confirm write-action payloads and expected effects before execution, and stop on billing or insufficient-credit errors until the user decides how to proceed.

Risk: The first-time setup guidance includes pipe-to-shell CLI installation commands.

Mitigation: Prefer a trusted package, verified installation instructions, or checksum/signature validation before installing the oo CLI.

## Reference(s):

- [ClawHub OrcaRouter Skill](https://clawhub.ai/oomol/skills/oo-orcarouter)
- [OrcaRouter Homepage](https://www.orcarouter.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
