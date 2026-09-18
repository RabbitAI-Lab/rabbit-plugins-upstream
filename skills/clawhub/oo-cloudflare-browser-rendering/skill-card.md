## Description:

Cloudflare Browser Run helps agents render URLs or raw HTML through an OOMOL-connected Cloudflare Browser Run account and return rendered HTML, Markdown, structured JSON, links, or selected page elements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Cloudflare Browser Run through the OOMOL oo CLI for browser-rendered page extraction, including HTML, Markdown, JSON, links, account listing, and selected element scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts executed on the user's machine.

Mitigation: Review the installer path before use, prefer a verified package or pinned installer, and verify checksums or signatures when available.

Risk: The skill can access a connected Cloudflare Browser Run account through OOMOL-managed credentials.

Mitigation: Connect only the intended Cloudflare Browser Run account and confirm account IDs with list_accounts before running account-specific actions.

Risk: Rendered page extraction can return large or sensitive page content from supplied URLs or HTML.

Mitigation: Use scoped inputs, avoid submitting confidential pages unless authorized, and review extracted content before sharing it outside the current workflow.

## Reference(s):

- [Cloudflare Browser Run documentation](https://developers.cloudflare.com/browser-run/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-browser-rendering)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Skill icon](https://static.oomol.com/logo/third-party/cloudflare_browser_rendering.svg)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live action schemas before running OOMOL connector actions and to return connector results such as rendered HTML, Markdown, JSON, links, account data, or scraped elements.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
