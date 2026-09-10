## Description:

This skill helps agents run Cue-powered cross-border legal research and produce Chinese Markdown reports with official-source citations for major jurisdictions such as the United States, the European Union, and Singapore.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, compliance teams, legal researchers, and agents use this skill to research foreign-law and cross-border regulatory questions through Cue and receive source-linked Chinese reports. It supports compliance reviews, litigation research, investment diligence, tax, export-control, privacy, and comparative-law workflows, but it does not replace advice from a licensed lawyer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes shell commands and passes user questions into a research runner.

Mitigation: Pass the user query as a structured process argument and avoid shell interpolation.

Risk: The skill requires a Cue API key and stores or reads it from local configuration.

Mitigation: Use only trusted Cue accounts, protect the API key, rotate it when exposed, and avoid committing local configuration.

Risk: Generated legal research reports may contain incomplete or incorrect external content.

Mitigation: Treat reports as untrusted research output, verify official citations, and require qualified legal review before relying on conclusions.

Risk: Runtime instructions discourage cancellation during long-running research.

Mitigation: Keep operator control available so the agent can stop, summarize partial progress, or retry safely when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-cross-border-regulation)
- [Cue playbook source](https://cuecue.cn/playbook)
- [EUR-Lex](https://eur-lex.europa.eu)
- [United States Code](https://uscode.house.gov)
- [eCFR](https://www.ecfr.gov)
- [Singapore Statutes Online](https://sso.agc.gov.sg)
- [Congress.gov](https://www.congress.gov)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown report with cited source links and optional conversion commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to a local Markdown file; Word or PDF conversion can be requested separately with pandoc.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
