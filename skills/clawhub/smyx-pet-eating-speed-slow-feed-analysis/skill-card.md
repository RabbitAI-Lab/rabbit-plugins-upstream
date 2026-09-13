## Description:

Analyzes pet food-bowl videos or video URLs to estimate eating start and end times, eating speed, and whether slow-feeding intervention guidance may be appropriate without providing disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet feeding videos, produce structured eating-speed reports, query prior cloud reports, and guide non-diagnostic slow-feeding interventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload pet videos or ask a server to fetch supplied video URLs.

Mitigation: Review the publisher, endpoint configuration, and data-handling expectations before using private videos.

Risk: The skill can create or reuse a hidden account identity and store service tokens locally.

Mitigation: Use approved accounts only, inspect local token storage, and rotate or remove tokens after testing.

Risk: Security evidence flags unsafe default HTTP endpoints and plaintext local token storage.

Mitigation: Configure trusted HTTPS production endpoints and remediate token storage before using real accounts or sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured Markdown or JSON analysis reports with report links and intervention guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a file when requested.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
