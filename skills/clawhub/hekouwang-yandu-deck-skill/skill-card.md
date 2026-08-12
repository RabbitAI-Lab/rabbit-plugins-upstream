## Description:

Creates immersive, swipeable, auto-playing HTML keynote-style decks from article content and supports publishing them to Cloudflare Pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and content creators use this skill to convert article content into one-screen-per-idea HTML deck pages, manage deck themes and site assets, add homepage or comment-board pieces, and build or deploy the result to Cloudflare Pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publishing workflow can deploy live Cloudflare Pages sites.

Mitigation: Run the build-only path first and verify the target Cloudflare project before any deployment.

Risk: The included publishing script may install global tooling.

Mitigation: Review scripts/publish.py before execution and install Wrangler through an approved local process.

Risk: A hard-coded Cloudflare analytics token may route analytics to the wrong account.

Mitigation: Replace or remove the Cloudflare Web Analytics beacon token before publishing.

Risk: Cloudflare D1 settings can point to another database if placeholders are not replaced.

Mitigation: Confirm wrangler.toml and D1 database bindings are set to the user's own Cloudflare account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huiyonghkw/skills/hekouwang-yandu-deck-skill)
- [Project Homepage](https://github.com/huiyonghkw/hekouwang-yandu-deck-skill)
- [Live YanDu DECK Site](https://hekouwang.pages.dev)
- [README.en.md](README.en.md)
- [Mobile and Comments Notes](references/mobile-and-comments.md)
- [Token Flip Theme Guide](references/换肤-token-flip.md)
- [Cloudflare D1 Comment Board Guide](references/留言板-D1.md)
- [System Notes](references/系统说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, JavaScript, Python, shell commands, and configuration file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate or modify HTML deck pages, templates, Cloudflare Pages configuration, D1 schema, and publishing scripts.]

## Skill Version(s):

1.3.1 (source: frontmatter, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
