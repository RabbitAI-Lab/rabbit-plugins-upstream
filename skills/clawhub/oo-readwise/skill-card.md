## Description:

Readwise lets an agent read, create, update, and delete Readwise data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Readwise users can use this skill to operate books, highlights, and Reader documents from an agent without handling raw API tokens. It supports listing and exporting content, saving documents, creating highlights, and updating Reader document metadata after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run Readwise actions that create, save, update, or otherwise change account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: The first-time setup path includes a one-line installer for the OOMOL CLI.

Mitigation: Install only after trusting OOMOL, preferably by reviewing the install guide, inspecting the installer, and checking available verification details.

## Reference(s):

- [Readwise homepage](https://readwise.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Readwise skill page](https://clawhub.ai/oomol/skills/oo-readwise)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON from the OOMOL connector when run with `--json`.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
