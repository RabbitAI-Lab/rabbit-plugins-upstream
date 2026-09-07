## Description:

Provides installation guidance and usage reference for CHA2A agent phone capabilities, including SMS/RCS messaging, inbox access, groups, registration, trust checks, attachments, and fallback API calls when the plugin is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to install and configure the cha2a-phone plugin, then operate CHA2A phone features such as outbound messages, RCS group messaging, inbox checks, registration, and trust verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound SMS/RCS, attachment upload, registration, and auto-reply can create real external actions.

Mitigation: Confirm recipients, message content, attachments, and auto-reply authorization with the user before enabling or executing those actions.

Risk: Broad plugin permissions can expose the full phone toolset.

Mitigation: Allow only the exact phone tools needed for the task and avoid broad plugin access unless the user intends to trust the whole toolset.

Risk: Messages and attachments pass through the service provider inbox relay and may be visible to the service.

Mitigation: Avoid sending sensitive plaintext and review the phone plugin separately before installation.

## Reference(s):

- [rcs-server API Reference](references/rcs-api.md)
- [CHA2A registry endpoint](https://compliancehub.cn/api/v1/)
- [CHA2A RCS endpoint](https://compliancehub.cn/rcs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, and API reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may describe external phone, RCS, attachment, registration, inbox, and trust-check actions that require user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
