## Description:

Monitors Chinese procurement intent notices, proposed projects, and expiring contracts to help users identify early-stage public-sector business opportunities before formal tender publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to scan Chinese public procurement signals by industry, region, budget, and renewal window. It produces ranked opportunity lists, follow-up guidance, and optional locally saved HTML reports.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may store account data and API credentials locally.

Mitigation: Prefer setting ZLBX_API_KEY directly and review or remove ~/.zlbx/config.json if local credential persistence is not acceptable.

Risk: Trial registration can fingerprint the device for duplicate-account controls.

Mitigation: Use a pre-provisioned API key to avoid auto-registration, or proceed only after explicit consent to the described device signals.

Risk: Generated reports may include signed access links that bypass normal login prompts.

Mitigation: Review generated reports and links before sharing, and avoid distributing reports outside the intended audience.

Risk: The skill writes opportunity reports to the local filesystem.

Mitigation: Store reports in an approved location and delete local report files when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/procurement-intent-monitor)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Auto-registration flow](references/auto-register.md)
- [Report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown opportunity lists and self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based trial registration; generated reports are saved locally and may contain signed access links.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
