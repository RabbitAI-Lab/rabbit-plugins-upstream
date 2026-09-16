## Description:

Consensus lets an agent search and read academic research through the OOMOL-connected Consensus connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Consensus for relevance-ranked academic papers with publication, study, and quality filters, then return research results through the connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes live remote installer pipelines for the oo CLI without checksum or signature verification.

Mitigation: Use an official, versioned oo CLI installation path with checksum or signature verification before relying on the skill.

## Reference(s):

- [Consensus Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-consensus)
- [Consensus Homepage](https://consensus.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or text with oo CLI command examples and JSON-backed Consensus search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to validate action payloads before execution; credentials are handled server-side by OOMOL.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
