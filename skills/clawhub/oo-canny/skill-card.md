## Description:

Canny enables an agent to read, create, and update Canny boards, posts, comments, and users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Canny workspaces from an agent through the OOMOL oo CLI. It supports listing and retrieving Canny records, plus confirmed creation or update of supported posts, comments, and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may execute a remote installer script for the oo CLI.

Mitigation: Review the installer before use and prefer a verified package or checksum-backed installation path when available.

Risk: Connected Canny workspaces may be read and modified through confirmed write actions.

Mitigation: Connect only appropriate Canny workspaces and confirm the exact payload and expected effect before running write actions.

## Reference(s):

- [ClawHub Canny skill page](https://clawhub.ai/oomol/skills/oo-canny)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Canny homepage](https://canny.io)
- [OOMOL Canny connection](https://console.oomol.com/app-connections?provider=canny)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canny connector responses are returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
