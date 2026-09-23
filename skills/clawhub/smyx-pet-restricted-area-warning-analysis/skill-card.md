## Description:

Monitors pet videos for restricted-area intrusion, dining-table climbing, and trash rummaging, then returns alert-oriented analysis results and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze home pet monitoring videos or URLs for restricted-zone and prohibited-behavior alerts, and to retrieve cloud-stored historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home monitoring media may be uploaded to a remote analysis service.

Mitigation: Use non-sensitive test media until the publisher documents the backend, data handling, retention, and deletion controls.

Risk: The skill can silently create or reuse an account identity and store authentication tokens locally.

Mitigation: Use an isolated test identity, review local token storage before use, and avoid real accounts unless identity and token controls are documented.

Risk: Configuration and scan evidence indicate unsafe or under-scoped network paths, including development or non-HTTPS endpoints.

Mitigation: Require HTTPS-only production endpoints and restrict authenticated requests to trusted hosts before deployment.

Risk: Historical report queries may expose cloud-stored monitoring reports.

Mitigation: Confirm access controls, user consent, report retention, and deletion options before enabling history lookup.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report text with optional report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a user-provided local file path.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact/SKILL.md frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
