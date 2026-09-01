## Description:

This skill helps agents work with Chinese tender and bid documents by interpreting tender requirements, generating editable bid documents, reviewing bid compliance, and checking similarity across bid files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to prepare, analyze, review, and compare tender-response documents through the 百炼标书 cloud service. It is intended for users who can provide authorized local tender or bid files and manage their own API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain sensitive commercial, pricing, or personal information and are uploaded to the vendor cloud for processing.

Mitigation: Use the skill only with documents the user is authorized to process, and confirm consent before uploading files.

Risk: The local config.json contains the user's API key and can authorize account actions.

Mitigation: Keep config.json private, do not paste or echo the API key in chat, and avoid sharing links or logs that contain credentials.

Risk: Bid-document generation can consume the account's available word balance.

Mitigation: Confirm the intended generation action before submitting it and monitor the reported account balance.

Risk: Duplicate-check results provide similarity risk signals but are not a legal determination of bid rigging, collusion, or submission validity.

Mitigation: Present duplicate-check findings as internal review signals and recommend legal or compliance review for final determinations.

## Reference(s):

- [Skill Instructions](SKILL.md)
- [API Contract Reference](references/api.md)
- [Usage Guide](references/usage.md)
- [Knowledge Fields Reference](references/knowledge-fields.md)
- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-express)
- [Publisher Profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 Service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Human-facing guidance plus JSON summaries, HTML or Word reports, and editable .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents may consume account word balance; interpretation, review, duplicate-check, and generated files are processed through the vendor cloud under the user's API key.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
