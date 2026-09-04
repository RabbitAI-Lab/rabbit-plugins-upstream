## Description:

ComfyUI logs report missing external tools; isolate host, config, and executable paths quickly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to troubleshoot ComfyUI startup warnings about missing host executables, confirm whether the issue blocks startup or only a feature, and update the relevant configuration path when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend changing an executable path in a ComfyUI configuration.

Mitigation: Review the discovered host-native absolute path before applying changes, especially in important environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/host-dependency-triage)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands and configuration path recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend inspecting and updating a configured executable path after verifying the host-native binary.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
