## Description:

Maps sampled YouTube topic and format coverage into an evidence-based content brief using Crawlora search, channel, video, and caption data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Content strategists and creators use this skill to examine sampled YouTube topics, channels, formats, and available captions, then develop testable content ideas without claiming to measure total coverage or unmet demand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API key and YouTube search parameters or video/channel identifiers are sent to Crawlora.

Mitigation: Use bounded public YouTube research; do not put private notes, secrets, or unrelated sensitive data in query parameters.

Risk: Sample gaps, view counts, and imperfect or unavailable captions can mislead content-planning conclusions.

Mitigation: Record sampling and caption limitations, distinguish metadata-only coding, and frame demand or growth claims as hypotheses.

## Reference(s):

- [YouTube endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/youtube-content-gap-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown topic-by-format/channel matrix and prioritized idea brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records sampled scope, source links and dates, unique-video counts, caption availability, and uncertainty.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
