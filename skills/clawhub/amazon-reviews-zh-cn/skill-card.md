## Description:

Collects Amazon product reviews through the official Gecho Bridge MCP, including review text, ratings, dates, and available reviewer information when the user provides an Amazon product URL or ASIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce researchers use this skill to collect structured Amazon product reviews through Gecho Bridge for product research. The agent routes a single review-collection task, summarizes useful fields, and reports a saved result path when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge, the Gecho Chrome extension, and a logged-in Amazon browser session.

Mitigation: Install only if comfortable using those components together, review the external extension/MCP project, and keep the task limited to products intended for research.

Risk: Collected review data may be saved to a local directory.

Mitigation: Choose a save directory that is appropriate for storing collected review data and avoid sharing raw outputs unnecessarily.

Risk: Amazon login, verification, region, cookie, or blocking pages can prevent collection or produce incomplete results.

Mitigation: Resolve those prompts manually in Chrome before retrying, and stop on tool errors or empty results instead of substituting another collection method.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/amazon-reviews-zh-cn)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge GitHub repository](https://github.com/gecho-ai/gecho-bridge)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw configuration video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes configuration video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise status, setup commands, summaries, and saved result paths when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Limits displayed review details to the most useful fields or the first 3 to 5 items; avoids pasting full raw JSON into chat.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
