## Description:

Analyzes aquarium pet videos or video URLs through a remote health-analysis API to identify visible health signals such as scales, fins, coloration, activity level, and potential disease indicators, then returns a health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and aquarium hobbyists use this skill to submit aquatic pet videos or URLs for health-oriented analysis and structured reporting. The output is health guidance for review and does not replace professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos, supplied URLs, report history, and account-linked identifiers may be sent to or retrieved from a remote service.

Mitigation: Review the configured endpoint, data retention, and deletion process before use; avoid submitting sensitive private videos or signed/internal URLs until the publisher clarifies handling.

Risk: The skill may create or reuse identity state and persist service tokens locally.

Mitigation: Run in a controlled workspace, inspect or reset local identity/token storage before sharing the environment, and rotate credentials if the workspace is exposed.

Risk: Security evidence reports a mismatch between HTTPS claims and apparent non-HTTPS development endpoint defaults.

Mitigation: Verify that production HTTPS endpoints are configured before installation or execution.

Risk: Health-analysis output may be incomplete, incorrect, or unsuitable for urgent care decisions.

Mitigation: Treat reports as informational guidance and consult a qualified aquatic veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface reference](references/api_doc.md)
- [SMYX analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON health-analysis report with optional report image/export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a user-specified file path when invoked with an output argument.]

## Skill Version(s):

1.0.12 (source: ClawHub server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
