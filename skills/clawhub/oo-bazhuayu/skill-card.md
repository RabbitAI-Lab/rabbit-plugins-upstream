## Description:

Bazhuayu helps agents operate a connected Bazhuayu account through OOMOL's oo CLI for reading, creating, updating, and exporting task data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Bazhuayu task schemas, list and query task data, export records, and run state-changing cloud task operations through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Bazhuayu state by starting, stopping, copying, or updating tasks, loop items, parameters, and exported-data status.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and inspect the live action schema before building the payload.

Risk: Marking data as exported can acknowledge records at task scope and may disrupt parallel consumers.

Mitigation: Use one sequential consumer per task and persist the preceding unexported-data result before marking records as exported.

Risk: The skill depends on a trusted OOMOL connector account and Bazhuayu plan entitlements for higher-impact actions.

Mitigation: Install only when the OOMOL connector model is trusted, and resolve authentication, connection, scope, plan, or billing issues before retrying failed actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bazhuayu)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Bazhuayu Homepage](https://www.bazhuayu.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to fetch live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
