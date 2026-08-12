## Description:

Search Harvester discovers candidate websites for link building and outreach by querying search engines through rotating Tor exits, deduplicating results, triaging liveness and anti-bot barriers, and exporting scored candidate lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toniilic](https://clawhub.ai/user/toniilic)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, link builders, founders, and marketers use this skill to discover directories, submission platforms, blogs, and listicles where they can submit a site or client site. It is intended for authorized, low-volume candidate discovery when ordinary server-side search requests are blocked by captchas or anti-bot controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes scraping traffic through Tor and optional public proxies, which may create privacy, compliance, and website terms-of-service risks.

Mitigation: Install only for an intentional Tor-based scraping workflow, use it only for authorized search and outreach activity, avoid sensitive or regulated queries, and prefer official APIs or approved data sources when available.

Risk: The setup examples include running Tor for network traffic routing, and copying privileged service commands directly can expand operational risk.

Mitigation: Run Tor as a constrained unprivileged service and review the local service configuration before deployment.

Risk: Automated search-engine requests can trigger anti-bot controls or return unreliable results from blocked exits.

Mitigation: Use the documented low-volume rotate-and-retry behavior, treat block responses as failures rather than results, and review harvested candidates before acting on them.

## Reference(s):

- [Skill homepage](https://github.com/toniilic/scraper-skill)
- [ClawHub skill page](https://clawhub.ai/toniilic/skills/scraper-skill-main)
- [OpenClaw skill format](https://docs.openclaw.ai/clawhub/skill-format)
- [OpenClaw publishing](https://docs.openclaw.ai/clawhub/publishing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Ranked markdown candidate list and terminal progress output, with setup and execution commands for the local harvesting workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Linux with tor, curl, python3, and nc; uses a local Tor SOCKS and control port; optional liveness triage checks harvested URLs before ranking.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
