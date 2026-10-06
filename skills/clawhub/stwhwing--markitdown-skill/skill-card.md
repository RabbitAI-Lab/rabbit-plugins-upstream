## Description:

Converts documents and public web pages to Markdown for reading, analysis, and knowledge-base use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users convert rich-format files and public web pages into readable Markdown before summarizing, extracting information, or adding it to a knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser rendering of an untrusted public page can trigger unfiltered network requests from the user's machine.

Mitigation: Prefer --no-browser on sensitive or internal-networked machines, or run browser rendering in an isolated network or container.

Risk: Allowing internal URLs can expose private-network resources.

Mitigation: Do not use --allow-internal outside trusted local development.

Risk: Optional cloud analysis or plugins may send document contents outside the machine.

Mitigation: Enable OpenAI, Azure, or plugin features only after explicitly accepting the destination and data transfer.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown (conversion engine)](https://github.com/microsoft/markitdown)
- [Usage guide](references/USAGE-GUIDE.md)
- [Security model](references/SECURITY.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown text or Markdown files; optional token-use estimates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batch conversion and optional local token-use estimates.]

## Skill Version(s):

1.8.3 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
