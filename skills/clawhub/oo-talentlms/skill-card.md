## Description:

This skill helps agents handle TalentLMS requests through OOMOL-connected TalentLMS actions for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate TalentLMS through an OOMOL-connected account, including user administration and read-only access to branches, categories, courses, groups, and users. Write and destructive TalentLMS actions require user confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run remote installer scripts directly in a shell.

Mitigation: Review the setup path before installing and prefer a verified package or separately downloaded and verified installer.

Risk: Write and delete actions can change or remove TalentLMS data.

Mitigation: Require explicit user confirmation for TalentLMS write actions and destructive actions before running them.

## Reference(s):

- [ClawHub TalentLMS Skill](https://clawhub.ai/oomol/skills/oo-talentlms)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [TalentLMS](https://www.talentlms.com)

## Skill Output:

**Output Type(s):** [shell commands, API calls, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect connector schemas and run TalentLMS actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
