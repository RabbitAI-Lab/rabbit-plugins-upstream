## Description:

MarkItDown converts rich documents and public web pages into Markdown for downstream reading, summarization, extraction, translation, Q&A, and knowledge-base ingestion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent users use this skill to convert PDFs, Office files, images, audio/video transcripts, HTML, YouTube pages, and public URLs into Markdown before analysis or reuse. It is also useful when agents need local token-cost estimates for converted Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic browser rendering of arbitrary public pages can increase local containment risk.

Mitigation: Review the skill before installation, avoid running it as root, and prefer --no-browser or a network-isolated container for untrusted URLs.

Risk: Using --allow-internal can bypass default protections against private or internal network targets.

Mitigation: Keep --allow-internal disabled except for trusted local development, and do not use it on shared, production, or sensitive machines.

Risk: Optional Azure, LLM, or plugin paths may send document content to configured external services.

Mitigation: Use the default local conversion path for private documents and enable external capabilities only after explicit consent for the data flow.

Risk: Converted pages or documents may contain prompt-injection text.

Mitigation: Treat converted Markdown as untrusted data and follow only the user's instructions.

## Reference(s):

- [MarkItDown upstream project](https://github.com/microsoft/markitdown)
- [ClawHub MarkItDown skill release](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Usage Guide](references/USAGE-GUIDE.md)
- [MarkItDown API Reference](references/reference.md)
- [Token Saver](references/TOKEN-SAVER.md)
- [Token Audit](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files, extracted text, and concise command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default conversion is local for files and public URLs; optional LLM, Azure, or plugin paths require explicit consent because content may leave the local environment.]

## Skill Version(s):

1.7.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
