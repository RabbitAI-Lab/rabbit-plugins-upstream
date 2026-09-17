## Description:

DataScope (mydatascope.com) supports reading, creating, and updating data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate DataScope through the oo CLI, including reading answers, list elements, and locations, and creating or updating DataScope records after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review installation steps before use, install the oo CLI through verified official documentation or a package manager, and do not allow an agent to run remote installer commands automatically.

Risk: Write actions can create or update DataScope records.

Mitigation: Confirm the exact target records, payload, and expected effect with the user before running write actions.

## Reference(s):

- [DataScope homepage](https://www.mydatascope.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub DataScope skill](https://clawhub.ai/oomol/skills/oo-datascope)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects that include data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
