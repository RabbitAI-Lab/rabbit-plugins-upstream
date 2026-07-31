## Description: <br>
Guides SaaS business operations across subscription revenue, plan packaging, trials, retention, expansion, margins, enterprise readiness, reporting, and diligence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, founders, SaaS operators, and advisors use this skill to reason through SaaS revenue, packaging, retention, expansion, cost-to-serve, enterprise-readiness, and reporting decisions. It helps the agent produce concise business guidance, formulas, operating checklists, and local memory updates for SaaS workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local SaaS memory can contain sensitive business information such as account names, ARR, commitments, churn reasons, contacts, and project records. <br>
Mitigation: Keep ~/Clawic/data/ access-controlled and only install the skill where that local memory model is acceptable. <br>
Risk: Pasted secrets or full customer/user exports could be preserved in local notes if the user asks the agent to remember them. <br>
Mitigation: Do not paste secrets or full customer/user exports into sessions expected to update memory; store pointers to secret managers instead of secret values. <br>
Risk: Guidance about billing, cancellations, refunds, plan migrations, or access suspension could affect customer access or revenue if acted on without review. <br>
Mitigation: Require explicit user confirmation before live billing or customer-access actions and state affected customer counts and revenue before proposing changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/saas) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Skill Page](https://clawic.com/skills/saas) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, formulas, checklists, local-memory entries, configuration snippets, and occasional code or shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local plain-text memory under configured ~/Clawic/data/ paths when the session produces durable SaaS business information.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
