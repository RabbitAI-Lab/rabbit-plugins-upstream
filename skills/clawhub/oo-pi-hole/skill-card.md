## Description:

Operate Pi-hole through an OOMOL-connected account with oo CLI actions for reading metrics, inspecting logs, managing domains, lists, clients, groups, DNS blocking, gravity updates, and backup import or export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Pi-hole administrators use this skill to operate a connected Pi-hole instance from an agent, including monitoring, log review, domain and list management, DNS blocking control, gravity updates, and teleporter backup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can run a remote installer directly in a shell.

Mitigation: Install only after trusting OOMOL and prefer manually installing the oo CLI from verified official instructions.

Risk: Write and destructive Pi-hole actions can change DNS behavior, delete entries, flush logs, import backups, or update configuration.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before write or destructive actions.

Risk: Incorrect request payloads could modify the wrong Pi-hole resource or fail against the connected instance.

Mitigation: Inspect the live action schema with oo CLI before constructing payloads and use read actions when possible.

## Reference(s):

- [Pi-hole Homepage](https://pi-hole.net)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pi-hole)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution and returns oo CLI JSON responses when actions run.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
