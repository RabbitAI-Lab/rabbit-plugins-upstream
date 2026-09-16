## Description:

Runs Cloudflare Browser Run actions through the OOMOL oo CLI to render pages, extract page content, discover links, scrape elements, and list accessible Cloudflare accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to render URLs or raw HTML with Cloudflare Browser Run, then return HTML, Markdown, structured JSON, discovered links, or selected scraped elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run curl-to-shell or PowerShell installer pipelines automatically; review the installer and use a verified, pinned, or signed release when available.

Risk: URLs or raw HTML submitted through the skill may be processed by connected OOMOL and Cloudflare services.

Mitigation: Avoid submitting sensitive content unless the connected account, service terms, and data-handling requirements are acceptable.

Risk: The skill depends on a connected OOMOL account and Cloudflare Browser Run credentials.

Mitigation: Install only if the OOMOL publisher and connected-account flow are trusted for the intended workspace.

## Reference(s):

- [Cloudflare Browser Run documentation](https://developers.cloudflare.com/browser-run/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-browser-rendering)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rendered HTML, Markdown, structured JSON, discovered links, scraped element data, account lists, or setup guidance returned from Cloudflare Browser Run via OOMOL.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
