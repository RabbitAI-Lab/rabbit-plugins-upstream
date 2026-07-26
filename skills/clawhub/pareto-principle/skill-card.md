## Description: <br>
Guides agents through Pareto analysis to identify measured vital-few inputs, avoid unsupported 80/20 claims, and make explicit decisions about lower-contribution items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to prioritize backlogs, business initiatives, defects, customers, or AI investments by measuring contribution distributions and concentrating effort at the observed elbow. It is not intended for tiny datasets or safety-critical and regulatory contexts where rare or long-tail items must still be addressed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat an asserted 80/20 split as fact without measuring the distribution. <br>
Mitigation: Require a precise output metric, enumerate inputs, measure each contribution, rank cumulative contribution, and report the observed ratio rather than assuming 80/20. <br>
Risk: Users may cut low-contribution items automatically even when they are safety-critical, regulatory, or strategically important. <br>
Mitigation: Screen for safety-critical and regulatory contexts up front, and require an explicit cut, maintain, or strategic-invest decision for the lower-contribution set. <br>
Risk: The skill can produce advisory prioritization that is stale as contribution patterns change. <br>
Mitigation: Include a re-measurement schedule, such as quarterly review or review after material business, product, or market changes. <br>


## Reference(s): <br>
- [Sources - pareto-principle](references/sources.md) <br>
- [Microsoft Office Bug-Fix Pareto example](examples/microsoft-office-bug-fix-pareto-2002.md) <br>
- [Realized AI Value Pareto example](examples/ai-value-concentration-2024-2026.md) <br>
- [deciqAI Pareto Principle skill page](https://www.deciqai.com/c/pareto-principle) <br>
- [deciqAI Pareto Principle machine-readable metadata](https://www.deciqai.com/s/pareto-principle.json) <br>
- [Gates WinHEC 2002 keynote transcript](https://news.microsoft.com/source/2002/04/18/gates-winhec-keynote-address-outlines-industrywide-vision-for-continued-vibrant-pc-ecosystem/) <br>
- [McKinsey The State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) <br>
- [Stanford HAI AI Index Report](https://aiindex.stanford.edu/report/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, analysis] <br>
**Output Format:** [Markdown analysis template and step-by-step coaching responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May pause for user input during coached Pareto analysis; no code execution or external tool access is required.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
