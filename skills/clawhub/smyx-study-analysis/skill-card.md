## Description:

Analyzes child or student study videos to identify learning-behavior patterns, generate structured reports, and provide family education improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as parents, guardians, educators, or agents acting for them use this skill to submit study-session media, request behavior analysis, review structured reports, and retrieve prior cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child or student media and identity-linked reports are uploaded to a remote analysis service.

Mitigation: Use only with appropriate consent, avoid unnecessary sensitive media, and require clear retention and deletion commitments before deployment.

Risk: The security guidance flags packaged development HTTP configuration and insufficient trusted-origin enforcement.

Mitigation: Deploy only after the publisher enforces HTTPS-only trusted service endpoints and removes private or development HTTP origins from the package.

Risk: Local account tokens and internal identifiers may be persisted by the skill.

Mitigation: Run in an isolated workspace with restricted file permissions, rotate credentials after testing, and avoid shared environments for child or student data.

Risk: Generated study-behavior suggestions may be mistaken for professional educational or psychological assessment.

Mitigation: Present reports as family education reference material and route serious learning or behavioral concerns to qualified teachers or counselors.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON analysis reports with report links; optional saved text output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include concentration, posture, habit, risk, and family education suggestion sections.]

## Skill Version(s):

1.0.16 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
