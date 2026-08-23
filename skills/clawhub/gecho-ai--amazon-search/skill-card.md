## Description:

Search Amazon products by keyword with the official Gecho Bridge MCP tool and return structured listings, prices, ratings, and links across a selected marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run focused Amazon product discovery through Gecho Bridge and summarize structured listings for catalog or market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on a logged-in browser session through Gecho Bridge and the Gecho Chrome extension.

Mitigation: Install only if you are comfortable granting that access, and resolve login, CAPTCHA, verification, region, or cookie prompts manually in Chrome.

Risk: Collected Amazon listing data may be saved locally.

Mitigation: Use a directory you control for save_dir and review saved result files before sharing them.

Risk: Results may reflect session-specific details such as region, availability, or pricing.

Mitigation: Treat collected listings as point-in-time research output and verify important product, price, and availability details before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/amazon-search)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho website](https://gecho.ai/)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and summarized structured listing fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include the top 3 to 5 product listings and a saved local result path when available.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
