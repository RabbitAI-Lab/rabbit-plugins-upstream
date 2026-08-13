## Description:

QuintaDB helps agents read, create, update, and delete data in QuintaDB through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected QuintaDB account from an agent, including listing databases and forms, reading records, and creating, updating, or deleting records with schema-driven payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and permanently delete QuintaDB records in a connected account.

Mitigation: Require user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

Risk: Incorrect payloads could modify the wrong fields or records.

Mitigation: Inspect the live connector schema before constructing action payloads and review the final JSON before execution.

Risk: Installing the skill grants an agent a path to operate the connected QuintaDB account.

Mitigation: Install it only for workflows where agent access to QuintaDB is intended and keep the OOMOL connection scoped to the required account.

## Reference(s):

- [QuintaDB homepage](https://quintadb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quintadb)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect live connector schemas before running QuintaDB actions.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
