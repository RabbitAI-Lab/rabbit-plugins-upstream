## Description:

Agentic feed digest using the feed CLI. Fetch, triage, and summarize RSS/Atom/JSON feeds to surface high-signal posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[odysseus0](https://clawhub.ai/user/odysseus0)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to catch up on RSS, Atom, and JSON feeds, triage unread entries, and produce concise digests of noteworthy posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on installing and running a third-party feed CLI.

Mitigation: Install only from a trusted source, review or pin the CLI version where possible, and scan the skill before deployment.

Risk: Using the feed CLI can contact configured feed servers and reveal reading activity through normal network requests.

Mitigation: Use only feed subscriptions and environments where those outbound requests are acceptable.

Risk: The workflow can mark selected feed entries as read.

Mitigation: Confirm the entry IDs before running read-status update commands.

## Reference(s):

- [Feed Digest on ClawHub](https://clawhub.ai/odysseus0/skills/feed-digest)
- [Publisher profile](https://clawhub.ai/user/odysseus0)
- [feed CLI Go package](https://github.com/odysseus0/feed/cmd/feed)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feed entry IDs, source names, dates, short summaries, and suggested read-status updates.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
