## Description:

Search public X (Twitter) posts by keyword with the official Gecho Bridge MCP tool and return post text, authors, engagement data, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search public X (Twitter) posts by keyword through Gecho Bridge, summarize representative posts, and capture links, authors, engagement counts, and optional saved structured results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge and the Chrome extension connecting to a logged-in X session, which creates normal live-session and account-context exposure risks.

Mitigation: Install only when that session connection is acceptable, keep platform prompts handled manually in Chrome, and use the workflow only for public post research.

Risk: The setup path uses an npx @latest command, which may reduce reproducibility and can introduce unreviewed package updates.

Mitigation: Review the Gecho Bridge package or source before running setup, and use a pinned version in environments that require reproducible or reviewed dependencies.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/x-search)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with setup commands, concise result summaries, links, counts, and saved file paths when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs should show only the top 3 to 5 useful items or fields and should not paste full raw JSON.]

## Skill Version(s):

1.1.38 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
