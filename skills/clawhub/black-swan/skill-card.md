## Description: <br>
Black Swan helps agents audit strategies, portfolios, and systems for fat-tail exposure, hidden normal-distribution assumptions, tail-survival design, and hindsight-driven narratives. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to stress-test decisions, portfolios, infrastructure plans, and post-event explanations against rare, high-impact events. It is most useful when a model, strategy, or narrative treats a fat-tailed domain as stable or normally distributed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may produce guidance that users mistake for financial, engineering, or operational advice. <br>
Mitigation: Treat outputs as a reasoning aid and review recommendations with appropriate domain experts before acting on portfolio, infrastructure, or operational decisions. <br>
Risk: The audit can over-label foreseeable grey swans as unpredictable black swans. <br>
Mitigation: Require users to distinguish black swans from grey swans and document whether known historical or domain evidence made the event category foreseeable. <br>


## Reference(s): <br>
- [Black Swan on ClawHub](https://clawhub.ai/deciqai/skills/black-swan) <br>
- [Primary sources](references/sources.md) <br>
- [Long-Term Capital Management example](examples/long-term-capital-management-collapse-1998.md) <br>
- [Fukushima Daiichi tsunami example](examples/fukushima-daiichi-tsunami-2011.md) <br>
- [AI trade concentration example](examples/ai-trade-concentration-2023-2026.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit with structured sections and concise recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask step-by-step questions before producing a Black Swan Audit when the user needs coaching.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
