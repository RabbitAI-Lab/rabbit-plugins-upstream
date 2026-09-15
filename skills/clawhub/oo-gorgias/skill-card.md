## Description:

Use Gorgias through an OOMOL-connected account to search and read helpdesk account, ticket, customer, tag, and user data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support teams use this skill to let an agent retrieve Gorgias helpdesk records through their connected OOMOL account. It supports read workflows for accounts, tickets, customers, tags, and users with pagination, search, filtering, and ordering where the connector exposes them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags broad command permission and setup guidance as riskier than the documented read-only Gorgias purpose requires.

Mitigation: Install only when the user trusts OOMOL, prefers verified or package-manager installation of the oo CLI, and restricts oo CLI permissions to Gorgias read actions where the environment supports it.

Risk: The skill reads Gorgias account, ticket, customer, tag, and user data through a connected account.

Mitigation: Authenticate deliberately and connect only the intended Gorgias account before running read actions.

## Reference(s):

- [Gorgias homepage](https://www.gorgias.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Gorgias skill page](https://clawhub.ai/oomol/skills/oo-gorgias)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema inspection before JSON payload construction.]

## Skill Version(s):

1.0.2 (source: evidence metadata and release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
