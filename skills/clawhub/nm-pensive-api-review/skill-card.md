## Description: <br>
Evaluates API surface design, consistency, and exemplar alignment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review public API changes, design new API surfaces, audit consistency, and validate documentation completeness before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run source and documentation inspection commands in the current project. <br>
Mitigation: Use it only when API review is intended, and review recorded commands and findings before acting on recommendations. <br>
Risk: Broad triggers may make the skill appear for general design or documentation requests. <br>
Mitigation: Confirm the request involves API review before invoking the workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-api-review) <br>
- [Configured Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [pandas DataFrame API](https://pandas.pydata.org/docs/reference/frame.html) <br>
- [requests API](https://requests.readthedocs.io/en/latest/api/) <br>
- [tokio Runtime API](https://docs.rs/tokio/latest/tokio/runtime/) <br>
- [serde API](https://docs.rs/serde/latest/serde/) <br>
- [Go net/http](https://pkg.go.dev/net/http) <br>
- [Go database/sql](https://pkg.go.dev/database/sql) <br>
- [Express 4.x API](https://expressjs.com/en/4x/api.html) <br>
- [Stripe API](https://stripe.com/docs/api) <br>
- [GitHub REST API](https://docs.github.com/en/rest) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with command evidence, API inventory, exemplar alignment analysis, issue findings, decision, and action plan.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes precise file and line references when findings are reported.] <br>

## Skill Version(s): <br>
1.9.17 (source: release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
