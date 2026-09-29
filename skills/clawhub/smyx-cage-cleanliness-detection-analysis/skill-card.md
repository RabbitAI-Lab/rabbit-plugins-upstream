## Description:

Analyzes fixed-camera pet cage images or videos to estimate feces and urine coverage, score cleanliness, trigger cleaning alerts, and return structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet boarding centers, pet shops, animal hospitals, and breeding facilities can use this skill to analyze cage floor images or videos for cleanliness monitoring. The skill helps operators identify waste coverage, generate a cleanliness score, and review current or historical reports without providing medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cage images, videos, URLs, and report history are processed by the Life Emergence cloud service.

Mitigation: Use the skill only for media appropriate for that service, and require publisher documentation for retention, access, and processing controls before sensitive facility use.

Risk: The skill creates or reuses an internally managed identity, stores service tokens locally, and retrieves account-linked history.

Mitigation: Run it only in controlled workspaces, protect local data and configuration files, and review token storage, account ownership, and history-access controls before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface document](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [JSON or Markdown reports with report links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured analysis results, cleanliness scores, cloud report export links, and historical report lists.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
