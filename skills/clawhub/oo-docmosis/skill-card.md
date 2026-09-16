## Description:

Docmosis (docmosis.com). Use this skill for ANY Docmosis request -- searching and reading data. Whenever a task involves Docmosis, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Docmosis through an OOMOL-connected account, inspect action schemas, check readiness and quotas, list templates, retrieve template metadata or structure, and render templates with JSON data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that should not be run automatically by an agent.

Mitigation: Install the oo CLI only after human review using trusted, verified documentation, and do not allow unattended setup commands.

Risk: Document rendering can process supplied data and consume account quota.

Mitigation: Confirm the selected template, JSON payload, output handling, and quota impact before running render_document.

## Reference(s):

- [Docmosis homepage](https://www.docmosis.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docmosis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; render actions may return JSON delivery metadata or base64 output.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
