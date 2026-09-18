## Description:

Use this skill for Gitee requests that search and read account or repository data through an OOMOL-connected Gitee account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Gitee account and repository information through the OOMOL oo CLI connector. It supports reading the authenticated user profile, fetching repository details, and listing repositories visible to the connected user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions tell users to execute remote installer scripts directly.

Mitigation: Review the oo CLI installation source before installing; prefer a signed package, pinned release, or download-and-verify workflow.

## Reference(s):

- [Gitee](https://gitee.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are returned as JSON with data and metadata fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
