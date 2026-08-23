## Description:

Retrieve complete Amazon product details with the official Gecho Bridge MCP tool, including title, price, variants, specifications, description, ratings, and links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route known Amazon product URLs or ASINs to Gecho Bridge and receive concise product-detail summaries. It is suited for product research workflows where a logged-in Chrome session and the Gecho extension are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates through Gecho's MCP server and Chrome extension in a logged-in browser session.

Mitigation: Use the skill only when the user is comfortable with that integration accessing Amazon product pages available in Chrome.

Risk: Amazon login, CAPTCHA, verification, region, or cookie prompts can block data collection.

Mitigation: Ask the user to resolve those prompts manually in Chrome before retrying the single Gecho workflow.

Risk: Running multiple browser-dependent Gecho jobs at once can interfere with the live tab and extension session.

Mitigation: Run only one Gecho Amazon product job per conversational turn and do not execute Gecho scraping jobs in parallel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/amazon-product)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise product-detail summaries, setup guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows only the top 3 to 5 useful fields, includes saved paths when available, and avoids pasting full raw JSON.]

## Skill Version(s):

1.1.37 (source: release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
