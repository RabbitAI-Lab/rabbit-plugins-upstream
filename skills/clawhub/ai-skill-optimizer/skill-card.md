## Description:

Guides agents through optimizing existing skills for token use, performance, security hardening, code quality, baseline measurement, verification, rollback, and publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to assess and improve existing skill repositories across token efficiency, performance, security posture, maintainability, and release readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to modify skill repositories or publish externally without enough confirmation.

Mitigation: Use it only in an isolated worktree or disposable branch, and require explicit approval before rollback or publishing.

Risk: The CISO-001 authorization string in the artifact could be mistaken for real authorization.

Mitigation: Treat CISO-001 as workflow text only and require separate human approval for security hardening or release actions.

Risk: Rollback or publish commands may affect unintended files or destinations if scope is not checked.

Mitigation: Verify the exact files, branch, package contents, and registry destination before executing commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/ai-skill-optimizer)
- [Publisher profile](https://clawhub.ai/user/johnsmithfan)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with JSON examples, shell command examples, checklists, and report templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes task schemas, baseline and verification templates, and rollback and publishing guidance.]

## Skill Version(s):

1.1.0-en2 (source: server release metadata; skill frontmatter: 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
