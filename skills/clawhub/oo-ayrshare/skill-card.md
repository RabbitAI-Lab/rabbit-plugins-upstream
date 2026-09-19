## Description:

Ayrshare (ayrshare.com). Use this skill for ANY Ayrshare request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Ayrshare through an OOMOL-connected account for reading social publishing data and creating, updating, validating, scheduling, retrying, or deleting posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include mutable remote installer scripts executed directly in Bash or PowerShell.

Mitigation: Review installer instructions before installing and prefer an official package manager, pinned release, or verified download for the oo CLI.

Risk: Publish, update, retry, and delete actions can affect public social media content or account data.

Mitigation: Confirm the exact payload and intended effect with the user before running write or destructive Ayrshare actions.

## Reference(s):

- [Ayrshare homepage](https://www.ayrshare.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Ayrshare OOMOL connection](https://console.oomol.com/app-connections?provider=ayrshare)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ayrshare)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Ayrshare action payloads.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
