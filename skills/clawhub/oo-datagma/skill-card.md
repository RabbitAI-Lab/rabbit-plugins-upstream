## Description:

Datagma lets an agent search, read, and enrich Datagma people and company data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Datagma from an OOMOL-connected account, including enrichment, work-email discovery, phone-number search, job-change checks, and credit lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute code on the user's machine.

Mitigation: Do not allow an agent to run installer commands automatically; use official, inspectable, versioned installation steps and verify checksums or signatures when available.

Risk: Datagma lookup inputs may include personal or business contact data sent through the Datagma/OOMOL connector.

Mitigation: Use the skill only with data the user is authorized to process and confirm that sending lookup inputs to the connected service is acceptable.

## Reference(s):

- [ClawHub Datagma Skill](https://clawhub.ai/oomol/skills/oo-datagma)
- [Datagma Homepage](https://datagma.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
