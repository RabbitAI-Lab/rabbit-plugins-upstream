## Description:

TemplateFox helps agents read, create, and update TemplateFox data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to automate TemplateFox template and PDF workflows through an OOMOL-connected account, including generating images or PDFs, listing templates, retrieving template fields, checking credits, and modifying PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that could execute arbitrary code if run without verification.

Mitigation: Install the oo CLI only through a trusted, verifiable method and do not allow an agent to run remote installer pipelines automatically.

Risk: TemplateFox write actions can create generated files or otherwise affect the connected account.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [TemplateFox homepage](https://templatefox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce signed TemplateFox download URLs when actions generate or transform files.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
