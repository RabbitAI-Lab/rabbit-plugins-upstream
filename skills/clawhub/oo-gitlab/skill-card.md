## Description:

GitLab helps agents read, create, update, merge, and delete GitLab projects, issues, and merge requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage GitLab projects, issues, and merge requests from an agent session while relying on live connector schemas and an OOMOL-connected GitLab account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on GitLab projects, issues, and merge requests visible to the connected account, including creating, updating, merging, and deleting.

Mitigation: Use a GitLab account with appropriate scope and require clear confirmation before any write or destructive request.

## Reference(s):

- [GitLab](https://gitlab.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
