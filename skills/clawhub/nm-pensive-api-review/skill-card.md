## Description:

Evaluates API surface design, consistency, and exemplar alignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review public API changes, design new API surfaces, audit consistency, and validate documentation readiness before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms may invoke the skill during general design or documentation work.

Mitigation: Use the skill when an API review is intended and confirm the review scope before following its workflow.

Risk: The workflow suggests shell and documentation-generation commands that may be costly or noisy in large or sensitive repositories.

Mitigation: Review proposed commands first and run them in an appropriate workspace with repository-specific limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-api-review)
- [ClawHub publisher profile](https://clawhub.ai/user/athola)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)
- [pandas DataFrame API](https://pandas.pydata.org/docs/reference/frame.html)
- [requests API](https://requests.readthedocs.io/en/latest/api/)
- [tokio Runtime API](https://docs.rs/tokio/latest/tokio/runtime/)
- [serde API](https://docs.rs/serde/latest/serde/)
- [Go net/http package](https://pkg.go.dev/net/http)
- [Go database/sql package](https://pkg.go.dev/database/sql)
- [Express 4.x API](https://expressjs.com/en/4x/api.html)
- [Stripe API documentation](https://stripe.com/docs/api)
- [GitHub REST API documentation](https://docs.github.com/en/rest)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with command evidence, API inventory, exemplar alignment analysis, findings, release decision, and action plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file and line references, numerical API inventory counts, and recommended documentation or migration actions.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
