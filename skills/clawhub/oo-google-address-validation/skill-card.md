## Description:

Operates Google Address Validation through an OOMOL-connected oo CLI account to validate, standardize, and return details for postal addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to validate and standardize postal addresses with Google Address Validation through OOMOL's oo CLI, inspect live action schemas, and submit validation feedback after reviewing the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A state-changing validation feedback action may be run with the wrong responseId, payload, or intended effect.

Mitigation: Review the exact responseId, payload, and intended effect with the user before running provide_validation_feedback.

Risk: The setup guidance includes remote installer commands that may not be independently verified.

Mitigation: Prefer a verified or package-manager installation path for the oo CLI before running installer scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-google-address-validation)
- [Google Address Validation documentation](https://developers.google.com/maps/documentation/address-validation)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector requests; action responses are JSON with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
