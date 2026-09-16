## Description:

Tencent Docs (docs.qq.com) lets an agent read, create, search, export, and update Tencent Docs files through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Tencent Docs from an agent: read documents and spreadsheets, discover files, export content, and run confirmed create or update actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad oo CLI authority and includes actions that can change Tencent Docs state.

Mitigation: Review the live connector schema, exact target document, payload, and expected effect with the user before running write actions.

Risk: First-time setup includes remote installer commands that should be reviewed before execution.

Mitigation: Use a verified installation method where possible and avoid running pipe-to-shell installer commands without inspection.

Risk: Tencent Docs data is routed through OOMOL's connector.

Mitigation: Install and use the skill only when the user trusts OOMOL and the connector is appropriate for the documents being accessed.

## Reference(s):

- [Tencent Docs homepage](https://docs.qq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
