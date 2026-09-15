## Description:

A-Leads (a-leads.co) supports A-Leads searching, reading, and contact-enrichment requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query A-Leads through their connected OOMOL account for business email lookup, personal email lookup, phone lookup, and email verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run a remote oo CLI installer on the user's machine.

Mitigation: Do not let an agent run installer commands automatically; install from a verified source or inspect the installer first.

Risk: A-Leads contact-enrichment lookups run through the user's connected account and may process personal or business contact data.

Mitigation: Run lookups only for user-approved requests and with an account connection the user has explicitly authorized.

Risk: Incorrect payloads could produce failed or unintended A-Leads queries.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [A-Leads homepage](https://a-leads.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-a-leads)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before running A-Leads actions; responses may include A-Leads data and an execution id.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
