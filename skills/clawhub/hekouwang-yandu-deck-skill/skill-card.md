## Description:

YanDu DECK helps an agent turn articles or topics into one-screen-per-idea, swipeable, auto-playing keynote-style HTML decks, localize fonts, configure optional comments, and publish the result to Cloudflare Pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

External developers and content producers use this skill to convert long-form articles or presentation topics into immersive web decks and to package the templates, publishing script, Cloudflare Pages configuration, and optional D1-backed comments workflow needed to ship them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish generated decks as public Cloudflare Pages sites.

Mitigation: Run the publishing script in build-only mode first and inspect the generated dist output for private or unintended material before deployment.

Risk: The artifact includes a hardcoded Cloudflare analytics beacon token.

Mitigation: Replace the analytics token with one controlled by the deployer or remove the beacon before publishing.

Risk: Leaving placeholder Cloudflare D1 or wrangler.toml values unchanged can bind comments to the wrong project or database.

Mitigation: Fill in the deployer's own Cloudflare Pages and D1 values and verify the binding before enabling the comments feature.

Risk: The publishing script can install Wrangler globally when it is missing.

Mitigation: Prefer installing and pinning Wrangler separately, then review the script behavior before allowing any global tool installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-yandu-deck-skill)
- [Repository homepage](https://github.com/huiyonghkw/hekouwang-yandu-deck-skill)
- [Live YanDu DECK site](https://hekouwang.pages.dev)
- [Mobile safe-area and comments notes](references/mobile-and-comments.md)
- [Theme token flip guide](references/%E6%8D%A2%E8%82%A4-token-flip.md)
- [Cloudflare Pages Functions and D1 comments guide](references/%E7%95%99%E8%A8%80%E6%9D%BF-D1.md)
- [YanDu DECK system notes](references/%E7%B3%BB%E7%BB%9F%E8%AF%B4%E6%98%8E.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, JavaScript, Python, shell command, TOML, and SQL snippets or file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for agent-assisted deck creation, local build review, Cloudflare Pages publishing, and optional comments setup; deployment should be explicitly reviewed before running.]

## Skill Version(s):

1.3.2 (source: frontmatter and changelog, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
