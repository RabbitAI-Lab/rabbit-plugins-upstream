## Description:

Routes Jina AI embedding and reranking requests through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Jina AI action schemas and run embedding or reranking requests through an OOMOL-connected account without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run mutable remote installer scripts, and embedding creation is marked as a write action.

Mitigation: Review the oo CLI installer source or use a verified installation method, then confirm embedding payloads before execution.

## Reference(s):

- [ClawHub Jina AI Skill](https://clawhub.ai/oomol/skills/oo-jina-ai)
- [Jina AI Homepage](https://jina.ai)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should inspect live action schemas before constructing requests and should confirm write-action payloads before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
