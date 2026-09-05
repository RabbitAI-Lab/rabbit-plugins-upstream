## Description:

Helps users in Chinese bidding workflows upload tender and bid documents to the 百炼®标书 service for tender interpretation, bid document generation, compliance review, and duplicate or similarity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, and bidding teams use this skill to interpret tender requirements, generate editable bid documents, review bid compliance, and compare bid files for similarity risk before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain confidential pricing, business, and personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm the user is comfortable with uploading the selected files and with the service retaining uploaded documents and generated outputs before running document-processing tasks.

Risk: The Api Key grants access to the user's account and is stored locally in the skill directory.

Mitigation: Have the user write the key directly to local config.json, do not paste or echo the key in chat, and treat the config file as a secret.

Risk: Generated bid documents may consume the account's available words, and repeated submissions could duplicate work or cost.

Mitigation: Check account balance before generation, reuse existing project and job identifiers when continuing work, and avoid resubmitting long-running generation tasks.

Risk: Duplicate or similarity checks provide risk signals but do not establish legal conclusions about collusion, invalid bids, or regulatory compliance.

Mitigation: Use duplicate-check results as internal review evidence only, require confirmation that the user is authorized to process all compared files, and keep final legal determinations with qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-business)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract reference](artifact/references/api.md)
- [Usage guide](artifact/references/usage.md)
- [Knowledge field reference](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown responses with generated JSON, HTML, Word, and .docx files where requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses user-selected local files, stores an API key in local config.json, and relies on cloud task results that may expire after about 7 days.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
