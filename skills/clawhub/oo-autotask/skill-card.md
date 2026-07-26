## Description: <br>
Autotask lets an agent search and read Autotask Companies, Contacts, Tickets, entity metadata, and zone information through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to let an agent retrieve and query Autotask PSA company, contact, ticket, metadata, and zone information through OOMOL-connected credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Autotask Companies, Contacts, and Tickets through the user's OOMOL-connected account. <br>
Mitigation: Install it only when that access is intended, and review requested record IDs, filters, selected fields, and limits before execution. <br>
Risk: First-time setup may require installing or authenticating the OOMOL CLI when commands fail because the CLI or connection is missing. <br>
Mitigation: Review the OOMOL CLI install and connection steps before setup, and avoid running authentication or connection commands proactively. <br>


## Reference(s): <br>
- [ClawHub Autotask listing](https://clawhub.ai/oomol/skills/oo-autotask) <br>
- [Autotask PSA](https://www.datto.com/products/autotask-psa/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; runtime responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Autotask actions are described; credentials are handled through the user's OOMOL-connected account.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
