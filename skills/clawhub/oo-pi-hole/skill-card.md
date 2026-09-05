## Description:

Operates an OOMOL-connected Pi-hole instance through the oo CLI for reading, creating, updating, and deleting Pi-hole data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and administer OOMOL-connected Pi-hole instances, including DNS blocking, logs, backups, configuration, and domains, lists, groups, and clients. It is intended for normal ClawHub use with user approval before state-changing or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad Pi-hole administration capability, including changes and deletions that can affect network behavior.

Mitigation: Confirm the exact payload and expected effect with the user before running any write or destructive action.

Risk: Backup export, DNS logs, query data, DHCP leases, and network device views can expose DNS activity and device information.

Mitigation: Retrieve only the information needed for the task and avoid sharing sensitive output beyond the intended user context.

Risk: The skill depends on OOMOL-connected access to administer the target Pi-hole instance.

Mitigation: Install and use it only when the user trusts OOMOL with Pi-hole administration for that connected instance.

## Reference(s):

- [Pi-hole homepage](https://pi-hole.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pi-hole)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
