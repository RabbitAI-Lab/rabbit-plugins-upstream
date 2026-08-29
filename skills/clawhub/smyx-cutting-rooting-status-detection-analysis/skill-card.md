## Description:

Analyzes images or videos of plant cuttings in transparent containers to detect visible root primordia, classify rooting stage, and provide transplant-timing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, propagation operators, and agricultural researchers use this skill to monitor rooting progress from transparent-container imagery without disturbing the cutting. It can return rooting-stage assessment, visible root-point counts or distribution, report links, and account-scoped historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded plant images or videos may be processed by cloud services.

Mitigation: Review endpoint, retention, and permission documentation before installation, and avoid submitting sensitive media unless the deployment policy permits it.

Risk: The skill can automatically create or reuse account identity and store identity or token data locally.

Mitigation: Use an isolated test account for review and confirm cleanup controls for local identity and token state before production use.

Risk: Historical report lookup is account-scoped and may retrieve cloud-stored analysis history.

Mitigation: Confirm that users understand the history lookup behavior and that access controls match the intended deployment.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured rooting-stage assessment, visible root-point details, transplant-timing guidance, report links, or historical report tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
