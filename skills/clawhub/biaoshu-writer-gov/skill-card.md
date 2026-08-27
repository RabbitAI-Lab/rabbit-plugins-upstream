## Description:

智能投标文件写作 helps agents interpret tender documents, draft deliverable .docx bid files, and review bid submissions for compliance using the 百炼®标书 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Bidding teams and procurement-support agents use this skill to analyze tender requirements, generate editable bid documents, and check draft submissions for disqualification, formatting, compliance, and similarity risks. It is intended for workflows where the user has provided local tender or bid files and has authorized upload to the named 百炼®标书 service.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender, bid, company, pricing, and compliance files may contain sensitive business or personal information and are uploaded to the named 百炼®标书 service for processing.

Mitigation: Confirm the user understands and authorizes upload before processing files, and disclose that files and generated results are retained under the user's App Key account for the service's stated retention period.

Risk: The App Key grants access to the user's service account and could be exposed if pasted into chat or forwarded in parameterized account links.

Mitigation: Have the user place the App Key only in the local config file, never request or echo the key in conversation, and avoid sharing links that contain credential-bearing parameters.

Risk: Generated bid content and compliance findings may be incomplete, inaccurate, or unsuitable for final tender submission without review.

Mitigation: Require manual review of generated .docx files, reports, unresolved placeholders, risk findings, and submission-critical requirements before filing.

Risk: Bid-document generation consumes points from the App Key account and long-running generation can be accidentally duplicated.

Mitigation: Confirm generation intent and balance before creating bid documents, use idempotent or continuation flows for retries, and avoid resubmitting active generation jobs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-gov)
- [百炼®标书 Service](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](references/api.md)
- [Usage Guide](references/usage.md)
- [Knowledge Fields Reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Natural-language summaries plus local .docx bid files, HTML or Word reports, and JSON task results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are saved to explicit local paths; generated bid documents and compliance findings require human review before submission.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
