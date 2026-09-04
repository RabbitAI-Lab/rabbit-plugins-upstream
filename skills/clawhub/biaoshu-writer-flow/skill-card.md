## Description:

Helps bidding teams interpret tender files, generate editable .docx bid documents, review submissions for compliance risks, and compare two or three bid files for duplicate or similarity signals using the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding and proposal teams use this skill to process tender and bid files into structured tender interpretations, editable bid documents, compliance review reports, and similarity-risk summaries before submission.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain commercially sensitive, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm user awareness and consent before upload, use only user-selected local files, and avoid processing files the user is not authorized to share.

Risk: The API key is a full account credential stored locally in the skill configuration.

Mitigation: Have the user place the key in the local config file themselves, do not ask for or echo the key in chat, and do not forward URLs containing credential parameters.

Risk: Generated bid documents, reports, and local project-name caches may remain on local disk, while cloud-side task results and .docx outputs are retained for a limited period under the user's account.

Mitigation: Store outputs only in the declared output directory, tell the user where files are written, and review the platform retention and billing notes before use.

Risk: Duplicate-checking and compliance results are risk signals and may be incomplete or require legal/procurement judgment.

Mitigation: Present findings as submission-preparation guidance, preserve manual review requirements, and avoid treating similarity findings as legal determinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-flow)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base fields reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, documents, configuration, guidance]

**Output Format:** [Text or Markdown summaries, JSON analysis results, HTML or Word reports, and editable .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents may be delivered through a short-lived download link; local reports are written under the skill output directory when requested.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
