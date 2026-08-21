## Description:

Fetches fresh, on-demand creator and content data across TikTok, Instagram, Facebook, and YouTube, including profile/page information, latest content, and media details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, creator operations, and research users use this skill to retrieve freshness-critical creator profile, content, and post data, compare it with baseline assumptions, and summarize decision-relevant deltas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator identifiers and query data are sent externally through a hosted gateway by default.

Mitigation: Review data-sharing requirements before use, avoid sending sensitive identifiers, and configure an approved API key and gateway when external transmission must be controlled.

Risk: The skill creates and transmits a stable local install identifier.

Mitigation: Assess this identifier in privacy review and change or remove the behavior before deployment if persistent local tracking is not acceptable.

Risk: Free hosted-gateway quota can be exhausted and return HTTP 429 responses.

Mitigation: Use an owned SCRUMBALL_API_KEY for production use and surface quota-exhaustion guidance clearly when 429 responses occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-realtime-enrichment)
- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operation Manifest](references/operations.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON-backed API results and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The output contract asks for freshness, key deltas, decision impact, and a next step.]

## Skill Version(s):

1.0.4 (source: evidence.release.version and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
