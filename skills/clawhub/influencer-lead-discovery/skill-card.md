## Description:

Find influencers and creators across TikTok, Instagram, and YouTube by keyword; expand similar creators, enrich profiles, and build outreach-ready lead lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, partnerships, and growth teams use this skill to discover, enrich, and rank creator candidates for campaigns across TikTok, Instagram, and YouTube. It helps assemble lead shortlists with selection rationale, data-quality caveats, and outreach next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, creator identifiers, optional API keys, and a persistent install identifier may be sent to a third-party creator-data service.

Mitigation: Use only a trusted SCRUMBALL_BASE_URL, avoid sensitive campaign data in requests or ambient .env files, and review whether sharing those identifiers is acceptable.

Risk: A configurable external API gateway changes where requests and related metadata are sent.

Mitigation: Pin SCRUMBALL_BASE_URL to an approved endpoint and inspect local environment files before use.

Risk: Influencer discovery and outreach can implicate privacy, anti-spam, and platform rules.

Mitigation: Review intended outreach against applicable privacy, anti-spam, and platform policies before acting on lead lists.

## Reference(s):

- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operation Manifest](references/operations.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with ranked lists, rationale, caveats, next steps, and optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API operation identifiers, platform profile identifiers, data-quality caveats, and outreach recommendations.]

## Skill Version(s):

1.0.4 (source: server release metadata and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
