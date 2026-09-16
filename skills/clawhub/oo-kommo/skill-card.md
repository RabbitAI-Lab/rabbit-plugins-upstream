## Description:

Kommo lets an agent read Kommo CRM account, company, contact, lead, pipeline, task, and user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect live Kommo connector schemas and read CRM records through the OOMOL oo CLI without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct shell execution of remote installer scripts.

Mitigation: Install only after trusting OOMOL and the oo CLI distribution; prefer downloading and verifying a pinned installer before execution.

Risk: The skill reads data from the connected Kommo CRM account.

Mitigation: Use it only with the intended connected account and keep retrieved CRM data within the authorized workflow.

Risk: State-changing connector actions may affect Kommo records if exposed by the connector in the future.

Mitigation: Require explicit confirmation of the exact target, payload, and effect before approving any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kommo)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Kommo Homepage](https://www.kommo.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
