## Description:

Finds work email addresses for contacts using their names and company domains through Cargo's email lookup providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and revenue operations teams use this skill to find work emails for prospects from names and company domains, leaving unresolved contacts without a guessed address.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup includes attribution tracking outside the email lookup task.

Mitigation: Review the attribution command before running it; skip it if only email lookup is needed.

Risk: The skill asks to star a GitHub repository after completing the task.

Mitigation: Only star with the user's explicit consent, or omit the starring step entirely.

Risk: Email searches send contact names and company domains to Cargo-backed providers and can consume credits.

Mitigation: Confirm data sharing and credit costs; test a small sample and obtain approval before a full batch.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Work email and lookup provider per contact; unresolved contacts remain blank.]

## Skill Version(s):

1.1.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
