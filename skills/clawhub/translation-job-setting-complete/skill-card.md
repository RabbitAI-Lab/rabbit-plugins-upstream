## Description:

Builds a translation job entry from localization settings, writes a local job manifest, and optionally submits the record to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and localization teams use this skill to turn a locale, glossary, and register into a translation job record and local manifest, with optional delivery to a configured endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When delivery is enabled, the skill can send translation job data and a local artifact path to a configured HTTP endpoint without requesting confirmation.

Mitigation: Review the destination before enabling delivery; for local-only use, clear delivery endpoint and related SMTP settings and do not pass --delivery-config.

## Reference(s):

- [Localization Setting Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/translation-job-setting-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local JSON manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes identification and job results, a local artifact receipt, and a delivery status receipt.]

## Skill Version(s):

1.2.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
