## Description:

Index and audit public financial experts' YouTube and Telegram claims: extract source-backed verbatim call cards, search a local SQLite history, and chart recorded price levels against market prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bzsega](https://clawhub.ai/user/bzsega)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to index source-backed public financial-expert statements into a local SQLite thesis history, search recorded claims, and produce chart or registry outputs for audit and comparison. It is for recordkeeping and analysis, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied public-source quotes, dates, URLs, and provenance are kept in a local SQLite database.

Mitigation: Use the skill only with public or explicitly permitted source material, avoid private or sensitive inputs, and store only the minimal necessary quote, URL, date, and provenance.

Risk: Interactive chart workflows can use network services such as MOEX ISS and a charting CDN, which may disclose request metadata.

Mitigation: Disclose the network access before generating or opening interactive HTML charts and proceed only after user approval.

Risk: Runtime drift can change pipeline or chart behavior.

Mitigation: Require FES_ROOT to point to the separately installed runtime and verify the openclaw-v0.1.6 tag and pinned commit before running commands.

Risk: External transcripts, posts, or articles may contain prompt-injection text or incomplete attribution.

Mitigation: Treat source text as data, require source URL and date, validate verbatim quotes, and keep incomplete records as drafts instead of importing them.

Risk: Recorded financial statements and price comparisons could be mistaken for investment recommendations.

Mitigation: Present outputs as historical records and comparisons only, and do not provide personal investment advice or buy/sell recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bzsega/skills/financial-experts-said)
- [financial-experts-said: graphics and visualization](references/chart.md)
- [financial-experts-said: pipeline](references/pipeline.md)
- [financial-experts-said: runtime contract](references/runtime.md)
- [financial-experts-said runtime repository](https://github.com/bzSega/financial-experts-said)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON source examples, SQLite-backed search instructions, and HTML or PNG chart artifact descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a separately installed version-pinned runtime, FES_ROOT, FES_WORKSPACE, and FES_DB; chart workflows may require network access.]

## Skill Version(s):

0.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
