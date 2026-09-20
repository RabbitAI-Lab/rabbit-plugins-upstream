## Description:

Search public X (Twitter) posts by keyword with the official Gecho Bridge MCP tool and return post text, authors, engagement data, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route keyword-level X (Twitter) research requests to the Gecho Bridge MCP workflow, collect public post text, authors, engagement data, and links, and summarize the most useful results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup runs an external MCP server from a mutable latest package and registers it for reuse.

Mitigation: Install only when the Gecho publisher is trusted, and prefer a pinned Gecho Bridge version or verified release before setup.

Risk: The workflow uses a live browser session and can write collected X research results to disk.

Mitigation: Use a limited browser profile for X research, resolve login or verification prompts manually, and choose save directories carefully.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/x-search)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with summarized X post fields, links, saved paths when available, and setup or troubleshooting commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs summarize 3 to 5 useful items and avoid pasting full raw JSON.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
