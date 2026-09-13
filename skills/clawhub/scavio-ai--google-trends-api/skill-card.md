## Description:

Query Google Trends for interest-over-time, by-region, and related queries for a keyword, and pull real-time trending searches for a country as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, marketers, SEO researchers, and market researchers use this skill to retrieve Google Trends interest-over-time, regional interest, related queries or topics, and real-time country-level trending searches through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party Scavio API key and each request consumes credits.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, confirm trust in Scavio before use, and monitor credit consumption.

Risk: Google Trends values can be misread as absolute search counts.

Mitigation: Describe returned values as relative 0-100 interest indexes and do not fabricate values, regions, or trending terms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-trends-api)
- [Scavio Google Trends API Documentation](https://scavio.dev/docs/google-trends?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-trends-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-trends-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, json]

**Output Format:** [Markdown guidance with shell and code examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented endpoint consumes 1 credit; Google Trends values are relative 0-100 interest indexes.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
