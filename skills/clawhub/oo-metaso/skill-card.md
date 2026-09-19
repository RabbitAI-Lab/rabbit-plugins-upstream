## Description:

Use Metaso through an OOMOL-connected account to search content, read webpages, and create scoped chat completions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to operate Metaso via an OOMOL-connected account for search, webpage extraction, and chat completions grounded in a requested Metaso scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup recommends executing unpinned remote installer scripts directly in a shell.

Mitigation: Use a versioned installer or package manager with signature or checksum verification before installing the oo CLI.

Risk: Metaso chat completion actions are tagged as write actions and may change service-side state or consume account resources.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The skill requires an OOMOL-connected Metaso account for connector access.

Mitigation: Connect only an OOMOL or Metaso account intended for this skill and avoid opening login or connection flows unless an auth or connection error requires it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-metaso)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Metaso Homepage](https://metaso.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return extracted webpage Markdown, structured JSON, search results, or streamed chat chunks depending on the selected Metaso action.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
