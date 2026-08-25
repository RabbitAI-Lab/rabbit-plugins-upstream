## Description:

Dandelion API (dandelion.eu). Use this skill for ANY Dandelion API request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Dandelion text-analysis actions through an OOMOL-connected account, including sentiment analysis, text similarity comparison, language detection, and entity extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected text may be sent to Dandelion through OOMOL for external processing.

Mitigation: Use the skill only with text approved for that external processing path, and avoid sensitive text unless that handling is intended.

Risk: First-time CLI installation, login, and connector setup affect the user's local environment and OOMOL account connection.

Mitigation: Review setup commands before running them and perform setup only when an auth, connection, or missing-CLI error requires it.

Risk: Incorrect action payloads can produce failed or misleading API calls.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [Dandelion API homepage](https://dandelion.eu/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dandelion)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
