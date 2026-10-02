## Description:

Provides a local encrypted execution layer for agents to store secrets and run or delegate scripts and workflow packages across trusted nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to store local credentials and scripts, execute stored workflows, and delegate sealed packages to trusted devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents or scripts with MGC access may retrieve local secret values or launch stored workflows.

Mitigation: Install only if you trust the package, limit access to MGC, and protect the local database and token file.

Risk: Importing or running sealed packages from untrusted sources can execute untrusted workflows.

Mitigation: Accept and run sealed packages only from trusted sources; review the workflow before granting access.

Risk: Plaintext folder exports may expose stored workflow contents.

Mitigation: Keep plaintext exports within a trusted boundary and use sealed packages for cross-device delegation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zkeviny/skills/mgc-meta-skill)
- [Project homepage (listed in bundled manifest)](https://github.com/zkeviny/MGC-Blackbox)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Guidance]

**Output Format:** [Structured tool responses and sealed package files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return stored secrets or launch stored scripts; folder exports can produce plaintext archives.]

## Skill Version(s):

1.5.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
