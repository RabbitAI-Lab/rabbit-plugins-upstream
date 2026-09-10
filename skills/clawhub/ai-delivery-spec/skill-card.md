## Description:

AI Delivery Spec helps product teams and agents clarify, create, review, and change requirements, PRDs, interactive prototypes, and acceptance criteria for product, service, and office workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache-2.0

## Use Case:

Product, design, engineering, QA, delivery teams, and coding agents use this skill to turn vague goals, existing materials, and requested changes into clear product decisions, implementable specifications, prototypes, review handoffs, and acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Python tools and scaffold or force-style commands can write local files.

Mitigation: Run optional tools in a virtual environment without administrator privileges, and review write commands before execution.

Risk: Sensitive product, requirement, or prototype materials could be included in generated artifacts.

Mitigation: Use explicit invocation for sensitive tasks and avoid placing real secrets, credentials, or private customer data in requirement or prototype artifacts.

Risk: Generated requirements, PRDs, prototypes, or acceptance criteria can encode incorrect business rules if sources or authority are unclear.

Mitigation: Review outputs against authoritative source material, keep unresolved decisions explicit, and confirm business approval separately from generated validation results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [README](README.md)
- [Discovery guidance](references/discover.md)
- [Specification guidance](references/specify.md)
- [Prototype guidance](references/prototype.md)
- [Review workspace guidance](references/review-workspace.md)
- [Change and acceptance guidance](references/change-acceptance.md)
- [Context guidance](references/context.md)
- [Stages and tooling guidance](references/stages.md)
- [Host adapter guidance](references/tool-adapters.md)
- [5.5.0 release package and checksum](https://github.com/franklinxkk/ai-delivery-spec/releases/tag/v5.5.0)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured text, JSON/YAML snippets, shell commands, and interactive prototype files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to the current requirement, change, review, prototype, or acceptance task; optional local validation tools may produce files and reports.]

## Skill Version(s):

5.5.0 (source: server release metadata, artifact changelog, SKILL.md heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
