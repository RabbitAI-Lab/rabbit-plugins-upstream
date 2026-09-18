## Description:

GitLab skill for reading, creating, updating, and deleting GitLab data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to operate GitLab projects, issues, merge requests, and user profile data through an OOMOL-connected GitLab account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform real GitLab write and delete operations.

Mitigation: Confirm exact payloads and expected effects before write actions, and require explicit approval before destructive actions.

Risk: First-time setup examples include installer commands that execute remote scripts.

Mitigation: Prefer a verified, version-pinned installation method or inspect installer contents before running them.

Risk: Connected account permissions may allow broader GitLab access than intended.

Mitigation: Use an OOMOL/GitLab account whose scopes match the intended tasks.

## Reference(s):

- [ClawHub GitLab skill page](https://clawhub.ai/oomol/skills/oo-gitlab)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [GitLab homepage](https://gitlab.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GitLab connector JSON responses and execution identifiers when actions are run.]

## Skill Version(s):

1.0.5 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
