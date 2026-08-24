## Description:

Retrieves complete TikTok Shop product details with the official Gecho Bridge MCP tool, including title, price, SKU, description, sales, ratings, and reviews, when the user provides a TikTok Shop product URL or product ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and researchers use this skill to collect and summarize structured details for a single TikTok Shop product through Gecho Bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge, the Gecho Chrome extension, and a logged-in TikTok Shop browser session.

Mitigation: Install only if comfortable with that browser-session dependency, review the extension and npm package provenance, and keep login, CAPTCHA, verification, and payment actions manual.

Risk: Product lookup can fail or return no collectable data when TikTok Shop presents login, CAPTCHA, region, cookie, verification, timeout, or blocked-page states.

Mitigation: Resolve platform prompts manually in Chrome before use, stop on tool errors, and report the exact failure reason instead of retrying repeatedly.

Risk: Saved results may be written to a local directory when a save folder is provided.

Mitigation: Use a specific writable absolute folder for saved output and review generated files before sharing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-product)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [Gecho Website](https://gecho.ai/)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional bash command blocks and saved-result paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries should show only the most useful fields and avoid pasting full raw JSON.]

## Skill Version(s):

1.1.37 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
