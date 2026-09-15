## Description:

Predis.ai (predis.ai). Use this skill for ANY Predis.ai request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate Predis.ai through an OOMOL-connected account: create generated content, list posts, and browse available system or custom templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the setup path before installing, prefer a verified package or signed release, and only run remote installer commands when the OOMOL installer source is trusted.

Risk: The create_content action changes Predis.ai state by submitting content generation requests.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Predis.ai homepage](https://predis.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector JSON data and execution identifiers returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
