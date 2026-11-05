## Description:

Paper Polisher Pro helps academic writers review AI-like writing signals, terminology, style, translation patterns, and manuscript quality, and provides sentence-level editing guidance without automatically rewriting text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

External academic writers use the skill to self-review manuscripts for writing signals, consistency, terminology, style, and quality before submission. Use its findings as writing guidance and follow institutional AI-use and disclosure policies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP workflow reports may retain manuscript excerpts in temporary storage, and the optional local HTTP server may freeze on an incomplete request.

Mitigation: Avoid confidential drafts until cleanup and HTTP timeout handling are fixed. Prefer explicit CLI report locations and the default stdio transport.

Risk: Terminology changes and detector conclusions may need human judgment.

Mitigation: Manually review terminology changes and detector conclusions before using them.

Risk: The optional model was unavailable for inspection.

Mitigation: Obtain it from a trusted source and independently verify its authenticity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Project repository and documentation](https://github.com/docsor1212/paper-polisher-pro)
- [Project documentation site](https://docsor.cn)
- [Best practices](references/best-practices.md)
- [FAQ](references/faq.md)
- [ModelScope skill mirror](https://modelscope.cn/skills/Docsor/paper-polisher-pro)

## Skill Output:

**Output Type(s):** [Analysis, Text, Guidance, JSON, Markdown, HTML reports]

**Output Format:** [Plain-text summaries and sentence-level suggestions, with JSON, Markdown, CSV, and HTML reports available from the tools.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include excerpts from the submitted manuscript; sentence-level suggestions guide edits and do not rewrite text automatically.]

## Skill Version(s):

7.4.0 (source: server-resolved release, skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
