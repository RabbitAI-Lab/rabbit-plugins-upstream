## Description:

Analyzes pet activity videos or video URLs to identify over-excitement behaviors, score risk, and return calming guidance with report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as pet owners, boarding centers, daycare operators, and training schools use this skill to submit pet activity videos or URLs for behavior-risk analysis and calming recommendations. It supports behavior safety review and report history lookup, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded pet videos or video URLs may be sent to a backend service, and report history is retrieved from cloud APIs.

Mitigation: Install only where those media and cloud-history data flows are acceptable; use approved service endpoints and avoid sensitive footage unless data handling has been reviewed.

Risk: The skill may create or reuse a local identity and store returned authentication tokens.

Mitigation: Run it in a controlled workspace, restrict access to local state, and clear stored identity or token data after evaluation or use.

Risk: The evidence warns that shipped dev or private endpoint configuration may require verification or correction.

Mitigation: Review configuration before execution and route requests only to trusted, intended backend services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-excitement-calming-guide-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API error reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Structured report text or JSON, with Markdown tables for history listings and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior assessment, calming recommendations, status messages, and report export links when returned by the backend service.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
