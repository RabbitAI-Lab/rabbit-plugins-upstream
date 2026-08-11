## Description:

跨境法规调研 helps agents run Cue-powered cross-border legal research and return source-linked Chinese Markdown reports covering statutes, regulatory guidance, legislative background, applicability boundaries, and compliance points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, legal researchers, compliance teams, and developers use this skill to request cross-border regulation research for markets such as the United States, European Union, and Singapore. The agent checks Cue access, runs the Cue research workflow, and delivers the generated Markdown report with source links for user review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user research questions to Cue's external service.

Mitigation: Only submit questions that are appropriate to send to Cue, and keep the Cue API key private.

Risk: Generated legal research reports may be incomplete or unsuitable as legal advice.

Mitigation: Review the report against its cited legal sources and obtain qualified legal review before relying on conclusions.

Risk: The skill can use a referenced external runner repository.

Mitigation: Verify the runner repository before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-cross-border-regulation)
- [Cue API key](https://cuecue.cn/api-key)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [EUR-Lex](https://eur-lex.europa.eu)
- [United States Code](https://uscode.house.gov)
- [eCFR](https://www.ecfr.gov)
- [Singapore Statutes Online](https://sso.agc.gov.sg)
- [Congress.gov](https://www.congress.gov)
- [USA.gov federal agencies](https://www.usa.gov/federal-agencies)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links, plus concise setup and diagnostic commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written as local Markdown files and may be converted to DOCX or PDF with pandoc.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
