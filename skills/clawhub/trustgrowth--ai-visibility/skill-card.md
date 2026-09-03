## Description:

Use when the user asks about AI visibility, GEO/AEO, AI Overview citations, LLM brand mentions, llms.txt, or AI crawler access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, marketers, and SEO/GEO practitioners use this skill to assess whether AI answer engines can reach, read, and cite a site. The skill supports readiness checks, imported observation review, and TrustGrowth score-level components while keeping readiness, observations, and unknowns distinct.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs may rely on public web fetches, optional paid connectors, or user-configured analytics and SEO sources.

Mitigation: Use only trusted connectors and preserve source, observation time, engine, and sample-size context in any conclusion.

Risk: Readiness checks can be mistaken for proof that AI systems actually cite or mention a site.

Mitigation: State that readiness measures whether engines can use the site, not whether they do, and label unsupported observations as unknown.

Risk: Third-party SEO or AI-monitoring estimates may be overread as guaranteed measurements.

Mitigation: Review outputs that rely on third-party estimates and report them as estimates unless validated evidence supports a measured label.

## Reference(s):

- [Connectors and categories](artifact/references/connectors.md)
- [Reporting contract](artifact/references/reporting.md)
- [OpenAI crawler documentation](https://platform.openai.com/docs/bots)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise guidance, with optional shell commands and JSON evidence records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve measured, absent, and unknown states; readiness-only findings should not be presented as proof of AI citations.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
