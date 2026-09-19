## Description:

WideHive orchestrates large batch research by fanning out one target per isolated sub-agent, merging structured results with code, and producing scenario-specific reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxdwind](https://clawhub.ai/user/yxdwind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use WideHive to research 20 or more papers, companies, repositories, products, or other targets by delegating each target to an isolated worker and collecting verifiable merged outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spawn many web-research workers and create workspace files.

Mitigation: Confirm the target list and batch size before fan-out, and inspect the run directory before using generated outputs.

Risk: Result filename handling can be unsafe when target slugs are not trusted.

Mitigation: Use trusted target lists or sanitize slugs to simple file names before worker dispatch and merging.

Risk: The merged CSV output should be treated as untrusted when opened in spreadsheet software.

Mitigation: Review or clean merged.csv before spreadsheet import and avoid automatic execution of spreadsheet formulas.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yxdwind/skills/skill)
- [ClawHub publisher profile](https://clawhub.ai/user/yxdwind)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON schemas, shell commands, and generated run artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates per-target JSON checkpoints, merged JSON/CSV tables, and final scenario-shaped reports.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
