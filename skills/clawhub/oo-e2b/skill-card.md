## Description:

E2B helps agents manage E2B sandboxes through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create, inspect, list, and delete E2B sandboxes from an agent session while relying on OOMOL-connected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute unverified code.

Mitigation: Prefer a package-managed or otherwise verified oo CLI installation path, avoid elevated pipe-to-shell execution, and review installer contents before running them.

Risk: Write and destructive actions can create or delete E2B sandboxes.

Mitigation: Fetch the live action schema, confirm the exact payload and target with the user, and require explicit approval before create or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-e2b)
- [E2B Homepage](https://e2b.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
