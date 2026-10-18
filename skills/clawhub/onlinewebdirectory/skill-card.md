## Description:

Checks crowd-observed website access conditions before a visit and reports directly observed access facts afterward.

This skill is ready for commercial/non-commercial use.

## Publisher:

[celestine1111](https://clawhub.ai/user/celestine1111)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to choose how to access a website based on shared observations, then contribute facts they directly observed during a visit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reporting sends observed website access facts to the directory service.

Mitigation: Report only facts directly observed and avoid including sensitive information.

Risk: Registration creates a local service key, and crowd-observed lookup results may be unreliable.

Mitigation: Protect the local key file and treat lookup results as hints rather than instructions.

## Reference(s):

- [Online Web Directory installation and API reference](https://onlinewebdirectory.net/install.md)
- [ClawHub skill listing](https://clawhub.ai/celestine1111/skills/onlinewebdirectory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON lookup results and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lookup results are crowd-observed hints, not instructions; reports contain directly observed site access facts.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
