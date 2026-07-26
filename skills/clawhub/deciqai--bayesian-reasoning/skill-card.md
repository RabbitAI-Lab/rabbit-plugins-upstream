## Description: <br>
Bayesian Reasoning helps agents structure belief updates with priors, likelihood ratios, posterior probabilities, and independence checks for evidence-heavy decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and decision-support agents use this skill to reason about uncertain evidence in domains such as medical screening, security alerts, fraud review, hiring signals, A/B tests, legal examples, physical search, and AI evaluation claims. It guides the agent to name hypotheses, anchor a prior, estimate likelihood ratios, compute a posterior, check evidence dependence, and state action thresholds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms such as Bayesian, prior, and posterior may activate the skill when a lighter response would suffice. <br>
Mitigation: Use the skill only when the decision involves uncertain evidence and a usable prior or base rate; tighten trigger wording if over-activation appears. <br>
Risk: Unsupported priors, likelihoods, or independence assumptions can produce misleading posterior confidence in high-stakes reasoning. <br>
Mitigation: Require sources for priors and likelihoods, explicitly estimate P(E|not-H), avoid compounding correlated evidence as independent, and review posterior estimates before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/bayesian-reasoning) <br>
- [deciqAI Bayesian Reasoning page](https://www.deciqai.com/c/bayesian-reasoning) <br>
- [Machine-readable skill metadata](https://www.deciqai.com/s/bayesian-reasoning.json) <br>
- [Sources - bayesian-reasoning](references/sources.md) <br>
- [Sally Clark Case example](examples/sally-clark-1999.md) <br>
- [Air France Flight 447 Search example](examples/air-france-447-search.md) <br>
- [AI Capability and Safety Belief Updating example](examples/ai-capability-safety-belief-updating-2023-2026.md) <br>
- [Royal Statistical Society letter on statistical evidence in court cases](https://web.archive.org/web/20120925034735/http://www.rss.org.uk/uploadedfiles/documentlibrary/744.pdf) <br>
- [Search for the Wreckage of Air France Flight AF 447](https://doi.org/10.1214/13-STS420) <br>
- [Stanford HAI AI Index Report](https://aiindex.stanford.edu) <br>
- [Anthropic Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown Bayesian update template with numerical fields and decision guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask stepwise coaching questions before producing a final posterior update.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
