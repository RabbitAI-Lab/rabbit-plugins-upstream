## Description:

Searches Amazon products through the official Gecho Bridge MCP workflow and returns marketplace-specific product lists with prices, ratings, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce researchers use this skill to route Amazon product-discovery requests to Gecho Bridge, collect structured marketplace results, and summarize the most useful product fields without pasting raw result dumps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow connects Gecho Bridge to a Chrome session where the user is logged into Amazon.

Mitigation: Install only when that connection is acceptable, review Gecho Bridge and the Chrome extension before use, and keep platform credentials handled manually in Chrome.

Risk: Amazon login, CAPTCHA, region, cookie, or blocking pages can prevent reliable product results.

Mitigation: Resolve platform prompts manually in Chrome before retrying, and stop on tool errors, timeouts, or empty results rather than substituting another scraper.

Risk: Saved result files may contain marketplace research data from the active browser session.

Mitigation: Choose an appropriate writable save directory and use the skill only for Amazon marketplace data that the user intends to collect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/amazon-search-zh-cn)
- [Gecho Bridge documentation](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho website](https://gecho.ai/)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command blocks and concise product-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs should report completion, result count, save path when available, and only the most useful 3 to 5 product results or fields.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
