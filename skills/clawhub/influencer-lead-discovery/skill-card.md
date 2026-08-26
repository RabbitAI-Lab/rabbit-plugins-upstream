## Description:

Find influencers and creators across TikTok, Instagram, and YouTube by keyword, expand similar creators, enrich profiles, and build outreach-ready lead lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, partnerships, and growth teams use this skill to discover, enrich, compare, and rank creator candidates for influencer campaigns across TikTok, Instagram, and YouTube.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill creates a persistent install identifier and sends it with API requests.

Mitigation: Review the skill before installing in tracking-sensitive environments and remove the local install identifier if stable per-install tracking is not acceptable.

Risk: The release security summary says the skill can send outbound requests to an environment-configured endpoint.

Mitigation: Use only a trusted SCRUMBALL_BASE_URL and avoid placing unrelated secrets in .env files used by this skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-lead-discovery)
- [API Index](artifact/references/api-index.md)
- [Request and Response Guide](artifact/references/request-response.md)
- [Operation Manifest](artifact/references/operations.json)
- [Quota and API Key Setup](https://data.scdata.cc/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance]

**Output Format:** [Markdown shortlist with operation calls and JSON API responses as supporting evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns ordered creator candidates with platform identifiers, selection rationale, risks, and outreach or testing next steps.]

## Skill Version(s):

1.0.5 (source: server release evidence and artifact/config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
