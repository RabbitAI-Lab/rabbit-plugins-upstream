## Description:

Collect Amazon product reviews with the official Gecho Bridge MCP tool, including review text, ratings, dates, and reviewer metadata when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect and summarize Amazon product reviews through the official Gecho Bridge workflow when they provide a product URL or ASIN.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can access data visible in the user's logged-in Amazon browser session.

Mitigation: Use it only for review collection on products the user specifies, and resolve login, CAPTCHA, verification, region, and cookie prompts manually in Chrome.

Risk: Saved raw results may contain review text, reviewer metadata, or other collected product-review details.

Mitigation: Choose save directories deliberately and avoid storing raw results where unrelated users or processes can access them.

Risk: Running multiple live browser collection jobs can interfere with the extension-backed workflow.

Mitigation: Run only one Gecho scraping job in a conversational turn and avoid parallel collection jobs.

## Reference(s):

- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)
- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/amazon-reviews)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown with inline bash code blocks and concise review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review counts, selected review fields, setup links, exact failure reasons, and saved result paths when available.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
