## Description:

Guides Mac Mini users through setting up a local document knowledge base with search, automated analysis, and Feishu summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and developers use this skill to set up document extraction, local knowledge-base search, scheduled analysis, and Feishu summary delivery on a personal Mac Mini.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled tasks continue to run shell commands after setup, and expanded command permissions increase the impact of changes to the analysis scripts.

Mitigation: Install only on a personal Mac you control; review scheduled commands before enabling them and restrict who can modify the analysis scripts.

Risk: The Feishu webhook is stored in plaintext, and document contents or summaries may leave the Mac through automated delivery.

Mitigation: Treat the webhook as a secret and review what documents and summaries may be sent to Feishu before enabling delivery.

Risk: Document processing can persist, clean, move, or overwrite extracted content and summaries.

Mitigation: Review the affected knowledge-base directories and retain backups of documents and summaries before running bulk processing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/seairteng/skills/macmini-knowledge-base)
- [Ollama download](https://ollama.com/download)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides installation and scheduled document analysis; may create summaries and catalogs on the user's Mac.]

## Skill Version(s):

1.4.8 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
