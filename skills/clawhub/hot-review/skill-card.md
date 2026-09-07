## Description:

This skill helps agents analyze ARI-collected Amazon review samples to identify VOC themes, negative-review issues, trend signals, competitor differences, and listing improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and commerce teams use this skill to inspect review data for product validation, competitor research, VOC reporting, advertising keyword ideas, and listing improvements. It is suited to account-authorized ARI workflows where paid analysis, exports, and monitoring are acceptable after the user understands the cost and data scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits or change future confirmation settings with too little fresh user approval.

Mitigation: Set the ARI account to ask before paid actions, use only-quote requests when estimating cost, and require explicit confirmation before recurring monitoring or schedule changes.

Risk: The skill uses an ARI API key and account-scoped review and report data.

Mitigation: Authorize only trusted ARI accounts, do not paste API keys into chat or reports, and rotate or remove credentials when the skill is no longer needed.

Risk: A custom ARI base URL could redirect authenticated requests to an untrusted server.

Mitigation: Use the default ARI endpoint unless the custom server is trusted and HTTPS-protected, and require explicit opt-in before using a non-default base URL.

## Reference(s):

- [Skill README](artifact/README.md)
- [User Guide](artifact/使用说明.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/hot-review)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Natural-language answers and Markdown reports, with optional JSON-style CLI output, CSV/Markdown/HTML exports, links, and shell commands for setup or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key for account access; paid workflows may return credit usage, report IDs, report URLs, and saved export file paths.]

## Skill Version(s):

1.4.7 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
