## Description:

OwlCoda RunKit helps agents coordinate receipt-backed project work, dependencies, handoffs, verification evidence, and ready-for-commit receipts through project-owned artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yeemio](https://clawhub.ai/user/yeemio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate multi-agent project execution with durable work items, handoffs, decisions, verification receipts, and ready-for-commit evidence while keeping release and deployment authority separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill maintains local coordination and verification records in projects where it is used.

Mitigation: Install it only for projects where RunKit-maintained local records are desired.

Risk: The skill invokes an external owlrunkit CLI, so an unintended package or version could undermine evidence binding.

Mitigation: Confirm the owlrunkit CLI comes from the intended package and version before relying on receipts.

Risk: Deployment, skill-refresh, and remote-helper workflows can become high-authority actions.

Mitigation: Treat those workflows as separate actions requiring explicit owner approval.

## Reference(s):

- [OwlCoda homepage](https://github.com/yeemio/owlcoda)
- [ClawHub skill page](https://clawhub.ai/yeemio/skills/owlcoda-runkit)
- [OwlCoda RunKit Contract v0.2](artifact/references/contract-v0.2.md)
- [OwlCoda RunKit Contract v0.1](artifact/references/contract-v0.1.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project coordination instructions, CLI command plans, and local artifact templates; it does not grant Git, release, deployment, credential, or foreign-write authority.]

## Skill Version(s):

0.23.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
