## Description:

Provides agents with Z-Library search, metadata, recent-book, quota, and download actions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Z-Library, retrieve book metadata, list recent additions, check account download limits, and download book files through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute directly in a shell.

Mitigation: Review setup steps before installing; prefer an official package manager or a downloaded installer that can be inspected and verified, and avoid elevated shells.

Risk: Using a Z-Library connector may create legal or account-risk concerns.

Mitigation: Confirm the user's legal and account-risk context before using connector actions, especially downloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-zlibrary)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Z-Library Homepage](https://z-lib.org)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
