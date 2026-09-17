## Description:

Docmosis helps agents operate Docmosis through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected Docmosis account use this skill to inspect live connector schemas, check Docmosis environment readiness, review template metadata and structure, and render documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Use official versioned installation instructions with checksum or signature verification before running installer commands.

Risk: Document rendering can generate output and consume Docmosis or OOMOL service resources.

Mitigation: Confirm the target template, input data, and expected resource impact before rendering documents.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-docmosis)
- [Docmosis homepage](https://www.docmosis.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON when run with --json; document rendering may return delivery metadata or base64 output.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
