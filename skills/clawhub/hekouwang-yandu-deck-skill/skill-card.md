## Description: <br>
YanDu DECK turns article topics into swipeable, auto-playing keynote-style web decks with self-hosted fonts and Cloudflare Pages publishing support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huiyonghkw](https://clawhub.ai/user/huiyonghkw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators and developers use this skill to convert articles or topics into immersive one-screen-per-idea web decks, update the YanDu DECK site, adjust deck themes, and prepare Cloudflare Pages releases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish to a live Cloudflare Pages site and change local project files during build and release work. <br>
Mitigation: Run with --build-only first, review generated files and Cloudflare settings, then deploy only after confirming the target project. <br>
Risk: Deployment and comment-board setup depend on site-specific Cloudflare, D1, analytics, and Wrangler configuration. <br>
Mitigation: Review CF_PROJECT, wrangler.toml, database identifiers, comment behavior, and analytics tokens before publishing. <br>
Risk: The security scan guidance warns against allowing the script to perform an unreviewed global Wrangler installation. <br>
Mitigation: Install and authenticate Wrangler separately, then run the publishing workflow from a reviewed local environment. <br>


## Reference(s): <br>
- [Hekouwang Yandu Deck Skill on ClawHub](https://clawhub.ai/huiyonghkw/skills/hekouwang-yandu-deck-skill) <br>
- [YanDu DECK live site](https://hekouwang.pages.dev) <br>
- [Token Flip Reference](references/换肤-token-flip.md) <br>
- [Comment Board D1 Reference](references/留言板-D1.md) <br>
- [System Notes](references/系统说明.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell commands, and configuration edits] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or modify HTML templates, Python scripts, Cloudflare Pages configuration, D1 schema, and deployment-ready site files.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
