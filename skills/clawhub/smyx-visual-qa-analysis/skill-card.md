## Description:

Answers open-ended questions about image content and provides cloud-based analysis reports and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People analyzing images can ask natural-language questions about visual content, view generated answers and reports, and retrieve previous reports from the cloud.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or videos, URLs, and questions are sent to the LifeEmergence cloud service.

Mitigation: Obtain user consent before sending content and avoid sensitive media unless the service's handling is acceptable.

Risk: The skill can silently create or reuse a local identity and store tokens in a workspace database.

Mitigation: Disclose account creation and token storage before use; protect and periodically review the local workspace.

Risk: The skill can fetch cloud report history beyond a single image question.

Mitigation: Make history access explicit and review retrieved records and report links before sharing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Natural-language answers and reports, JSON analysis results, and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to cloud reports; verify important model-generated answers independently.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata; packaged frontmatter says 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
