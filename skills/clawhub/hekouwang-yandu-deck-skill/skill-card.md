## Description:

Turns articles into interactive, auto-playing keynote-style web decks, with self-hosted fonts and optional publishing to Cloudflare Pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and content producers use this skill to turn article content into responsive, slide-based presentations, then build a local preview or optionally publish it to Cloudflare Pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publishing workflow can invoke Wrangler and publish the built site publicly when --deploy is used.

Mitigation: Review the publishing script's environment and network permissions, then confirm the Cloudflare project and content before deployment.

Risk: If the optional comments board is enabled, it stores visitor names, comment text, and a salted IP hash in D1.

Mitigation: Leave comments disabled unless needed; when enabling them, use your own D1 database and IP_SALT and disclose the collection to visitors.

## Reference(s):

- [Project homepage and installation](https://github.com/huiyonghkw/hekouwang-yandu-deck-skill)
- [Live YanDu DECK example](https://hekouwang.pages.dev)
- [System overview and deployment setup](references/系统说明.md)
- [Optional D1 comments board](references/留言板-D1.md)
- [Mobile layout and comments options](references/mobile-and-comments.md)
- [Theme conversion guide](references/换肤-token-flip.md)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [HTML/CSS/JavaScript deck files, Markdown guidance, shell commands, and TOML/SQL configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responsive, slide-based web decks with optional autoplay, analytics, comments, and Cloudflare Pages deployment.]

## Skill Version(s):

1.3.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
