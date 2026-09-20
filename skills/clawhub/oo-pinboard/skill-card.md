## Description:

This skill lets an agent handle Pinboard requests for reading, creating, updating, and deleting data through the OOMOL-connected Pinboard connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, add, replace, and delete Pinboard bookmarks through an OOMOL-connected account. It is intended for Pinboard workflows where the agent should use the oo CLI connector rather than direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the oo CLI through a remote shell command can execute installer code from OOMOL.

Mitigation: Install only after trusting OOMOL and reviewing or verifying the installer; run setup steps only when the CLI is missing or authentication fails.

Risk: Bookmark add, replace, and delete actions can overwrite or remove Pinboard data.

Mitigation: Confirm the exact URL, payload, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [Pinboard homepage](https://pinboard.in/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pinboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the oo CLI connector.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
