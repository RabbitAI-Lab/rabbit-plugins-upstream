## Description: <br>
Utilitarianism guides agents through stakeholder mapping, welfare impact estimation, aggregation checks, and sensitivity testing for ethical cost-benefit decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and users invoke this skill when a policy, product, or organizational decision affects multiple parties differently and needs explicit welfare trade-off analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Utilitarian analysis can embed value judgments when different harms and benefits are converted into a single comparison. <br>
Mitigation: Require explicit affected-party mapping, conversion assumptions, rights constraints, and sensitivity checks before relying on the conclusion. <br>
Risk: The skill can produce misleading decision support if users treat a welfare-maximizing result as the final ethical answer. <br>
Mitigation: Use the output as reviewable guidance and compare it with relevant legal, safety, rights, and organizational constraints. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/utilitarianism) <br>
- [Utilitarianism Sources](references/sources.md) <br>
- [Cost-Benefit Analysis of the Clean Air Act (1970)](examples/cost-benefit-analysis-of-the-clean-air-act-1970.md) <br>
- [Benefits and Costs of the Clean Air Act](https://www.epa.gov/clean-air-act-overview/benefits-and-costs-clean-air-act) <br>
- [Utilitarianism Metadata](https://www.deciqai.com/s/utilitarianism.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with structured welfare maps and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Non-executable reasoning output; no credentials, tools, or shell commands are requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
