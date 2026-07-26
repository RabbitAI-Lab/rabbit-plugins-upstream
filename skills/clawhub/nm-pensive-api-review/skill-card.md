## Description: <br>
Evaluates API surface design, consistency, and exemplar alignment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review public API changes, design new API surfaces, audit consistency, and validate documentation before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may surface the skill during general API design or documentation discussions. <br>
Mitigation: Invoke it intentionally for API surface reviews and confirm that its checklist matches the current review task. <br>
Risk: The workflow can propose local search, documentation, and build commands as part of API inventory and governance checks. <br>
Mitigation: Review proposed commands before execution and keep an evidence log of commands and findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-api-review) <br>
- [Source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [pandas DataFrame API](https://pandas.pydata.org/docs/reference/frame.html) <br>
- [requests API](https://requests.readthedocs.io/en/latest/api/) <br>
- [tokio runtime API](https://docs.rs/tokio/latest/tokio/runtime/) <br>
- [serde API](https://docs.rs/serde/latest/serde/) <br>
- [Go net/http package](https://pkg.go.dev/net/http) <br>
- [Go database/sql package](https://pkg.go.dev/database/sql) <br>
- [Express API](https://expressjs.com/en/4x/api.html) <br>
- [Stripe API](https://stripe.com/docs/api) <br>
- [GitHub REST API](https://docs.github.com/en/rest) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with command examples, file references, findings, recommendations, and an approval decision.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API inventory counts, exemplar comparisons, consistency issues, documentation gaps, and timed action items.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
