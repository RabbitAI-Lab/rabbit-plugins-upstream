## Description:

TwitterAPI.io (twitterapi.io) lets an agent read, create, update, and delete TwitterAPI.io data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TwitterAPI.io from an agent workflow, including profile, tweet, timeline, search, list, Community, Space, trend, and monitoring tasks. It is suitable when the agent should use the OOMOL connector rather than calling the TwitterAPI.io API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional oo CLI install path uses a remote installer.

Mitigation: Install the oo CLI only when OOMOL is trusted and the remote installer approach is acceptable.

Risk: Write and destructive actions can change TwitterAPI.io monitoring users and tweet filter rules.

Mitigation: Review the exact payload and effect before approval, especially filter-rule and monitored-user changes.

## Reference(s):

- [TwitterAPI.io homepage](https://twitterapi.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-twitterapi-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that return JSON from TwitterAPI.io connector actions.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
