## Description:

Google Slides (workspace.google.com). Use this skill for ANY Google Slides request: reading, creating, and updating data through the OOMOL Google Slides connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to inspect Google Slides schemas, retrieve presentations and pages, generate thumbnails, create presentations, copy templates, and apply confirmed Google Slides updates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup directs users to run a remote oo CLI installer script without built-in verification.

Mitigation: Review the installer before use and prefer a signed, checksum-verified, or documented package-manager installation path.

Risk: Write actions can create or modify Google Slides presentations when supplied payloads are executed.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-googleslides)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Slides](https://workspace.google.com/products/slides/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and metadata such as execution IDs when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
