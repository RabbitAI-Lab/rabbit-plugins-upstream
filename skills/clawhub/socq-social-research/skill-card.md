## Description: <br>
Research public social-platform content, accounts, keywords, and SEO search data with SocQ. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to research public social and SEO data, select SocQ endpoints, estimate costs, submit asynchronous collection jobs, poll results, paginate records, and retrieve raw exports when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests can send URLs, usernames, keywords, domains, and returned public social data to SocQ. <br>
Mitigation: Use the skill only for lawful, authorized research, avoid sensitive personal targeting or harassment use cases, and set explicit result limits. <br>
Risk: SocQ is a credit-metered external service, so broad or cross-platform collection can consume paid credits. <br>
Mitigation: Check account credits and endpoint cost before large runs, reduce result limits where appropriate, and confirm broad scopes before submitting jobs. <br>
Risk: Asynchronous tasks, provider failures, unsupported filters, or early pagination stops can produce partial coverage. <br>
Mitigation: Poll tasks until a terminal state, follow pagination to the requested cap, and report failed platforms, filters, partial coverage, and collection time with the results. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [ClawHub Skill Page](https://clawhub.ai/socq/skills/socq-social-research) <br>
- [Authentication](references/authentication.md) <br>
- [Capability Catalog](references/catalog.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Cross-platform Research](references/cross-platform.md) <br>
- [Errors and Recovery](references/errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, API payload guidance, and structured result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, endpoint names, result coverage notes, pagination status, failed platforms, filters, collection time, and links to raw JSONL exports when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
