## Description:

Collect one X (Twitter) post and its replies with the official Gecho Bridge MCP tool for post content, author data, engagement, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social media researchers use this skill to collect and summarize a known X post and available replies through Gecho Bridge, including post content, author details, engagement, comments, and saved result paths when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow connects Gecho Bridge and its Chrome extension to a logged-in X browser session.

Mitigation: Install only if you are comfortable with that connection, and review the Gecho Bridge package and extension source or trust before use.

Risk: Collected post data can be written to local storage when a save directory is provided.

Mitigation: Provide a save directory only when you want collected post data written locally, and choose an intended writable directory.

Risk: Login walls, CAPTCHA, verification prompts, region prompts, cookie prompts, or blocked pages can prevent collection.

Mitigation: Resolve platform prompts manually in Chrome before running the workflow, then stop and report the exact failure if the tool still fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/x-post-detail)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho website](https://gecho.ai/)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with setup commands and summarized structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a saved local result path when provided by the tool; avoids pasting full raw JSON.]

## Skill Version(s):

1.1.37 (source: release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
