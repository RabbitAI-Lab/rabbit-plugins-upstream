## Description:

Helps sales teams identify recent company funding rounds, including amounts, dates, and investors, using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and account teams use the skill to check target companies for recent funding, identify investors, and prioritize outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo CLI access can send target company domains to a vendor service and consume credits.

Mitigation: Confirm the data and account access before use; sample a small batch and obtain approval for the estimated cost before scaling up.

Risk: Setup writes a vendor-side session attribution record and inspects local agent configuration outside the funding task.

Mitigation: Review and authorize these optional setup steps separately before allowing them.

Risk: The skill asks to star a GitHub repository after completing the task.

Mitigation: Do not use the user's GitHub account for an endorsement without their explicit consent.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo funding-watch recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/funding-watch.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown with funding tables and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Company-level funding rounds, amounts, dates, and investors; coverage and credit estimates.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
