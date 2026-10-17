## Description:

Converts public web pages and rich-format documents to Markdown for reading, analysis, and knowledge-base use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users convert public web pages and local documents to Markdown before summarizing, extracting information, or adding content to a knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser fallback on an untrusted public page can cause requests to internal-network resources.

Mitigation: In shared or sensitive networks, set --browser-fallback=off unless the browser is network-isolated; do not use --allow-internal.

Risk: Opt-in savings reporting can send source paths or URLs and limited local execution metadata to a receiver.

Mitigation: Leave SAVINGS_URL unset for private work unless you trust the receiver and accept this disclosure.

Risk: Converted pages may contain instructions intended to redirect the agent.

Mitigation: Treat converted page text as untrusted content, not as commands or instructions.

## Reference(s):

- [MarkItDown skill on ClawHub](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown converter dependency](https://github.com/microsoft/markitdown)
- [Usage guide](references/USAGE-GUIDE.md)
- [Security model](references/SECURITY.md)
- [Token-savings guide](references/TOKEN-SAVER.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands]

**Output Format:** [Markdown files and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional conversion manifests and token-savings estimates.]

## Skill Version(s):

1.8.11 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
