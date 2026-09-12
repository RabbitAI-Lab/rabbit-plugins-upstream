## Description:

An agent skill for tender and bid workflows that uploads local tender or bid documents to 百炼®标书 to interpret requirements, generate .docx bid documents, review compliance risks, and compare bid-file similarity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Bid teams, proposal writers, and procurement support staff use this skill to analyze tender files, generate bid documents, review submission risks, and compare bid documents for similarity before submission. It is intended for user-authorized local tender and bid files processed through the vendor cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive tender and bid files are uploaded to the vendor cloud service and may contain commercial, pricing, or personal information.

Mitigation: Use only with files the user is authorized to process, obtain explicit upload consent before first use, and avoid deployment where policy forbids vendor-cloud processing.

Risk: Credentials or registration data could be exposed if users send phone numbers, SMS codes, API keys, or credential-bearing links in chat.

Mitigation: Have users create the skill-local config.json themselves, never ask them to paste secrets into chat, and do not forward links containing API key or bind_key parameters.

Risk: The security scan reports undeclared local project-history persistence in ~/.zcm/projects.json.

Mitigation: Review and align local persistence with the declared storage boundary before deployment, and clear local history where retention is not required.

Risk: The security scan reports review-worthy response-control instructions and redirect/network-request concerns.

Mitigation: Deploy only in an environment that enforces platform policy, restricts outbound access to the declared service domain, and reviews redirect handling before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-flow)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API dispatcher](artifact/references/api.md)
- [Authentication, jobs, and billing API](artifact/references/api-auth.md)
- [Interpretation and bid-document workflow API](artifact/references/api-bid-workflow.md)
- [Bid compliance review API](artifact/references/api-compliance.md)
- [Bid similarity checking API](artifact/references/api-duplicate.md)
- [Knowledge-base field reference](artifact/references/knowledge-fields.md)
- [Operational usage reference](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Chinese-language assistant guidance plus generated .docx bid documents, HTML or Word reports, JSON results, and text summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include short-lived download links, local report paths, progress summaries, and risk or similarity findings; paid operations consume account word balance under the user's API key.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
