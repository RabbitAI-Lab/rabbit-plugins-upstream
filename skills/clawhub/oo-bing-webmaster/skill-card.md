## Description:

Provides OOMOL-connected access to Bing Webmaster Tools for reading and managing sites, verification, sitemaps, URL submissions, crawl and indexing reports, and related SEO settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO operators, and site administrators use this skill to inspect Bing Webmaster Tools data and run site-management workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands without verification.

Mitigation: Review the OOMOL CLI installation path before installing, prefer a documented version-pinned manual install, and do not let an agent run curl|bash or irm|iex automatically.

Risk: The skill can perform write or destructive Bing Webmaster Tools actions.

Mitigation: Require user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bing-webmaster)
- [Bing Webmaster Tools](https://www.bing.com/webmasters/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and the bing_webmaster connector; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
