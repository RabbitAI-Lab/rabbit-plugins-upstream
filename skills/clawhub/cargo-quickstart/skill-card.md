## Description:

Guides a new Cargo user from a buyer persona to a short lead list and credit receipt, with an option to save the search as a recurring play.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and go-to-market users can try Cargo by searching for leads matching a chosen buyer persona, reviewing a credit receipt, and optionally saving the search as a weekly play.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A short demo request may trigger a paid lead search and spend Cargo credits without clear approval.

Mitigation: Confirm the active workspace, provider, lead limit, and expected credit cost before the first paid search.

Risk: Fallback searches can use a different provider or cost more than the initial search.

Mitigation: Confirm the replacement provider and its cost before running any fallback, especially the higher-cost prospect search.

Risk: A weekly saved play can generate future searches and charges.

Mitigation: Require separate explicit confirmation before enabling the recurring play.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo Quickstart on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-quickstart)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown lead table, credit receipt, and optional CLI instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lead count and credit use depend on connected providers; a recurring play is offered separately.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
