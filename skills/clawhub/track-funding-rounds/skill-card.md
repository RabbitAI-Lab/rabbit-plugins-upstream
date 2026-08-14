## Description:

Track which companies recently raised funding, with round, amount, and investors, powered by Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Go-to-market, sales, and business development teams use this skill to identify companies that recently raised funding and retrieve round details, amounts, investors, and acquisition history for target accounts or markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs the latest global Cargo CLI package from npm.

Mitigation: Review the @cargo-ai/cli package before installation and confirm the global install is acceptable for the execution environment.

Risk: The skill requires Cargo sign-in or an API token.

Mitigation: Use approved credential handling for Cargo authentication and avoid exposing tokens in prompts, logs, or shared shell history.

Risk: Cargo actions consume credits, and batch cost scales with the number of records.

Mitigation: Run the documented 10-20 record sample first, report observed cost and hit rate, then get user approval with the record count and credit estimate before a full batch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/track-funding-rounds)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Cargo funding watch recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/funding-watch.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and structured funding details from Cargo CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI, Cargo account authentication, and credit-aware batch execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
