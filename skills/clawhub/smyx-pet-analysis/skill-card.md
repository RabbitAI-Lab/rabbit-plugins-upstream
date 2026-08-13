## Description:

Analyzes pet image, video, or URL inputs through a cloud pet health service and returns a structured Pet Safety Guardian health report with potential disease signals, care suggestions, history results, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to submit pet media or media URLs for health-oriented analysis, receive structured diagnostic-style guidance, and query prior pet health analysis reports. Results are health reference material and should not replace professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, media URLs, and account-linked identifiers are sent to the Life Emergence cloud service for analysis.

Mitigation: Install and use only when the provider's retention, account-scoping, and cloud-processing practices are acceptable for the submitted pet media.

Risk: The skill may silently create or reuse account identities, retrieve history, and store service tokens in a local SQLite-backed data directory.

Mitigation: Review and protect the local data directory, avoid shared or sensitive workspaces, and clear stored tokens or local user data when the skill is no longer needed.

Risk: Health analysis output can be incomplete or misleading if treated as a veterinary diagnosis.

Mitigation: Use reports as reference guidance and consult a professional veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Pet analysis API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Life Emergence skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON text, with optional report links and optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud APIs, upload local media or submit media URLs, query history, and save results to a caller-specified output path.]

## Skill Version(s):

999.999.1003 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
