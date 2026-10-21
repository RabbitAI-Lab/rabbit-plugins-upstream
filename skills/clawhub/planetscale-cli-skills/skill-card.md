## Description:

Provides command guidance and automation workflows for managing PlanetScale resources with the pscale CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and run PlanetScale CLI workflows for database, branch, deployment, organizational, and operational management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production deletion, demotion, deployment, or rollback instructions may lack clear approval and recovery checks.

Mitigation: Use narrowly scoped credentials; obtain explicit approval for the exact organization, database, and branch; review recovery options before destructive or production changes; keep automatic deployment disabled until proposed changes are reviewed.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI upstream repository (not release provenance)](https://github.com/planetscale/cli)
- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON]

**Output Format:** [Markdown guidance with pscale CLI examples and structured command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes bundled shell automation scripts; PlanetScale CLI authentication may be required.]

## Skill Version(s):

1.0.35 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
