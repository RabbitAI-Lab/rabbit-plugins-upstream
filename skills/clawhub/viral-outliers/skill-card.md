## Description:

Find viral outlier posts on TikTok, Instagram and YouTube, pull creator stats, transcribe and analyse videos, build competitor watchlists, and crawl profiles on demand. Prepaid credits, MCP or REST.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matsclaes2](https://clawhub.ai/user/matsclaes2)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use the skill to find and analyze high-performing public social posts, compare creators, monitor selected profiles, and turn examples into niche-adapted content ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated use grants access to an account, and some actions spend prepaid credits.

Mitigation: Use a dedicated, revocable API key or OAuth, review paid actions, monitor the credit balance, and keep credentials out of shell history.

Risk: Scheduled profile tracking and email alerts can continue monitoring profiles, and alert emails consume credits.

Mitigation: Choose tracking schedules and alerts deliberately, and review or stop them when they are no longer needed.

Risk: The external CLI implementation and hosted backend were not audited.

Mitigation: Prefer the documented REST or hosted MCP route; if using the CLI, review and pin an exact release and protect credentials.

## Reference(s):

- [Viral Outliers documentation](https://viraloutliers.com/docs)
- [Getting started](https://viraloutliers.com/docs/getting-started)
- [OpenAPI specification](https://viraloutliers.com/openapi.json)
- [Getting started reference](references/getting-started.md)
- [Skills reference](references/skills.md)

## Skill Output:

**Output Type(s):** [Analysis, API data, Text, Configuration instructions]

**Output Format:** [Structured API data and natural-language analysis in text or Markdown, with setup examples in shell, YAML, and JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some actions use prepaid credits; results depend on public profiles available to the service.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
