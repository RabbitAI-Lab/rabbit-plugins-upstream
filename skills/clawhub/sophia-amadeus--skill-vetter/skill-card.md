## Description:

Audits AI skills for security risks before installation by checking credentials, permissions, network use, destructive operations, and ClawHub security status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sophia-amadeus](https://clawhub.ai/user/sophia-amadeus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill before installing or running ClawHub, GitHub, or third-party skills to review credentials, permissions, network access, destructive operations, and ClawHub security status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated verdicts can overstate safety after incomplete checks.

Mitigation: Use this skill as a checklist only; manually review the target package and rely on official ClawHub security status where available.

Risk: Pattern-based checks may miss important files, alternate execution paths, or disguised credentials.

Mitigation: Inspect all files and scripts in the target skill before installation, especially files that execute commands, access networks, or handle credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sophia-amadeus/skills/skill-vetter)
- [Credential Patterns](references/credential-patterns.md)
- [Safe Coding Patterns](references/safe-patterns.md)
- [Flagged Skills](references/flagged-skills.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and structured security verdict text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes security status, credential storage, network access, file system, permission, pattern, score, verdict, and reason fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
