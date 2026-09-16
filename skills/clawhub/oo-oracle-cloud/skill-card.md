## Description:

Operates Oracle Cloud Infrastructure through an OOMOL-connected oo CLI workflow for reading, creating, updating, and deleting OCI resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Oracle Cloud Infrastructure resources through the OOMOL-connected oo CLI, including networking, compute, tenancy, compartments, Monitoring metrics, alarms, and Oracle Cloud Agent actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, terminate, and delete OCI resources.

Mitigation: Use least-privilege OCI access limited to intended tenancies and compartments, and require explicit user confirmation for every write or destructive action.

Risk: The skill can run commands on compute instances through Oracle Cloud Agent.

Mitigation: Require explicit approval for each host command, verify the target instance and command payload, and avoid using the skill with accounts that can reach unintended hosts.

Risk: The documented CLI setup includes pipe-to-shell installation commands.

Mitigation: Install the oo CLI through a verified or pinned method and review installation scripts before execution.

## Reference(s):

- [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oracle-cloud)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OCI connector action names, validated JSON payloads, and summaries of JSON CLI responses.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
