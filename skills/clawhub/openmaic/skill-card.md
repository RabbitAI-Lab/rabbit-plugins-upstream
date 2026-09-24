## Description:

OpenMAIC helps an agent guide users through OpenMAIC live demo setup, local setup, classroom generation, and extension of the OpenMAIC product or SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and technical users use this skill to set up OpenMAIC, configure provider credentials, generate multi-agent interactive classrooms, and understand extension paths for the OpenMAIC product and SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a stored OpenMAIC access code for the live demo.

Mitigation: Keep the access code private, store it only in the local OpenClaw configuration, and do not paste it into chat.

Risk: Classroom generation can send prompts, parsed PDF content, and optional media or search requests to OpenMAIC or configured provider services.

Mitigation: Avoid sensitive PDFs or regulated material unless remote processing is acceptable, or use local mode with reviewed server-side provider settings.

Risk: Misconfigured provider keys or model names can cause generation failures.

Mitigation: Configure provider credentials and DEFAULT_MODEL in OpenMAIC server-side configuration files before generation, and keep provider-prefixed model names.

## Reference(s):

- [ClawHub OpenMAIC Skill](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [OpenMAIC GitHub Repository](https://github.com/THU-MAIC/OpenMAIC)
- [Live Demo Mode](references/live-demo.md)
- [Generate Flow](references/generate-flow.md)
- [Provider Keys](references/provider-keys.md)
- [Startup Modes](references/startup-modes.md)
- [Clone Or Reuse Existing Repo](references/clone.md)
- [Extend Or Build On OpenMAIC](references/extend.md)
- [OpenMAIC Product Extension Cookbook](references/extend-cookbook.md)
- [Consume The OpenMAIC SDK](references/extend-sdk.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, API request shapes, and generated classroom URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HTTP request guidance, provider configuration steps, classroom job IDs, poll URLs, status updates, and raw classroom URLs.]

## Skill Version(s):

0.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
