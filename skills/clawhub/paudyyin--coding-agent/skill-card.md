## Description:

Provides configurable Chinese-language coding sub-agents for OpenClaw that route code review, security audit, and testing requests to specialized agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using OpenClaw use this skill to route coding requests to Chinese-language sub-agents for code review, security auditing, and test generation. It helps standardize review, risk scanning, and testing workflows across coding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms such as review, security, or test may activate a sub-agent unexpectedly.

Mitigation: Confirm the intended task type and repository scope before allowing file inspection or command execution.

Risk: Configured sub-agents can read files and run project commands when the host grants those tools.

Mitigation: Use the skill only in repositories where file inspection and local command execution are acceptable, and review commands before they run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/coding-agent)
- [Agent Definition Specification](artifact/references/agent-definition-spec.md)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with optional code blocks, command suggestions, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs follow the selected sub-agent role: code review findings, security audit findings, or test plans and generated tests.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
