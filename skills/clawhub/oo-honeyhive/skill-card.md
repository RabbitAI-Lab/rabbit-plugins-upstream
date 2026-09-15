## Description:

HoneyHive lets agents read, create, update, and delete HoneyHive data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage HoneyHive datasets and datapoint associations through the OOMOL oo CLI while relying on live connector schemas before each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of unverified remote installer scripts.

Mitigation: Review or replace the oo CLI setup path with a version-pinned or signed installer flow before installation.

Risk: Write and destructive HoneyHive actions can change datasets, remove datapoint associations, or permanently delete datasets.

Mitigation: Confirm the exact payload, target dataset, and intended effect with the user before approving write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-honeyhive)
- [HoneyHive homepage](https://www.honeyhive.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action schemas are inspected before execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
