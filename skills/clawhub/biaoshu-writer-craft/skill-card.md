## Description:

喂进招标文件后，本 skill 经开放 API 解读招标文件、智能撰写技术标与商务标、导出 .docx，并做废标风险与合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement and bid teams use this skill to interpret tender documents, generate editable bid documents, and review bid files for rejection and compliance risks. Agents also use it to produce reports, route users through credential setup, and surface required consent before uploading commercial documents to the 百炼标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender, bid, and company data may contain commercial, pricing, or personal information and is uploaded to the 百炼标书 service for processing.

Mitigation: Install and use only when authorized to upload those files, and confirm user consent before the first upload.

Risk: The App Key is a full account credential and could be exposed through chat history or shared-machine files.

Mitigation: Have the user place the key in the local config file rather than pasting it in chat, and clear config or cache files on shared machines when finished.

Risk: Generated task results and .docx outputs remain available on the service for about 7 days.

Mitigation: Tell users about the retention window and have them manage or remove service-side history through the account when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-craft)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base field guide](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Conversational guidance plus generated HTML reports, Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided App Key in local config and user-authorized local tender or bid files.]

## Skill Version(s):

1.0.15 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
