## Description:

ERE (Editorial Refinement Engine) refines LLM-generated text into more natural editorial prose while preserving facts, entities, numbers, dates, and quotations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rickkbarbosa](https://clawhub.ai/user/rickkbarbosa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, editors, and content teams use this skill to turn AI-drafted text into publishable editorial prose with configurable profiles for technical, corporate, creative, minimal, and general writing. It is best suited for refinement and analysis of existing text, not translation, simple grammar correction, exact-format content, or generating content from scratch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive text may be exposed through the optional /tmp-based analysis workflow if local temporary-file handling is not acceptable.

Mitigation: Use the analysis helper only with text suitable for local temporary files, redact sensitive content when possible, and delete temporary files after analysis.

Risk: The draft audit API design described in the artifact is not production-ready by itself.

Mitigation: Do not deploy any audit API workflow without adding access controls, retention policy, and a security review.

Risk: Editorial refinement may accidentally change meaning despite the skill's preservation rules.

Mitigation: Compare the refined text against the original for preserved facts, entities, numbers, dates, and quotations before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rickkbarbosa/skills/ere)
- [Catálogo de Padrões de IA - ERE](references/patterns.md)
- [Princípios dos Clássicos de Escrita - Catálogo ERE](references/writing-principles.md)
- [Português (pt-BR) - Princípios Específicos da Língua](references/portuguese-writing-principles.md)
- [SDD - Editorial Refinement Engine (ERE)](references/ERE.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, analysis]

**Output Format:** [Markdown or plain text with optional JSON metrics from the local analysis helper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can propose refined prose and optional local readability, diff, and quality-score analysis; the helper uses Python stdlib and writes only when the user follows optional file-based commands.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
