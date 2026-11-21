## Description:

Accepts a local video or video URL of a cat, dog, bird, or other pet, sends it to a remote service for analysis, and returns a structured health report with potential concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers can submit a pet video for remote health analysis and review a structured report with potential concerns and care suggestions. They can also retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious because it reports undeclared behavior and options that may trigger analysis or remote data handling.

Mitigation: Before use, verify that export-only requests cannot analyze or upload video, disclose remote processing and account registration, and limit history lookup and file changes to what is expected.

Risk: Potential disease alerts could be mistaken for a veterinary diagnosis.

Mitigation: Treat the report as health reference information and consult a veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Markdown-formatted text containing structured JSON results and a report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include potential health concerns and care suggestions; results are for reference and do not replace veterinary diagnosis.]

## Skill Version(s):

999.999.1014 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
