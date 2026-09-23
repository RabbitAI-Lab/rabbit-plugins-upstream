## Description:

Adds UI plugin registration support to OpenClaw so plugins can register custom tabs in the Control UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maverick-software](https://clawhub.ai/user/maverick-software)

### License/Terms of Use:


## Use Case:

Developers and OpenClaw maintainers use this skill to add plugin UI tab registration support, including gateway registry methods and Control UI navigation integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill changes an OpenClaw source tree and requires a gateway restart.

Mitigation: Install only in an intended OpenClaw development or release workflow, review the code changes before applying them, and run the documented build and UI build checks before restarting the gateway.

Risk: Plugin-provided tab labels, icons, and group names may not have strong validation.

Mitigation: Validate plugin UI registration inputs before exposing them in the Control UI and review installed plugins that register views.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maverick-software/skills/plugin-architecture)
- [Installation instructions](artifact/INSTALL_INSTRUCTIONS.md)
- [UI plugin registry reference](artifact/reference/ui-plugin-registry.ts)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown instructions with TypeScript code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces source-tree patch guidance that should be reviewed and tested before gateway restart.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
