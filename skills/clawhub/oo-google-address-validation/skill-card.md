## Description:

Provides agent guidance for using OOMOL's oo CLI to validate and standardize postal addresses with Google Address Validation and submit validation feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the Google Address Validation connector schema, validate and standardize postal addresses, and submit feedback for completed validation sequences through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Address data may be sent through OOMOL to Google.

Mitigation: Use the skill only when that data flow is acceptable, keep payloads minimal, and avoid unnecessary address details.

Risk: Remote installer commands can execute code from external sources.

Mitigation: Run installer commands only after independently verifying and trusting the installer source; prefer an existing trusted oo CLI installation.

Risk: The feedback action changes remote validation state.

Mitigation: Treat provide_validation_feedback as a write action and confirm the exact payload and intended effect with the user before running it.

Risk: Broad @file inputs may include more data than intended.

Mitigation: Inspect file contents before use and pass the smallest payload that satisfies the action schema.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-google-address-validation)
- [Google Address Validation Documentation](https://developers.google.com/maps/documentation/address-validation)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide schema inspection and connector execution; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
