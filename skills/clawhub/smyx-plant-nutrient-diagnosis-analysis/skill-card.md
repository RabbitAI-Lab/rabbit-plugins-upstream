## Description:

Diagnoses likely plant nutrient deficiencies from plant leaf images or videos, returning likely deficient nutrient elements, confidence, and fertilization direction guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit plant leaf media for cloud-based nutrient deficiency diagnosis and to retrieve account-linked diagnosis history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media files or media URLs are sent to the Life Emergence cloud service for analysis.

Mitigation: Use only media and URLs approved for external processing; avoid sensitive local files and private or internal URLs.

Risk: The skill creates or reuses a persistent local identity and stores service tokens in workspace data.

Mitigation: Run it only in workspaces where persistent local account data is acceptable, and clear local data or isolate workspaces between users.

Risk: History lookup can return account-linked diagnosis reports.

Mitigation: Treat history results as user or account data and invoke history lookup only when the user asks for prior reports.

Risk: Nutrient deficiency symptoms can overlap, so diagnosis and fertilization guidance may be uncertain.

Mitigation: Use results as advisory input and confirm with plant context, soil testing, or an agricultural expert before making treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON text, with an optional saved result file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and account-linked history lists; local media inputs are size-limited to 10 MB.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
