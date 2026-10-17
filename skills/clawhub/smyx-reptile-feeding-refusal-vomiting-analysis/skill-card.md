## Description:

Analyzes reptile feeding videos to flag possible prey refusal or regurgitation and provide a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers, breeders, and developers use enclosure-camera feeding footage or video URLs to check for feeding refusal or regurgitation, review alerts, and retrieve past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feeding videos or URLs and report queries are sent to the publisher's cloud service.

Mitigation: Share only media you are authorized to upload and review the publisher's data-handling terms before use.

Risk: The skill creates or reuses a local identity, can read a workspace API-key file, and stores authentication tokens in local SQLite for later report access.

Mitigation: Run it only in a trusted workspace, limit access to local credentials and the database, and remove stored identity data when no longer needed.

Risk: A video-based alert may be mistaken for a veterinary diagnosis.

Mitigation: Treat results as observational guidance; consult a reptile veterinarian for persistent refusal, regurgitation, or health concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report or Markdown table; optional JSON-formatted results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a local file and retrieve cloud-hosted historical reports.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; bundled frontmatter lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
