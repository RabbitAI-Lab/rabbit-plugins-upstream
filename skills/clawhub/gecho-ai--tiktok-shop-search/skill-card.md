## Description:

Search TikTok Shop products by keyword with the official Gecho Bridge MCP tool and return structured product data, prices, ratings, sales signals, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce researchers, and developers use this skill to route TikTok Shop product discovery requests through Gecho Bridge and summarize structured product results for market or competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge and a Chrome extension connected to a logged-in TikTok Shop browser session.

Mitigation: Install only after reviewing the Gecho package and extension trust, and keep account login, CAPTCHA, verification, region, and cookie prompts under manual browser control.

Risk: Saved product results may be written to an unintended location if the save directory is unclear.

Mitigation: Choose a specific writable folder for saved results and provide a directory path rather than a JSON filename.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-shop-search)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise result summaries and inline shell command blocks when setup is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes the top 3 to 5 product results or useful fields and includes saved file paths when available.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
