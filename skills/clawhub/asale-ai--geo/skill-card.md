## Description:

GEO-first SEO analysis skill for auditing and improving websites for AI-powered search visibility while preserving traditional SEO foundations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to run GEO and SEO audits, assess AI citability, check crawler access, generate llms.txt and schema guidance, and produce client-ready optimization reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes broad activation terms and can perform website analysis when invoked for GEO or SEO work.

Mitigation: Use it deliberately with explicit /geo commands or clearly scoped URL analysis requests.

Risk: Prospect and proposal workflows may persist client or prospect data under ~/.geo-prospects.

Mitigation: Avoid storing sensitive client or prospect data unless local persistence is acceptable for the environment.

Risk: The /geo update command can change future skill behavior.

Mitigation: Review upstream changes before running /geo update and rescan the skill after updating.

## Reference(s):

- [ClawHub skill page for geo](https://clawhub.ai/asale-ai/skills/geo)
- [ClawHub publisher profile for asale-ai](https://clawhub.ai/user/asale-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, inline summaries, generated configuration files, JSON-LD snippets, shell commands, and optional PDF report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write audit reports, llms.txt, schema report files, PDF report files, and local prospect or proposal records depending on the invoked /geo command.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
