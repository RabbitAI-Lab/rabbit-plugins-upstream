## Description:

This skill helps agents read, create, update, and delete TalentLMS data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and administrators use this skill to inspect TalentLMS records and manage users, courses, groups, branches, and categories through the oo CLI. It supports read actions directly and requires confirmation for write or destructive user operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI without verification.

Mitigation: Prefer a verified, pinned, or package-manager-based oo CLI installation method before using the skill.

Risk: The skill can create, update, and delete TalentLMS users.

Mitigation: Require user confirmation for write actions and explicit approval before destructive delete actions.

## Reference(s):

- [ClawHub TalentLMS Skill](https://clawhub.ai/oomol/skills/oo-talentlms)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [TalentLMS](https://www.talentlms.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector actions and returns JSON responses from TalentLMS.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
