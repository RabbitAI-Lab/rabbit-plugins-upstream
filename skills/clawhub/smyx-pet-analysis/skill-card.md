## Description:

Analyzes submitted pet video files or video URLs for cat, dog, bird, or other pet health signals and returns a structured Pet Safety Guardian health report with findings, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to submit pet media or video URLs for health-oriented analysis, retrieve structured diagnostic-style reports, and query prior report history associated with the user's local or generated identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or submitted video URLs are uploaded to the skill's configured service.

Mitigation: Use only media the user is authorized to submit, disclose off-device processing before use, and avoid sensitive background content in uploaded files.

Risk: The skill automatically creates or reuses a local or generated identity and may associate reports with that identity.

Mitigation: Review identity-handling behavior before deployment and avoid exposing generated identifiers in user-facing output.

Risk: Account tokens may be stored in a workspace SQLite database.

Mitigation: Run the skill in a controlled workspace, restrict database file access, and clear local state when the skill is no longer needed.

Risk: Bundled endpoint configuration includes dev or HTTP endpoints unless corrected by the publisher.

Mitigation: Verify endpoint configuration before installation or execution and prefer production HTTPS endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet health analysis API documentation](artifact/references/api_doc.md)
- [Analysis API error-code reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text, with optional report-link output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report text to a local output file when requested.]

## Skill Version(s):

999.999.1005 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
