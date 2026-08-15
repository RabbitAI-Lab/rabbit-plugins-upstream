## Description:

Search G2, the B2B software review site, read a full product profile with pricing and features, and pull faceted reviews with exact per-star counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to query Scavio's G2 endpoints for B2B software search, product profiles, pricing details, alternatives, and faceted review research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SCAVIO_API_KEY and sends it to Scavio's API for each request.

Mitigation: Use a scoped Scavio API key where possible, store it only in the runtime environment, and rotate it if exposed.

Risk: Every G2 endpoint call spends 5 Scavio credits, and multi-page review pulls can spend credits quickly.

Mitigation: State the expected credit cost before running requests, avoid looping over product profiles, and bound pagination before starting.

Risk: Filtered G2 review calls can return zero results for ambiguous reasons, including unsupported or overly narrow filters.

Mitigation: Re-check unfiltered or with broader filters before reporting that a segment has no reviews or no opinion.

## Reference(s):

- [Scavio G2 Search Documentation](https://scavio.dev/docs/g2-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-g2)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration]

**Output Format:** [Markdown with JSON request examples and Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide the agent to call Scavio's G2 API and return structured JSON-derived findings.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
