## Description:

Helps an agent generate concise, accessibility-friendly alt text for publicly reachable image URLs using Alt Text Generator AI through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to inspect the live connector schema and generate accessibility-oriented alt text for a public image URL through an OOMOL-connected Alt Text Generator AI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs and request data are sent through the OOMOL-connected Alt Text Generator AI service.

Mitigation: Use the skill only for image URLs and request data appropriate for that connected service, and follow the server security guidance before use.

Risk: First-time setup may require running a CLI installer.

Mitigation: Review the CLI installer before running setup commands, as recommended by the security evidence.

## Reference(s):

- [Alt Text Generator AI homepage](https://alttextgeneratorai.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-alt-text-generator-ai)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connector action returns JSON data with metadata including an execution identifier.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
