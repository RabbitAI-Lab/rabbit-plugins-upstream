## Description:

Systematic 6-layer diagnostic framework for OpenClaw issues: policy, config, runtime, logs, network, code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivanovandreidimitrov-ctrl](https://clawhub.ai/user/ivanovandreidimitrov-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to diagnose OpenClaw issues systematically across policy, configuration, runtime state, logs, network, and code before proposing a root cause and fix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The diagnostic process may involve reading configuration, runtime status, logs, and plugin code that contain sensitive operational details.

Mitigation: Use the skill only where that level of diagnostic visibility is appropriate, and redact secrets or sensitive logs before sharing findings.

Risk: Troubleshooting guidance can lead to incorrect conclusions if symptoms are summarized without evidence.

Mitigation: Require each hypothesis to be verified against logs, configuration, runtime state, or code before acting on a proposed fix.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivanovandreidimitrov-ctrl/skills/deep-diagnostic-procedure-public)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklist steps, inline shell commands, and a diagnostic report template.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
