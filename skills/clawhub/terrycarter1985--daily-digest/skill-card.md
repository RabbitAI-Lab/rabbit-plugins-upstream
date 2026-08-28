## Description:

Generate a structured daily digest from multiple source URLs for daily briefings, standups, or knowledge sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to fetch several user-provided URLs and turn them into a consolidated Markdown digest with an overview, per-source takeaways, and notable quotes or statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can summarize internal pages, confidential documents, or user-provided URLs whose contents should not be redistributed.

Mitigation: Use public or approved URLs, and confirm that any requested email, Slack, or other delivery channel is authorized for the content.

Risk: Paywalled, JavaScript-heavy, or very large pages may produce incomplete source text, which can make a digest incomplete or misleading.

Mitigation: Review skipped URLs, truncation notes, and important quotes or statistics against the original sources before relying on the digest.

## Reference(s):

- [Daily Digest on ClawHub](https://clawhub.ai/terrycarter1985/skills/daily-digest)
- [Publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown digest with headings, bullet takeaways, source domains, and quoted notable items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May note skipped URLs, fetch failures, or truncated sources in the digest footer.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
