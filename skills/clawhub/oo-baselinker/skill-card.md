## Description:

BaseLinker helps agents search and read BaseLinker inventory catalogs, products, warehouses, orders, order events, and order statuses through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect BaseLinker commerce data from an OOMOL-connected account without handling raw API tokens. It is suited for read-focused inventory and order lookup workflows where the agent should inspect the live connector schema before running actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags the skill as suspicious because it advertises read-focused use while leaving room for broad connector actions.

Mitigation: Inspect the live connector schema before each action and require explicit user confirmation for any action that is tagged or behaves as write-capable or destructive.

Risk: The security guidance notes unsafe CLI installation steps as a concern.

Mitigation: Prefer installing the oo CLI through a verified package or an inspected installer before running connector commands.

Risk: The OOMOL-connected CLI can access a user's BaseLinker account through server-side credentials.

Mitigation: Install only when the user is comfortable granting this access, and independently restrict connector actions when read-only behavior is required.

## Reference(s):

- [ClawHub BaseLinker Skill Page](https://clawhub.ai/oomol/skills/oo-baselinker)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [BaseLinker Homepage](https://baselinker.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and a meta.executionId value.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
