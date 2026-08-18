## Description:

为建筑施工、市政、装修、园林、公路和基建等领域检索拟建项目、采购意向和临期续约线索，并按投资额、审批进度和紧急度生成商机清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development and construction sales teams use this skill to find early-stage construction and infrastructure opportunities in China, compare proposed projects, procurement intentions, and expiring contracts, and decide which leads to pursue next.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may create or use a persistent ZLBX account and save an API key under the user's home directory.

Mitigation: Use a preconfigured ZLBX_API_KEY when available, require explicit user consent before auto-registration, and review local credential storage before deployment.

Risk: Trial registration sends a hashed device identifier and basic platform attributes for quota de-duplication.

Mitigation: Proceed only when that data sharing is acceptable; preconfiguring ZLBX_API_KEY bypasses the auto-registration flow.

Risk: Generated chat output and HTML reports may contain direct-access signed links.

Mitigation: Treat generated links and reports as sensitive and share them only with the intended audience.

Risk: Construction opportunity results can be incomplete, stale, or unsuitable as the sole basis for commercial decisions.

Mitigation: Keep the skill's disclaimer and data-gap reporting in generated reports, and verify high-value opportunities against authoritative procurement or project sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/construction-project-opportunity-radar)
- [Opportunity radar workflow](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration workflow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown opportunity list with an optional generated HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved trial registration; a full three-route scan is documented as consuming about 8-15 API calls.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
