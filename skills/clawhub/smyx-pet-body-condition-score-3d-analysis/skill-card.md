## Description:

Analyzes multi-angle pet videos to reconstruct body shape and estimate a 1–9 Body Condition Score (BCS), returning structured observations without diagnosing disease or recommending treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet care platform developers and operators can use multi-angle pet videos to request a visual BCS estimate and retrieve prior reports for weight-management tracking. The results are observational and do not replace veterinary assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that videos may still be submitted when configuration-only mode is selected.

Mitigation: Use a corrected release that honors configuration-only mode before relying on that setting.

Risk: Selected videos and URLs are sent to lifeemergence.com, and account creation and saved credential behavior are not clearly explained.

Mitigation: Avoid sensitive household footage and private access links, protect the workspace database, and use credentials dedicated to this service.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON or text reports; history listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a visual BCS estimate on a 1–9 scale and standardized observations; estimates may differ from hands-on assessment.]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
