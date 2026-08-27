## Description:

Feed Digest helps agents fetch subscription feeds, summarize items, classify information, and track read status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect feed items, generate concise digests, classify information, and manage read status inside an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the release suspicious because it asks agents for broad local command, file, and external API abilities that are not tightly scoped to feed summarization.

Mitigation: Review before installing, grant only the permissions needed for the intended workflow, and constrain use to trusted feeds and known storage paths.

Risk: Feed fetching and command execution can expose users to untrusted content or unintended local actions if inputs are not controlled.

Mitigation: Use trusted feed sources, avoid user-controlled command construction, and require explicit user approval for commands or writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feed-digest)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON result structures and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include digest results, metadata, status updates, execution logs, retry guidance, and configuration notes.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
