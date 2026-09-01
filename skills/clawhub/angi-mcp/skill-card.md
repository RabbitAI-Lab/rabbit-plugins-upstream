## Description:

Read angi.com from a shell with fpx to find home-service providers by trade and city, inspect profiles, ratings, reviews, and list trade/city taxonomy without running the angi-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to gather Angi public provider, profile, rating, review, and trade/city taxonomy data from shell workflows. Optional signed-in account reads are limited to Angi pages the user intentionally pairs through their browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing fpx/Transporter with Angi allows the skill to fetch pages through the user's browser tab.

Mitigation: Pair only www.angi.com for public provider searches, and pair my.angi.com only when the user intentionally wants signed-in account pages read.

Risk: Optional signed-in account reads can expose the user's own Angi projects or reviews when my.angi.com is paired.

Mitigation: Use the signed-in workflow only with explicit user intent, and keep the documented fetch-only profile without cookie, storage, or header scope.

Risk: Angi result payloads include duplicate provider records and undocumented fields that may change.

Mitigation: Resolve trade and city slugs from sitemaps, use --dedupe id on search pages, and pass through unknown fields rather than assuming their meaning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC extractor](references/rsc.mjs)
- [Angi](https://angi.com/)
- [Angi state/category sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)
- [Angi plumbing geo sitemap example](https://www.angi.com/sitemap/angi-geocat-plumbing.xml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and code snippets; extractor usage emits JSON arrays for downstream jq processing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented workflows using fpx, curl, node, and jq; no cookie, storage, or header scope is declared by the skill.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
