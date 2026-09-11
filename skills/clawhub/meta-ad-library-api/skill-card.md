## Description:

Search the Meta Ad Library by keyword or Facebook Page id and walk full cursor pagination through every ad, with creative, run dates, platforms and political spend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing researchers use this skill to search public Facebook and Instagram ad data, inspect creative details, and build capped ad datasets through Scavio's Meta ads API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and sends requests to Scavio.

Mitigation: Install only if the user accepts Scavio API use, keep SCAVIO_API_KEY in the environment or a secret store, and avoid committing credentials.

Risk: Full cursor pagination can consume paid credits because each page costs one credit.

Mitigation: Set an explicit page or credit cap before crawling and tell the user the intended budget.

Risk: Ad Library totals and spend fields can be misunderstood.

Mitigation: Do not present capped totals as exact, and do not treat null commercial spend or reach as zero because Meta publishes those fields for political and issue ads only.

Risk: Optional SDK installation changes the execution environment.

Mitigation: Prefer direct HTTPS examples or install optional SDKs in an isolated project or virtual environment.

## Reference(s):

- [Scavio Meta Ads Search documentation](https://scavio.dev/docs/meta-ads-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=meta-ad-library-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=meta-ad-library-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/meta-ad-library-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API request examples, shell commands, and structured-response notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on HTTPS API calls that return JSON envelopes and on bounded cursor pagination.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
