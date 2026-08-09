## Description:

Systematic 6-layer diagnostic framework for OpenClaw issues: policy, config, runtime, logs, network, code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivanovandreidimitrov-ctrl](https://clawhub.ai/user/ivanovandreidimitrov-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to diagnose persistent OpenClaw issues by checking policy, configuration, runtime state, logs, network dependencies, and plugin code in a structured order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic work can expose sensitive log or configuration values such as credentials, tokens, phone numbers, or private channel information.

Mitigation: Review and redact logs or configuration output before sharing it publicly or with third parties.

Risk: The checklist includes shell and configuration commands that may behave differently across OpenClaw environments.

Mitigation: Review each command before running it and execute it only in the intended environment.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with checklists, diagnostic questions, inline shell commands, and a report template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces troubleshooting guidance only; it does not execute commands or collect data by itself.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
