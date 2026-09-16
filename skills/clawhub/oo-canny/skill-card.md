## Description:

Operate Canny through OOMOL's oo CLI connector to read, create, and update boards, posts, comments, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate a connected Canny workspace through OOMOL, including listing boards, posts, comments, and users and creating or updating Canny records after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute remote installer scripts without built-in verification.

Mitigation: Review the setup path before installing and prefer a pinned, signed, or checksum-verified oo CLI release.

Risk: Create and update actions can change Canny workspace data.

Mitigation: Approve write operations only after checking the exact payload and the affected Canny record.

## Reference(s):

- [Canny homepage](https://canny.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
