## Description:

Pinboard (pinboard.in) lets agents read, create, update, and delete Pinboard data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Pinboard bookmarks through an OOMOL-connected account, including listing, retrieving, adding, replacing, and deleting bookmarks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may run unverified scripts if an agent executes setup steps automatically.

Mitigation: Install the oo CLI only through a trusted, verifiable method and do not let the agent run remote installer commands automatically.

Risk: Bookmark write and delete actions can change or remove user data.

Mitigation: Confirm exact payloads before write actions and require explicit approval before destructive delete actions.

## Reference(s):

- [ClawHub Pinboard Skill](https://clawhub.ai/oomol/skills/oo-pinboard)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Pinboard](https://pinboard.in/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include connector command payloads and returned JSON data summaries.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
