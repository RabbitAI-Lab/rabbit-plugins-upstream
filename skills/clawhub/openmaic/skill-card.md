## Description:

OpenMAIC assistant for setting up, generating, and extending OpenMAIC.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and external users use this skill to set up OpenMAIC, configure provider keys, generate multi-agent interactive classrooms, or extend the OpenMAIC product and @openmaic/* SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local setup may run clone, install, build, or startup commands on the user's machine.

Mitigation: The skill requires explicit confirmation before state-changing local actions and reports existing local state before reuse.

Risk: Access codes and provider keys are sensitive credentials used by OpenMAIC services.

Mitigation: The skill directs users to edit local configuration files themselves and avoids asking users to paste API keys into chat.

Risk: PDF-based generation and classroom content may be sent to the selected OpenMAIC service.

Mitigation: The skill requires confirmation before reading local PDFs and tells users which service mode is active before generation.

Risk: SDK font loading may depend on a remote font endpoint, which can affect offline or restricted-network deployments.

Mitigation: Users who need offline operation or strict network controls should review the renderer font dependency and configure suitable local assets.

## Reference(s):

- [OpenMAIC ClawHub Listing](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [Clone Or Reuse Existing Repo](references/clone.md)
- [Startup Modes](references/startup-modes.md)
- [Provider Keys](references/provider-keys.md)
- [Live Demo Mode](references/live-demo.md)
- [Generate Flow](references/generate-flow.md)
- [Extend Or Build On OpenMAIC](references/extend.md)
- [Extend The OpenMAIC Product Cookbook](references/extend-cookbook.md)
- [Consume The @openmaic/* SDK](references/extend-sdk.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local command execution after user confirmation and may return an OpenMAIC classroom URL.]

## Skill Version(s):

0.3.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
