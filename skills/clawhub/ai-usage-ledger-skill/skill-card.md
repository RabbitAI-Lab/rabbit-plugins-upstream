## Description:

Compiles locally recorded AI coding-agent usage into an append-only ledger with token counts, list-price estimates, account attribution, validation reports, dashboards, documents, anonymized publication copies, and query workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[completetech](https://clawhub.ai/user/completetech)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineering leaders, finance reviewers, and authorized operators use this skill to measure local AI coding-agent usage, compare API-equivalent costs with subscription plans, validate coverage, and prepare dashboards or ledger documents for internal review or anonymized publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local AI agent logs and can retain sensitive usage metadata.

Mitigation: Install only for authorized local usage auditing, keep the ledger home and generated outputs private, and treat the ledger store as sensitive.

Risk: Optional prompt capture, credential-derived account claims, identifiable accounts, raw-log archives, broader profile or host scans, and scheduling can increase privacy or operational exposure.

Mitigation: Leave these features off unless they are needed and authorized, and enable them only after reviewing the skill disclosures and consent prompts.

Risk: Searching untrusted archived transcript text directly in a terminal can expose users to the disclosed archive grep terminal-output issue.

Mitigation: Prefer ledger.py query logs table or JSON output, or avoid terminal searches over untrusted archived transcript text until the issue is fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/completetech/skills/ai-usage-ledger-skill)
- [ClawHub metadata homepage](https://github.com/CompleteTech-LLC/ai-usage-ledger-skill)
- [Harness catalog](references/harness-catalog.md)
- [Log formats](references/log-formats.md)
- [Discovery and account attribution](references/discovery.md)
- [Ledger document catalog](references/ledger-document-catalog.md)
- [Pitfalls](references/pitfalls.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown, JSON, CSV, SQLite, HTML, PDF, DOCX, shell commands, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local ledger stores, dashboards, study packages, ledger documents, anonymized copies, and query results; prompt text, credentials-derived account claims, raw-log archives, broader host scans, and scheduled refreshes are opt-in.]

## Skill Version(s):

1.5.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
