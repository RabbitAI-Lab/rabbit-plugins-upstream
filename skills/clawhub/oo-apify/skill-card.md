## Description:

Apify (apify.com). Use this skill for ANY Apify request - reading, creating, and updating data. Whenever a task involves Apify, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Apify through an OOMOL-connected account, including retrieving actor, user, dataset, and run information and starting actor runs with reviewed JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from the oo CLI installation source.

Mitigation: Review the oo CLI installation source before running installer commands, and install only when the CLI is missing.

Risk: Starting an Apify actor run can change account state, consume credits, or affect data.

Mitigation: Fetch the live action schema, review the exact JSON payload and expected impact, and get user confirmation before running write actions.

## Reference(s):

- [Apify homepage](https://apify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apify)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
