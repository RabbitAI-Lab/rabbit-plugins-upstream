## Description:

Helps agents plan, design, run, and analyze A/B tests, multivariate tests, and growth experimentation programs with hypotheses, metrics, sample sizing, and documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiweiyeah](https://clawhub.ai/user/jiweiyeah)

### License/Terms of Use:

MIT-0

## Use Case:

External users, product teams, marketers, and developers use this skill to structure statistically rigorous experiments, choose metrics, estimate sample size and duration, document outcomes, and maintain an experimentation backlog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad experiment or comparison wording, which can route general comparison requests into A/B testing guidance.

Mitigation: Confirm the user wants an experiment design or measurement plan before applying the full A/B testing workflow.

Risk: Experiment recommendations can be misleading when baseline rate, traffic, minimum detectable effect, or stopping rules are missing.

Mitigation: Ask for baseline conversion rate, traffic volume, smallest meaningful lift, and planned duration before interpreting significance or recommending a launch decision.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jiweiyeah/skills/ab-testing)
- [Sample Size Guide](references/sample-size-guide.md)
- [A/B Test Templates Reference](references/test-templates.md)
- [Evan Miller Sample Size Calculator](https://www.evanmiller.org/ab-testing/sample-size.html)
- [Optimizely Sample Size Calculator](https://www.optimizely.com/sample-size-calculator/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with checklists, tables, hypotheses, test plans, and analysis recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sample size estimates, metric definitions, experiment documentation templates, and cautions about premature stopping or insufficient traffic.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter metadata.version is 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
