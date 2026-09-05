## Description:

MarkItDown helps agents convert documents and public web pages into Markdown using Microsoft's MarkItDown CLI, with utilities for URL conversion, batch conversion, and token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to convert user-provided files and public web pages into Markdown before analysis, summarization, extraction, translation, Q&A, or knowledge-base ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch arbitrary public URLs, and the security evidence flags incomplete SSRF protection.

Mitigation: Use only user-provided public HTTP/HTTPS URLs, avoid authenticated, private, internal, shortened, or sensitive links, and keep --allow-internal disabled except for trusted local testing.

Risk: Browser fallback for web conversion is unsandboxed.

Mitigation: Prefer disabling browser fallback when it is not needed, or run browser-based conversion in an isolated container or other trusted environment.

Risk: Optional LLM, Azure Document Intelligence, and plugin paths can send content to external endpoints or run third-party code.

Mitigation: Use the local conversion path for sensitive content, obtain explicit user consent before enabling external services, and use only trusted plugins.

Risk: The skill depends on MarkItDown and optional conversion dependencies installed at runtime.

Mitigation: Pin MarkItDown and optional dependency versions before deployment and review dependency changes during upgrades.

## Reference(s):

- [ClawHub MarkItDown Skill](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [USAGE-GUIDE.md](references/USAGE-GUIDE.md)
- [reference.md](references/reference.md)
- [TOKEN-SAVER.md](references/TOKEN-SAVER.md)
- [TOKEN-AUDIT.md](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write converted Markdown files and local token estimates when the user requests conversion or token-saving analysis.]

## Skill Version(s):

1.6.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
