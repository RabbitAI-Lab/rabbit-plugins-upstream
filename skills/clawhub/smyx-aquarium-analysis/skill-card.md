## Description:

Analyzes aquarium pet image or video inputs through the publisher's cloud API to produce a health report covering visible traits, potential disease signals, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and aquarium caretakers use this skill to submit aquatic pet media for cloud-based health analysis, then review structured findings, care suggestions, historical report data, and report export links. The report is informational and is not a substitute for professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded aquarium media is sent to the publisher's cloud service for analysis.

Mitigation: Install and run the skill only when users are comfortable sharing the submitted media with the publisher's service; avoid sensitive media and review service policies before normal use.

Risk: History lookups are account-linked and the skill may store generated or reused identity/session data locally.

Mitigation: Review local data handling and account-linking behavior before deployment, and provide users a clear process for clearing or resetting local identity/session data where supported.

Risk: Evidence.security reports inconsistent cloud endpoints and a wrong history command in the release.

Mitigation: Verify production HTTPS endpoint configuration and correct the documented history command before normal use.

Risk: The generated health report may be incomplete or inaccurate for real animal care decisions.

Mitigation: Present results as informational triage guidance and direct users to consult a qualified aquatic veterinarian for diagnosis or treatment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Markdown or JSON health report with report export links; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account-linked history results and publisher-hosted report image URLs.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
