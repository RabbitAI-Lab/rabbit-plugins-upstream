## Description:

Contentful (contentful.com). Use this skill for ANY Contentful request - reading, creating, and updating data. Whenever a task involves Contentful, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Contentful connector schemas and perform Contentful read, create, and update operations through the OOMOL oo CLI with user-connected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified download-and-run installer commands.

Mitigation: Prefer an official signed or package-manager install path, or inspect and verify the installer before running it.

Risk: Create and update actions can modify Contentful content.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Contentful homepage](https://www.contentful.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-contentful)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Contentful connector command guidance and JSON request payloads for oo CLI actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
