## Description: <br>
A wealth-management copilot skill for financial professionals that provides reference workflows for client opportunity scans, outreach, allocation strategy, investor education, asset diagnostics, portfolio optimization, work reviews, and ongoing investment support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gechengling](https://clawhub.ai/user/gechengling) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Financial professionals use this skill to draft client opportunity scans, outreach scripts, product briefings, investor education answers, asset diagnostics, allocation references, review summaries, and investment support content. Outputs are reference frameworks for qualified human review and do not replace financial, legal, insurance, compliance, or suitability review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive client financial information may be sent to remote MCP services despite a no-network disclosure. <br>
Mitigation: Confirm all MCP data recipients, require client-data consent and minimization for KYC and portfolio fields, and avoid identifiable client records until the disclosure and report-export controls are corrected. <br>
Risk: Reference workflows may be mistaken for regulated financial, legal, insurance, or compliance advice. <br>
Mitigation: Require qualified human review before client use and keep outputs framed as reference-only analysis rather than professional advice or guarantees. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gechengling/skills/wealth-copilot-digital-employee) <br>
- [Qieman MCP service endpoint](https://dashscope.aliyuncs.com/api/v1/mcps/Qieman/sse) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown and structured advisory templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reference-only output requiring human review before real-world use] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
