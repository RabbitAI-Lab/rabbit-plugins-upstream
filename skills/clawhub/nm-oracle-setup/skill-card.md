## Description:

Provisions the oracle ML inference daemon with onnxruntime via uv.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to provision and verify the local ONNX runtime environment needed by the oracle ML inference daemon.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup process creates a local Python virtual environment and downloads onnxruntime.

Mitigation: Install only when you intend to provision the oracle plugin's local inference environment and are comfortable with uv-managed dependency downloads.

Risk: The skill calls the oracle plugin's provisioning function.

Mitigation: Review the referenced oracle plugin before use if you have not already trusted that plugin.

Risk: Provisioning can fail when uv or network access is unavailable.

Mitigation: Confirm uv is installed and network access is available before running setup; report any returned error to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-oracle-setup)
- [Oracle plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/oracle)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline bash code blocks and short status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports provisioning success or failure and suggests checks for uv and network availability.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
