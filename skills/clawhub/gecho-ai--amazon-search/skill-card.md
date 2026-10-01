## Description:

Searches Amazon products by keyword with the official Gecho Bridge MCP tool and returns structured listings, prices, ratings, and links across a selected marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce researchers use this skill to route Amazon product discovery requests through Gecho Bridge, summarize useful listing fields, and optionally save structured raw results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge, the Gecho Chrome extension, and a live logged-in Amazon browser session.

Mitigation: Install and log in to the extension, keep Amazon open in Chrome, and resolve login, CAPTCHA, region, cookie, or verification prompts manually before running the tool.

Risk: The setup commands use an unpinned external MCP package via @latest.

Mitigation: Review or pin the Gecho Bridge MCP package before use instead of relying blindly on the latest published version.

Risk: Saved raw results may be written to a user-selected directory.

Mitigation: Choose a deliberate writable save directory and avoid storing marketplace research output in sensitive or shared locations unless intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/amazon-search)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [API Calls, Markdown, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown summaries with structured listing fields, links, optional saved file paths, and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows the top 3 to 5 useful items or fields, reports exact failures, and avoids pasting full raw JSON.]

## Skill Version(s):

1.1.38 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
