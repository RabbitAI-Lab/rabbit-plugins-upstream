## Description:

Plate Recognizer helps agents read license plates from images and retrieve Snapshot Cloud usage through an OOMOL-connected Plate Recognizer account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Plate Recognizer Snapshot Cloud actions through OOMOL, including image plate reads and current-month usage checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes installer, login, and connection steps that can affect the user's local environment or account access.

Mitigation: Require explicit user approval before running installers, authentication commands, or connection steps.

Risk: The allowed oo CLI permission is broader than the two Plate Recognizer actions documented by the skill.

Mitigation: Limit agent use to platerecognizer get_statistics and read_number_plates, and inspect the live connector schema before each action payload.

Risk: The skill depends on a connected third-party account and can fail when authentication, scopes, credentials, app readiness, or billing are unavailable.

Mitigation: Attempt setup or billing remediation only after the matching error is observed, then ask the user before taking the documented corrective step.

## Reference(s):

- [Plate Recognizer homepage](https://platerecognizer.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Plate Recognizer ClawHub listing](https://clawhub.ai/oomol/skills/oo-platerecognizer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns normalized Plate Recognizer results when actions succeed.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
