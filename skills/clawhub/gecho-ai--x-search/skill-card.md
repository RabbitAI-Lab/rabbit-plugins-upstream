## Description:

Searches public X (Twitter) posts by keyword with the Gecho Bridge MCP tool and returns post text, authors, engagement data, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for keyword-level X research and monitoring, including collecting representative public posts, engagement fields, author information, links, and optional saved result data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a third-party Chrome extension and MCP server operating through the user's logged-in browser session.

Mitigation: Install and use it only for intended X searches, review the Gecho Bridge package and extension trust boundary, and keep the browser session limited to accounts and data appropriate for the task.

Risk: Search results can include saved local data when a save directory is used.

Mitigation: Choose a writable save directory that is appropriate for the sensitivity of the collected public post data.

Risk: Login walls, CAPTCHA, verification, region prompts, cookie prompts, or blocked pages can prevent reliable collection.

Mitigation: Resolve required platform prompts manually in Chrome before running the workflow and stop on tool failures or timeouts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/x-search)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with command snippets and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public post text, authors, engagement counts, links, status messages, setup guidance, and a saved local result path when available.]

## Skill Version(s):

1.1.37 (source: evidence.release.version and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
