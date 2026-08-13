## Description:

招标文件解读工具 lets an agent use a user-provided App Key to call the 百炼®标书 service for tender interpretation, bid-package extraction, `.docx` bid-document generation, and optional compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement-support users use this skill to analyze tender files, understand disqualification and scoring risks, generate editable bid documents, and review draft bids for compliance. It is intended for workflows where the user can authorize upload of tender or bid files to the 百炼®标书 cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain sensitive commercial or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Confirm the user understands and authorizes the upload before first use, and process only files the user explicitly provides.

Risk: The App Key controls access to the user's 百炼®标书 account, and generated results may remain available under that account for about 7 days.

Mitigation: Keep the App Key out of chat, store it only in the local skill credential file, avoid forwarding links that contain key parameters, and direct users to manage retained data through the service account.

Risk: Bid-document generation consumes account credits, while API submission also requires a positive balance.

Mitigation: Check the account balance before generation and confirm credit use before producing final bid documents.

Risk: Changing the API base URL could send documents or credentials to an untrusted endpoint.

Mitigation: Use the trusted 百炼®标书 production host unless the user has explicitly approved another endpoint.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read)
- [百炼®标书 Service](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](artifact/references/api.md)
- [Usage and Operations Guide](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Natural-language guidance, JSON task results, HTML or Word reports, and generated `.docx` bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads only user-selected local tender or bid files, writes reports and generated documents to the configured output directory, and uses a local App Key credential for service access.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
