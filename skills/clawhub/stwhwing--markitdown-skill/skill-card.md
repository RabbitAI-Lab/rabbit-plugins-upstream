## Description:

Converts user-provided documents and public web pages into Markdown with Microsoft's MarkItDown CLI and bundled helper scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent users use this skill to turn files or public URLs into Markdown before reading, summarizing, extracting, translating, or answering questions about the content. It is also used to reduce token usage by converting rich documents and noisy web pages into cleaner text before analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering user-supplied pages in a headless browser can expose the runtime to active web content, and the scan notes weak network isolation plus an automatic no-sandbox fallback.

Mitigation: Run the skill in a contained, non-root environment, avoid untrusted links when browser fallback is enabled, and use --no-browser for risky pages.

Risk: Fetching internal or private network URLs can create SSRF and data exposure risk, especially if internal access is explicitly allowed.

Mitigation: Keep the default public-URL restrictions enabled and do not use --allow-internal on private networks.

Risk: Optional LLM image descriptions, Azure Document Intelligence, and third-party plugins can send document content to external services.

Mitigation: Enable those paths only after explicit user consent for the specific content being sent out.

Risk: Unpinned MarkItDown dependency updates can change parser behavior or introduce new dependency risk.

Mitigation: Pin the MarkItDown dependency for production releases and review updates before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Publisher Profile](https://clawhub.ai/user/stwhwing)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [Usage Guide](references/USAGE-GUIDE.md)
- [MarkItDown API Reference](references/reference.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown documents, plain-text guidance, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default local conversion keeps content on the user's machine; optional LLM, Azure, or plugin paths can transmit content externally and require explicit consent.]

## Skill Version(s):

1.7.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
