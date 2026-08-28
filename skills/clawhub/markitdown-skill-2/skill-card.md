## Description:

Convert documents and web pages to Markdown with Microsoft's MarkItDown CLI for file, URL, webpage, OCR, audio, YouTube, and token-saving document analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to convert user-provided files and web links into Markdown before reading, summarizing, extracting, translating, or adding the content to a knowledge base. It is also used to estimate token cost for converted Markdown when a supported baseline is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad proactive document and URL processing may expose confidential content to external services.

Mitigation: Use the skill only on files and URLs intended for conversion, avoid authenticated or internal URLs unless approved, and review before installing in confidential environments.

Risk: LLM image-description and Azure Document Intelligence examples can upload document-derived or image-derived content to external providers.

Mitigation: Enable OpenAI or Azure-backed conversion only when the user has approved the provider and the content is allowed to leave the local environment.

Risk: Third-party MarkItDown plugins may expand conversion behavior beyond the base package.

Mitigation: Leave plugins disabled unless the specific plugin source and behavior have been reviewed and trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/markitdown-skill-2)
- [Server-Resolved Source Repository](https://github.com/stwhwing/markitdown-skill)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [MarkItDown Usage Guide](artifact/references/USAGE-GUIDE.md)
- [Token-Saving Workflow](artifact/references/TOKEN-SAVER.md)
- [MarkItDown API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash and Python examples; converted document output is Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write .md files and emit optional JSON token-cost estimates from the token_saver helper.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
