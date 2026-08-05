## Description: <br>
A basic finance analysis skill that calculates solvency and profitability ratios, performs three-factor DuPont ROE decomposition, and analyzes operating, investing, and financing cash-flow structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, personal investors, finance learners, and small business operators use this skill to review financial statement data for basic health checks, ratio tables, DuPont driver analysis, cash-flow structure, and improvement suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and exec authority even though the artifact describes it as a pure Markdown skill. <br>
Mitigation: Install it with the minimum permissions needed for the task, avoid exec/write access unless the publisher narrows and documents those permissions, and run it in a sandbox. <br>
Risk: Financial statements and internal company data may be confidential. <br>
Mitigation: Use non-confidential or redacted data unless the API and data flow have been reviewed and approved. <br>
Risk: The skill provides basic historical financial analysis and may produce incomplete conclusions if inputs are inaccurate, incomplete, or missing industry context. <br>
Mitigation: Validate source data before use, provide comparable industry data when relevant, and treat outputs as review material rather than final financial advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/accounting-and-finance-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown tables and concise prose] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include calculated financial ratios, DuPont decomposition, cash-flow structure tables, risk notes, and improvement suggestions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
