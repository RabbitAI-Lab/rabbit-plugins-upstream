## Description:

Extract reusable code snippets, API patterns, and configuration examples from web pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to extract actionable code blocks, CLI commands, API examples, and configuration snippets from public documentation pages, tutorials, and blog posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetched web pages can contain incorrect, unsafe, or stale commands and configuration.

Mitigation: Review snippets from untrusted pages before executing or reusing them.

Risk: Extracted snippets may include secrets, tokens, or sensitive configuration copied from source material.

Mitigation: Inspect saved snippets before sharing or committing them, especially shell commands and configuration files.

Risk: Snippet reuse can conflict with the source page's content license or attribution requirements.

Mitigation: Respect the source page's license and include attribution when requested.

## Reference(s):

- [Docker Compose documentation](https://docs.docker.com/compose/)
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/web-snippet-extractor)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with structured snippet sections and fenced code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the source URL, snippet language, snippet type, and optional workspace-saved Markdown snippets.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
