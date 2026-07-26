## Description: <br>
Compare job offers as four-year total-compensation curves covering vesting cliffs, bonuses, 401(k) match, crossover timing, risk assumptions, and negotiation levers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, candidates, and career advisors use this skill to compare competing job offers over a stated time horizon. It helps quantify compensation, equity risk, crossover timing, and negotiation levers while keeping assumptions visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may produce misleading offer comparisons if private equity is treated as equivalent to cash or public RSUs. <br>
Mitigation: Make the private-equity discount explicit, get user agreement on the assumption, and show sensitivity at multiple discount levels when needed. <br>
Risk: The documented helper script is not packaged with this release. <br>
Mitigation: Confirm scripts/offer_comparison.py exists and comes from a trusted source before using the programmatic helper. <br>
Risk: Compensation outputs may be mistaken for financial advice. <br>
Mitigation: Keep the educational-model disclaimer and advise verification with a licensed professional before acting. <br>


## Reference(s): <br>
- [Offer Comparison homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/offer-comparison.html) <br>
- [ClawHub listing](https://clawhub.ai/mohitagw15856/skills/offer-comparison) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with tables and optional inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes year-by-year and cumulative compensation tables, crossover analysis, assumption sensitivity, negotiation levers, and an educational-model disclaimer.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
