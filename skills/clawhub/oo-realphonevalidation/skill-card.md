## Description:

RealPhoneValidation helps agents validate individual 10-digit phone numbers through RealPhoneValidation endpoints using an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to validate individual phone numbers and retrieve available caller enrichment through a connected RealPhoneValidation account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Phone lookup data is handled by OOMOL and RealPhoneValidation when the connector runs.

Mitigation: Install and run the skill only when that data handling is acceptable for the user's phone validation task.

Risk: Fallback setup guidance includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-managed oo CLI installation path, inspect installer scripts before use, and do not let an agent run remote installer commands automatically.

## Reference(s):

- [RealPhoneValidation homepage](https://realphonevalidation.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-realphonevalidation)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill inspects the live connector schema before constructing each payload.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
