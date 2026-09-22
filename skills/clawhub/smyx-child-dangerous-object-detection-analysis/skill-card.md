## Description:

Analyzes child activity-zone images or videos to detect dangerous object contact or socket-contact behaviors and return structured alert reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill with child activity-zone images or videos to identify contact with knives, scissors, medicine, lighters, electrical sockets, and similar hazards. It returns alert-oriented structured reports, report links, or history listings for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-monitoring videos or home-interior media may be uploaded to a remote service.

Mitigation: Use only with appropriate guardian consent, minimize uploaded media, and confirm retention, access-control, and deletion policies before deployment.

Risk: The security evidence reports unsafe development network settings and HTTP endpoint concerns.

Mitigation: Remove development endpoints and enforce HTTPS production endpoints before installing or running the package.

Risk: The skill can create or reuse a persistent identity and store account tokens locally.

Mitigation: Document identity and report retention controls, isolate credentials, and clear local token or database state between users and environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-dangerous-object-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an optional output file when requested; accepts local file paths or video URLs as analysis inputs.]

## Skill Version(s):

1.0.5 (source: server release metadata; SKILL.md frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
