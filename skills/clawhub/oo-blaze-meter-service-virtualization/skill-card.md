## Description:

BlazeMeter Service Virtualization (blazemeter.com). Use this skill for BlazeMeter Service Virtualization requests involving reading, creating, and updating service virtualization data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live BlazeMeter Service Virtualization action schemas, retrieve service mock templates, list templates in a workspace, and update JSON-safe template configuration through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified remote installer commands can execute changing network code on the user's machine.

Mitigation: Prefer a signed oo CLI package or a documented release with checksum verification before installation.

Risk: The update_service_mock_template action changes BlazeMeter Service Virtualization state.

Mitigation: Review the exact payload and expected effect with the user before allowing the write action.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [BlazeMeter Service Virtualization](https://www.blazemeter.com/)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-blaze-meter-service-virtualization)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL oo CLI and may return connector JSON with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
