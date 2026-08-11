## Description:

Analyzes livestock and poultry vocalizations for abnormal acoustic patterns such as coughing, wheezing, painful screams, and hoarse calls, then returns respiratory health risk hints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, veterinarians, and developers can use this skill to submit livestock or poultry audio/video for non-contact herd or flock screening, abnormal-call event detection, respiratory risk hints, and report-history lookup. Its outputs are screening aids, not disease diagnoses or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock audio/video files or URLs are sent to lifeemergence.com services for cloud analysis.

Mitigation: Use only recordings approved for that service and avoid submitting unrelated sensitive audio or video.

Risk: Authentication tokens may be stored locally in a SQLite database under the workspace data directory.

Mitigation: Review local retention and workspace access controls, and clear stored credentials when they are no longer needed.

Risk: Cloud report history is fetched under an automatically resolved identity.

Mitigation: Confirm the account or tenant context before querying history and avoid sharing returned report links broadly.

Risk: Respiratory health risk hints could be mistaken for diagnosis or treatment guidance.

Mitigation: Treat outputs as screening prompts and confirm animal-health decisions with a qualified veterinarian or laboratory testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocalization-health-analysis-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis reports with command examples and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a user-specified file; history queries are formatted as a Markdown table.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
