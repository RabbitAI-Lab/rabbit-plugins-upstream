## Description:

Viggle lets an agent read and manage Viggle characters, scenes, render jobs, and account credit through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Viggle from an agent session, including creating reusable characters and scenes, submitting render jobs, checking job status, and retrieving account resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute changing code on a user's machine.

Mitigation: Review the OOMOL CLI installation path before use and prefer a version-pinned or package-manager install with checksum or signature verification.

Risk: Write and destructive Viggle actions can create, modify, or delete account resources.

Mitigation: Approve write or delete actions only after checking the exact target and payload, with explicit approval for destructive actions.

## Reference(s):

- [ClawHub Viggle skill page](https://clawhub.ai/oomol/skills/oo-viggle)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Viggle homepage](https://viggle.ai)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building payloads and requires user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
