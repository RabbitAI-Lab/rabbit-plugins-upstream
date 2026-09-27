## Description:

Identifies bird species in target-area images or videos, supports at least 500 common species and custom model training, and returns structured bird recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecological observers use this skill to identify bird species in supplied images or videos and retrieve structured recognition reports or report history through a cloud API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bird images or videos are sent to the Life Emergence cloud service for analysis.

Mitigation: Prefer non-sensitive media unless the publisher documents retention, deletion, and handling controls that meet the deployment requirements.

Risk: The skill may silently create or reuse an external identity and store local access tokens in a workspace SQLite database.

Mitigation: Review identity, account deletion, and token cleanup controls before installation or shared-workspace use.

Risk: Cloud report history can be retrieved through the skill.

Mitigation: Use account separation and access controls appropriate for the reports that may be available through the linked cloud account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)
- [API 接口文档](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with JSON report content and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write recognition results to a caller-specified output file.]

## Skill Version(s):

1.0.21 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
