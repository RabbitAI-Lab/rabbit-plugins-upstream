## Description:

Local tariff data source contract for SmartClaws master agents that defines the tariff snapshot file schema and how to use it during control decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eduv09](https://clawhub.ai/user/eduv09)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators using SmartClaws master agents use this skill to define a local tariff snapshot file and guide load-control decisions from current and lookahead tariff data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured tariff snapshot path could point to the wrong local file.

Mitigation: Before installing, confirm that snapshotFile points only to the intended tariff JSON file.

Risk: Stale, missing, or malformed tariff data could lead to poor control decisions.

Mitigation: Use freshness checks, treat invalid tariff data as non-authoritative, run a conservative control cycle, and report the tariff source issue.

Risk: Publishing local tariff data to device channels could expose data or alter system behavior.

Mitigation: Do not publish tariff data to device channels unless explicitly instructed by the owner.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eduv09/skills/smartclaws-tariff-file-source)
- [SmartClaws homepage](https://github.com/skalenetwork/smartclaws)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with YAML and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines local-file schema, freshness checks, and master-agent usage constraints; it does not add code, persistence, network behavior, or privileged actions.]

## Skill Version(s):

1.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
