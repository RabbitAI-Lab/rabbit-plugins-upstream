## Description:

Install and configure the ClawGuard security plugin - an LLM-as-a-Judge guardrail that detects and blocks risky tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lidan-capsule](https://clawhub.ai/user/lidan-capsule)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to install, configure, and troubleshoot ClawGuard for OpenClaw gateways so tool calls can be evaluated and optionally blocked before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan says the third-party plugin has broad visibility into tool calls.

Mitigation: Review the @capsulesecurity/clawguard package version before installation and tightly control tool-call logging, metrics, and configured LLM providers when prompts or tool arguments may contain secrets.

Risk: The security scan notes risky credential-display troubleshooting.

Mitigation: Avoid printing gateway tokens in shared logs or terminals; inspect and rotate credentials using approved secret-handling procedures.

## Reference(s):

- [ClawGuard GitHub](https://github.com/capsulesecurity/clawguard)
- [ClawGuard npm package](https://www.npmjs.com/package/@capsulesecurity/clawguard)
- [ClawGuard ClawHub page](https://clawhub.ai/lidan-capsule/skills/clawguard)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and configuration tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes installation, Docker setup, verification, configuration, authentication troubleshooting, and operational workflow guidance.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
