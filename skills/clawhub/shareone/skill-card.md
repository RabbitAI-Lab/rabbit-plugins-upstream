## Description:

Host HTML/Markdown pages and share PDF, Word, or PowerPoint docs as ShareOne short links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and teams use this skill to publish HTML or Markdown pages, share office documents, update existing ShareOne links, manage sharing settings, handle comments, and download shared content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish local files or conversation-derived content to externally accessible ShareOne links.

Mitigation: Treat every publish or update as external sharing, confirm the intended content and scope, and avoid broad requests such as sharing the last response unless that is deliberate.

Risk: A helper script can print saved ShareOne API keys in full.

Mitigation: Do not run key-checking commands where stdout is logged; if a key is exposed, rotate it after use or fix the key-printing behavior before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beep879/skills/shareone)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and ShareOne link results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update externally accessible ShareOne URLs and may invoke local JavaScript helper scripts.]

## Skill Version(s):

1.2.12 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
