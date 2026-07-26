## Description: <br>
Guides agents through pre-mortem style inversion audits for high-stakes or hard-to-reverse decisions by naming failure paths, ranking their likelihood and impact, and designing mitigations, not-to-do rules, and abort triggers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, founders, investors, and product teams use this skill to stress-test consequential plans before committing. It helps an agent turn a decision into an Inversion Audit with concrete failure paths, load-bearing mitigations, not-to-do rules, and an abort trigger. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs agents to fetch updated skill text from deciqai.com at runtime, which may change instructions after review. <br>
Mitigation: Use a pinned local copy or disable the runtime freshness fetch unless the remote endpoint is explicitly trusted and reviewed. <br>
Risk: The skill can guide high-stakes decision analysis, and its outputs may be incomplete if the agent or user lacks domain knowledge. <br>
Mitigation: Use the audit as decision support and have accountable domain experts review failure paths, mitigations, and abort triggers before relying on them. <br>


## Reference(s): <br>
- [Inversion skill page](https://clawhub.ai/deciqai/skills/inversion) <br>
- [Publisher profile](https://clawhub.ai/user/deciqai) <br>
- [Sources - inversion](references/sources.md) <br>
- [Performing a Project Premortem](https://hbr.org/2007/09/performing-a-project-premortem) <br>
- [Apollo 204 Review Board Final Report](https://history.nasa.gov/Apollo204/) <br>
- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a structured Inversion Audit with failure paths, probability-impact ratings, mitigations, not-to-do additions, abort triggers, and residual uncertainty.] <br>

## Skill Version(s): <br>
1.0.7 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
