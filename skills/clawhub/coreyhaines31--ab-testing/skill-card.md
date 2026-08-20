## Description: <br>
Helps agents plan, design, run, and analyze statistically rigorous A/B tests and experimentation programs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product managers, marketers, and growth teams use this skill to frame hypotheses, choose metrics, estimate sample size and duration, document variants, and interpret A/B, A/B/n, and multivariate tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad experiment and comparison phrasing may activate the skill for requests that are not actually about experiment design. <br>
Mitigation: Confirm the user wants A/B testing or experimentation guidance before applying statistical planning recommendations. <br>
Risk: The skill may read named product-marketing context files in the workspace when they exist. <br>
Mitigation: Keep product-marketing context files scoped to information that is appropriate to use for experiment planning. <br>
Risk: Experiment recommendations can be misleading when baseline rates, traffic, or metric definitions are incomplete or wrong. <br>
Mitigation: Ask for the baseline conversion rate, traffic volume, minimum detectable effect, test constraints, and metric definitions before making statistical recommendations. <br>


## Reference(s): <br>
- [Sample Size Guide](references/sample-size-guide.md) <br>
- [A/B Test Templates Reference](references/test-templates.md) <br>
- [Evan Miller A/B Test Sample Size Calculator](https://www.evanmiller.org/ab-testing/sample-size.html) <br>
- [Optimizely Sample Size Calculator](https://www.optimizely.com/sample-size-calculator/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text] <br>
**Output Format:** [Markdown guidance with structured experiment plans, checklists, tables, and templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference workspace product-marketing context files when present.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact metadata lists 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
