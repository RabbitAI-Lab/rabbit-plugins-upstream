## Description:

Analyzes images or videos of crop leaves, buds, and fruit for common pests and returns pest types with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farmers, growers, and agricultural advisors can submit crop images or videos to identify common pests and receive a structured observation with pest types, estimated counts, confidence scores, and a report link. The results support early assessment; the skill does not provide pesticide or pest-control recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags credential handling and media uploads, including uploads despite the --export-env-only option; --api-url does not change the destination.

Mitigation: Review credential handling and automatic account enrollment before installing. Use an isolated workspace and non-sensitive media, and request fixes that separate secrets from identity fields and protect stored tokens and logs.

Risk: The bundled files do not establish the provider's media-retention practices or server-side account isolation.

Mitigation: Do not send sensitive media; confirm retention and account-isolation practices with the provider before relying on them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Markdown]

**Output Format:** [Structured pest-analysis text or JSON with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pest types, estimated counts, confidence scores, and report links; no pesticide or treatment advice.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
