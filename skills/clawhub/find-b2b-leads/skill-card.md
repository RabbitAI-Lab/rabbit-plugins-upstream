## Description:

Find B2B leads by job title, company, and keyword and return a structured list of names, titles, companies, and LinkedIn URLs, powered by Cargo and Sales Navigator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, and go-to-market teams use this skill to source people leads for outbound campaigns from job title, company, keyword, and location criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates Cargo attribution/session records in addition to performing lead sourcing.

Mitigation: Review the behavior before installing and use it only if you are comfortable with Cargo recording that session attribution.

Risk: The skill asks to use the user's GitHub account for a promotional repository star after successful use.

Mitigation: Decline the optional prompt if you do not want the agent to act through your GitHub account; the skill states this action should require explicit approval.

Risk: Lead-search criteria are sent to Cargo and Sales Navigator through the Cargo CLI.

Mitigation: Use only search criteria and account context that are appropriate to share with those services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/find-b2b-leads)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Cargo prospecting recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/prospecting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured lead-list output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lead results are described as name, title, company, and LinkedIn URL; asynchronous Cargo runs may return a run or batch UUID for polling.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
