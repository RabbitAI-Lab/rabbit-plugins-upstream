## Description: <br>
Guides agents to size safety buffers for budgets, timelines, runway, engineering capacity, and value-investing decisions under uncertainty. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to audit commitments where point estimates may be wrong, choose explicit safety margins, and decide whether a proposed commitment still survives adverse scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad buffer, runway, budget, or investing discussions and produce advisory guidance that depends on user-provided assumptions. <br>
Mitigation: Treat outputs as decision support, verify estimates and base rates, and seek qualified review before making material financial, operational, or safety-critical commitments. <br>
Risk: Real examples added back into the skill could expose confidential business, financial, or personal details. <br>
Mitigation: Scrub observed-use examples before sharing or publishing, and remove sensitive details from any cases used to update the skill. <br>


## Reference(s): <br>
- [Primary sources](references/sources.md) <br>
- [Graham's 1934 Framework and Buffett's Lifelong Application](examples/grahams-1934-framework-and-buffetts-lifelong-application.md) <br>
- [Margin of Safety Against AI-Era Valuations (2024-2026)](examples/ai-era-valuations-margin-of-safety-2024-2026.md) <br>
- [Berkshire Hathaway Annual Letters to Shareholders](https://www.berkshirehathaway.com/letters/letters.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown audit with concise explanatory text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask step-by-step questions in coach mode before producing the audit.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
