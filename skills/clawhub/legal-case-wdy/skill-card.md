## Description:

类案预判（法律检索+类似案例）。用户描述纠纷（如被骗钱、欠债不还、合同纠纷、被打伤等）时，自动检索相关法律条文和类似判例，分析法律后果及建议。触发词：法律依据、类似案例、纠纷、被骗、欠债、合同违约、侵权、打官司。

This skill is ready for commercial/non-commercial use.

## Publisher:

[rose-develop](https://clawhub.ai/user/rose-develop)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to search legal provisions and similar cases for described disputes such as fraud, unpaid debts, contract breach, injury, torts, or litigation questions. It can return legal basis, related precedent summaries, and optional next-step analysis after checking for the required WENDAOYUN_API_KEY.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User dispute descriptions may contain sensitive personal, financial, or legal details that are sent to the Wendaoyun API.

Mitigation: Ask users to omit names, account numbers, addresses, and unnecessary private facts before external lookup, and require confirmation for fact-specific disputes.

Risk: Broad or ambiguous legal requests may trigger external lookup before the user understands what data will be shared.

Mitigation: Clarify the request and disclose that the dispute summary will be sent to a third-party API before performing the search.

Risk: Legal search results and similar cases may be mistaken for definitive legal advice.

Mitigation: Frame results as informational legal research support and advise users to consult qualified counsel for jurisdiction-specific decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rose-develop/skills/legal-case-wdy)
- [Wendaoyun API portal](https://open.wendaoyun.com/home)
- [Wendaoyun get-laws API endpoint](https://h5.wintaocloud.com/prod-api/api/invoke/get-laws)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with legal article and similar-case sections, plus optional shell command examples and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the WENDAOYUN_API_KEY environment variable and sends dispute summaries to Wendaoyun API endpoints with top_k defaulting to 3 and capped at 5.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
