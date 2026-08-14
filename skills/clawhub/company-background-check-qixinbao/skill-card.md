## Description:

This skill helps agents produce company background-check reports from a procurement and bidding perspective, covering company profile, business focus, customers and suppliers, award history, competitors, public-risk findings, and optional contacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and agents use this skill to investigate a named company or compare two companies using bid and tender data. It is intended for supplier screening, competitor analysis, customer and supplier relationship review, award-history analysis, and public-risk collection with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores or reads a Zhiliaobiaoxun API key from an environment variable or local configuration file.

Mitigation: Use a dedicated API key, avoid pasting credentials into chat, and rotate the key if the local configuration file or environment is exposed.

Risk: Trial registration can use a hashed device identifier after user consent.

Mitigation: Proceed with automatic registration only after explicit consent; preconfigure ZLBX_API_KEY to bypass automatic registration.

Risk: Generated HTML reports and signed platform links may expose sensitive business context to anyone who receives them.

Mitigation: Treat generated reports and signed links as sensitive, share them only with the intended audience, and avoid public forwarding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-background-check-qixinbao)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [API quick reference](artifact/references/api-quick.md)
- [Workflow guide](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown report in chat plus a generated self-contained HTML report file when applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include source-linked public-risk findings, signed platform links, local report paths, and data-boundary disclaimers.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
