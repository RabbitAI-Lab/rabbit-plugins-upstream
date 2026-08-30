## Description:

Search Capterra for B2B software, read a full product profile with the complete pricing table and 25 reviews included, and page deeper reviews with per-criterion scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, software buyers, and research teams use this skill to query Capterra through Scavio for B2B software discovery, pricing research, review mining, competitive intelligence, and product comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party API provider and requires a SCAVIO_API_KEY.

Mitigation: Install only when use of Scavio is acceptable, keep the API key out of source code and logs, and load it from the environment or a secret store.

Risk: Every endpoint call spends credits, and duplicate or unnecessary review requests can waste credits.

Mitigation: Use the product endpoint before deeper review pages, do not request review page 1 separately, stay within the page cap, and reuse returned slugs or review URLs.

## Reference(s):

- [Scavio Capterra Search Documentation](https://scavio.dev/docs/capterra-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/capterra-reviews-api)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, JSON request details, and Python or JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses use structured JSON envelopes with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
