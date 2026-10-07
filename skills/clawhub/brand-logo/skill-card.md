## Description:

Retrieves a logo image for one public domain using ReplyNodes' read-only, unauthenticated endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents retrieving a logo image for one known public domain can use this skill for a focused lookup, not broader brand research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A publicly retrievable logo may still be subject to trademark or copyright restrictions.

Mitigation: Preserve the source domain and confirm usage rights with the rights holder before reuse.

Risk: A fallback image or cached result may be mistaken for a current official logo.

Mitigation: Check fallback and cache response headers; identify placeholders and avoid claiming they are verified logos.

Risk: Using single-domain lookup for bulk crawling exceeds the intended scope.

Mitigation: Limit requests to individual known domains and respect HTTP errors and service limits.

## Reference(s):

- [ClawHub brand-logo release](https://clawhub.ai/replynodes-ai/skills/brand-logo)
- [ReplyNodes public logo endpoint](https://img.replynodes.com)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Image bytes with brief text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One domain per request; results may be a detected logo, favicon, or placeholder.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
