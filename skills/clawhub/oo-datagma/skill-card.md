## Description:

Datagma helps agents search and read Datagma data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to enrich people or companies, find verified work emails or phone numbers, check job changes, and inspect Datagma credit balance through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer one-liners for the oo CLI.

Mitigation: Perform first-time setup manually; prefer a pinned package, verified download, or reviewed installer before allowing agent use.

Risk: Datagma enrichment, email, phone, credit, and job-change checks may consume account credits and query external services.

Mitigation: Use the skill only for explicit Datagma requests and confirm intended action inputs before running commands that may spend credits.

Risk: Contact enrichment and search actions can involve person, company, email, phone, or social-profile data.

Mitigation: Submit only data the user intends to send to the OOMOL-connected Datagma service and avoid unrelated secrets or personal data.

## Reference(s):

- [Datagma homepage](https://datagma.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-datagma)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON data from Datagma connector actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
