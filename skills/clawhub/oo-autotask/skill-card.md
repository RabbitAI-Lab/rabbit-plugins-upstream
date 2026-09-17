## Description:

Use this skill for Autotask requests that search, query, and read Autotask Companies, Contacts, Tickets, entity metadata, and API zone information through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Autotask PSA through an OOMOL-connected account, inspect action schemas, query records, retrieve records, and handle setup or billing recovery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Use a versioned, signed, or checksum-verified oo CLI installation method before running the connector.

Risk: The connected Autotask account determines what business records the agent can query or retrieve.

Mitigation: Connect only an Autotask account with read access appropriate for the agent's intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-autotask)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Autotask PSA](https://www.datto.com/products/autotask-psa/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; read actions can return JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: evidence.release.version; artifact SKILL.md metadata.version agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
