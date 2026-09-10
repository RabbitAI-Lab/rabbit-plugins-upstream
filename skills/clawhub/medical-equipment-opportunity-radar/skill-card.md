## Description:

医疗设备商机雷达 helps users find early procurement opportunities for medical equipment, devices, consumables, inspection reagents, and hospital information systems by scanning proposed hospital projects, health-system purchase intentions, and expiring maintenance or service contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, business development, and procurement-intelligence users use this skill to identify and prioritize early hospital procurement leads by product line and geography, then receive follow-up suggestions for each opportunity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement search terms and geography are sent to Zhiliaobiaoxun's API.

Mitigation: Use the skill only for queries appropriate for that external service, and avoid including confidential deal strategy or sensitive internal context in search prompts.

Risk: Automatic trial registration may use a hashed MAC-derived device identifier.

Mitigation: Prefer supplying an existing ZLBX_API_KEY. If no key is configured, review the consent prompt before allowing auto-registration.

Risk: API keys and signed report or notice links can grant access if exposed.

Mitigation: Protect ~/.zlbx/config.json as a secret and share generated HTML reports or sk/auto-login links only with trusted recipients.

## Reference(s):

- [Workflow](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Report Template](references/report-template.md)
- [Auto Registration Workflow](references/auto-register.md)
- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/medical-equipment-opportunity-radar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown opportunity list with an optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Zhiliaobiaoxun API results, preserves returned signed links in reports, and may write HTML reports under the user's home directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
