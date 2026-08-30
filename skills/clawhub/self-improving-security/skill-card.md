## Description:

Captures security findings, incidents, compliance gaps, and threat intelligence in project learning logs so agents can improve future security work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to capture vulnerabilities, access-control issues, misconfigurations, compliance findings, incident-response outcomes, and threat intelligence as structured markdown learnings. It supports recurring security review by turning resolved or repeated findings into reviewed runbooks, hardening checklists, playbooks, or agent guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security logs could accidentally capture secrets, credentials, tokens, private keys, or PII.

Mitigation: Redact sensitive values before writing to .learnings and describe the type and location of the exposure rather than the secret content.

Risk: Optional hooks may persist across sessions or inspect command output in sensitive environments.

Mitigation: Keep hooks project-scoped, prefer the activator-only reminder hook, and enable command-output detection only in trusted environments where it is needed.

Risk: Promoting findings into shared agent guidance could preserve incorrect or overbroad security rules.

Mitigation: Promote only broadly applicable patterns after an explicit user approval of a reviewed diff.

## Reference(s):

- [OpenClaw Security Integration](references/openclaw-integration.md)
- [Security Hook Setup Guide](references/hooks-setup.md)
- [Security Learning Examples](references/examples.md)
- [ClawHub skill page](https://clawhub.ai/jose-compu/skills/self-improving-security)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown entries, setup guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates project-scoped .learnings markdown files when the agent follows the skill; optional hooks emit reminder text.]

## Skill Version(s):

1.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
