## Description:

Creates delivery acknowledgement guidance and a local receipt, with optional delivery to a configured mail server or endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to compute delivery acknowledgement guidance and save a confirmation receipt. A configured delivery target also sends or submits the record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime delivery settings can submit the computed record and local artifact path to an arbitrary endpoint without per-run confirmation.

Mitigation: Before execution, review delivery endpoint, API key, and SMTP environment variables and the optional delivery configuration; run without delivery settings when only a local receipt is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/export-confirmation-style-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON receipt and local business artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes identification, confirmation, local-effect, and delivery outcomes; delivery is unconfigured by default.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
