## Description:

Google Address Validation (developers.google.com). Use this skill for ANY Google Address Validation request: reading, creating, and updating data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to validate, standardize, and inspect postal addresses with Google Address Validation through an OOMOL-connected account. It also supports submitting validation feedback after the user confirms the payload and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running a remote installer script directly in the shell, which may execute unreviewed code.

Mitigation: Install only after trusting OOMOL and the oo CLI source; prefer downloading and inspecting the installer or using a verified package-manager flow before execution.

Risk: The provide_validation_feedback action changes service-side state.

Mitigation: Confirm the exact payload and expected effect with the user before running the action.

## Reference(s):

- [Google Address Validation documentation](https://developers.google.com/maps/documentation/address-validation)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-google-address-validation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before building action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
