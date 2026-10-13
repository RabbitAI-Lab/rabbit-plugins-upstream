## Description:

Helps an agent compare server changes and inspect status, Docker, backups, and Proxmox while distinguishing read, write, and destructive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[higangssh](https://clawhub.ai/user/higangssh)

### License/Terms of Use:

MIT-0

## Use Case:

Server operators and their agents use Homebutler to review changes, inspect server and container health, check backups and Proxmox guests, and perform requested administrative actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server reads can reveal hostnames, internal addresses, services, and logs.

Mitigation: Inspect only requested servers, treat results as sensitive, and summarize rather than sharing raw output.

Risk: Broad inventory scans and repeated remote reads can expose more infrastructure and incur unnecessary SSH traffic.

Mitigation: Avoid --all and inventory scans unless requested, and do not poll remote servers unnecessarily.

Risk: Restore, purge, stop, and power operations can overwrite data or interrupt services.

Mitigation: Require explicit human approval for the specific action and target before proceeding.

## Reference(s):

- [Homebutler on ClawHub](https://clawhub.ai/higangssh/skills/homebutler)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include server changes, items needing attention, and suggested actions; commands identify whether to use a tool or ask the operator to run them.]

## Skill Version(s):

2.5.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
