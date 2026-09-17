## Description:

AI Skill Creator (EN) guides agents through creating, reviewing, packaging, and publishing ClawHub skills using a staged workflow with security review and quality gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to scaffold new ClawHub or OpenClaw skills, draft skill files, run security and quality review steps, and prepare publishable packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to create files, package artifacts, publish releases, and perform rollback actions.

Mitigation: Require explicit confirmation for target paths, permissions, publish actions, and rollback actions before execution.

Risk: The security workflow references a CISO-001 authorization string that may be mistaken for real authorization.

Mitigation: Treat CISO-001 only as workflow text and require real human or organizational approval for security review decisions.

Risk: The rollback guidance includes a broad Git restore pattern.

Mitigation: Replace broad rollback commands with a scoped restore of only the intended skill directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/ai-skill-creator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON, shell commands, and file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to generate skill files, package artifacts, publish releases, and review rollback actions.]

## Skill Version(s):

1.1.0-en2 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
