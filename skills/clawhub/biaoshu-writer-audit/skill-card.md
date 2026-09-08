## Description:

上传招标/投标文件，AI 一站式完成智能解读、成品投标文件生成、标书审查和标书查重，覆盖废标红线、评分标准、控标洞察、分级风险和雷同检测等投标场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to interpret tender documents, generate editable bid documents, review bid compliance risks, and check similarity across bid files before submission. Developers may also use it as an agent integration for the 百炼®标书 Open API workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid and tender documents, proposal drafts, and related business data are sent to the 百炼®标书 cloud service.

Mitigation: Use the skill only when the user is comfortable with that transfer, has authority to upload the files, and accepts processing under the API-key account.

Risk: Uploaded files and generated results may remain on the server briefly after processing.

Mitigation: Tell users that server-side results and generated .docx files may persist for about seven days and can be managed through the service account.

Risk: The API key controls the user's service account and could be exposed if pasted into chat or embedded in links.

Mitigation: Keep the API key out of chat, store it only in the local config file, and do not forward links that contain API-key or bind-key parameters.

Risk: Proposal generation may consume account word credits.

Mitigation: Confirm billing expectations before generation and distinguish account-balance prechecks from actual credit consumption.

Risk: Compliance and duplicate-check outputs are risk signals, not legal determinations.

Mitigation: Present results as internal review guidance and preserve prompts for human review, especially for similarity, disqualification, or incomplete semantic-review findings.

## Reference(s):

- [Usage guide](artifact/references/usage.md)
- [Open API contract](artifact/references/api.md)
- [Knowledge-base fields](artifact/references/knowledge-fields.md)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance, JSON API results, HTML or Word reports, and editable .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local report paths, short-lived download links for generated bid documents, and Chinese procurement terminology from the upstream service.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
