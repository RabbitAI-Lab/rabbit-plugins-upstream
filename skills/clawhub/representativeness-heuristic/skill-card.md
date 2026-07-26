## Description: <br>
Helps agents audit profile-driven probability judgments for base-rate neglect, conjunction fallacy, and prototype bias before high-stakes decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and decision-support agents use this skill to challenge candidate, investment, product, and startup judgments where resemblance to a vivid prototype may be replacing base-rate reasoning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may cause the skill to intervene in hiring, investing, startup, or other profile-based probability discussions where the user did not ask for a bias audit. <br>
Mitigation: Review and narrow activation language if deployment should be limited to explicit requests for base-rate, conjunction-fallacy, or representativeness analysis. <br>
Risk: The skill can influence high-stakes judgments by producing calibrated recommendations from user-supplied base rates and profile evidence. <br>
Mitigation: Use its output as decision-support guidance, verify base rates and likelihood assumptions against domain data, and keep human review in the final decision path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/representativeness-heuristic) <br>
- [Sources - representativeness-heuristic](references/sources.md) <br>
- [Tversky & Kahneman 1972 + 1983 - The Linda Problem](examples/tversky-kahneman-1972-1983-the-linda-problem.md) <br>
- [The Hot Hand in Basketball](examples/gilovich-vallone-tversky-1985-the-hot-hand-in-basketball.md) <br>
- [Representativeness in AI-Startup Investing](examples/ai-startup-next-openai-pattern-matching-2023-2026.md) <br>
- [deciqAI skill page](https://www.deciqai.com/c/representativeness-heuristic) <br>
- [Agent-readable metadata](https://www.deciqai.com/s/representativeness-heuristic.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown] <br>
**Output Format:** [Markdown coaching responses with calibrated probability summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May pause at WAIT prompts in novice coaching mode.] <br>

## Skill Version(s): <br>
1.0.5 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
