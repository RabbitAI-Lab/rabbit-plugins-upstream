## Description: <br>
用于中文公文和机关企事业单位、学校等正式事务材料的起草、改写、压缩和复核；当用户明确要求写申请、请示、报告、通知、通告、意见、决定、决议、议案、公报、命令、函、复函、批复、说明、方案、纪要、公告、公示、通报、征求意见函、制度、规定、办法、管理办法、实施细则、操作规程、工作要点、总结、调研、讲话、致辞、采购公告、可研、审查材料、AI 算力、新闻稿、新闻消息、快讯、活动报道、活动新闻稿、新闻通稿、新闻评论、时评、评论员文章等正式文本，或要求对这类材料做文种校验、格式核验、去口语化、降 AI 味时使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, writers, reviewers, and agents use this skill to draft, revise, compress, and review Chinese official documents and formal workplace materials. It helps route document genres, preserve supplied facts, check official-document structure, reduce informal or AI-like wording, and provide review guidance for documents such as requests, reports, notices, plans, minutes, speeches, and AI compute procurement materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process user-provided official drafts that contain sensitive organizational, personnel, financial, procurement, or policy information. <br>
Mitigation: Use it only in an agent environment trusted for the document sensitivity, and avoid providing confidential drafts to untrusted runtimes. <br>
Risk: Generated or revised official documents may include incorrect facts, unsupported implications, or wording unsuitable for legal, financial, procurement, audit, or formal signing decisions. <br>
Mitigation: Human reviewers should verify facts, authority, amounts, dates, policy bases, document genre, and final approval language before use or signature. <br>
Risk: Optional lint results are advisory and do not prove that a document satisfies official-document requirements. <br>
Mitigation: Treat local lint findings as review aids and apply the relevant genre, formatting, and handling-element checks before finalizing a document. <br>
Risk: Web research may be used when the user requests current or public-source verification, which can expose task context to search tools. <br>
Mitigation: Use web verification only when needed, keep search terms minimal, and record unresolved or conflicting public-source facts as items for confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing) <br>
- [GitHub repository](https://github.com/gongyu0918-debug/chinese-official-writing-skill) <br>
- [Issue tracker](https://github.com/gongyu0918-debug/chinese-official-writing-skill/issues) <br>
- [Workflow](references/workflow.md) <br>
- [Official Style](references/official-style.md) <br>
- [Genre Routing](references/genre-routing.md) <br>
- [Review Checklist](references/review-checklist.md) <br>
- [GB/T 9704 Format](references/format-gbt9704.md) <br>
- [AI Compute Documents](references/ai-compute-docs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, code, shell commands] <br>
**Output Format:** [Plain text or Markdown, with optional local lint commands when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce complete Chinese formal document drafts, rewritten text, concise review findings, format checks, and advisory lint results.] <br>

## Skill Version(s): <br>
1.5.33 (source: evidence release, skill metadata, and README) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
