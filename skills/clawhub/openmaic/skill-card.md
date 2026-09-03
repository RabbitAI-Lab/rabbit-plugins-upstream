## Description:

OpenMAIC assistant for setting up, generating, and extending OpenMAIC.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and classroom-content creators use this skill to set up OpenMAIC, run the hosted live demo or a local instance, generate multi-agent interactive classrooms, and extend OpenMAIC or its @openmaic/* SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live Demo mode sends generation requests and any uploaded or parsed classroom material to open.maic.chat.

Mitigation: Use Live Demo only when that cloud data flow is acceptable; otherwise run OpenMAIC locally and configure providers server-side.

Risk: OpenMAIC access codes and provider API keys can be exposed if pasted into chat or written by the agent.

Mitigation: Keep credentials in local configuration files and have the user edit those files directly.

Risk: Optional web search, image, video, TTS, server persistence, and remote font features add extra provider or storage data flows.

Mitigation: Enable optional features only after confirming their providers and persistence paths are appropriate for the classroom content.

Risk: Incorrect model or provider configuration can cause generation failures.

Mitigation: Set provider-prefixed DEFAULT_MODEL values in OpenMAIC server-side configuration and fix auth or model errors in .env.local or server-providers.yml before retrying.

## Reference(s):

- [OpenMAIC Skill Page](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Repository](https://github.com/THU-MAIC/OpenMAIC.git)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [Clone Or Reuse Existing Repo](references/clone.md)
- [Startup Modes](references/startup-modes.md)
- [Provider Keys](references/provider-keys.md)
- [Generate Flow](references/generate-flow.md)
- [Live Demo Mode](references/live-demo.md)
- [Extend Or Build On OpenMAIC](references/extend.md)
- [Extend The OpenMAIC Product Cookbook](references/extend-cookbook.md)
- [Consume The @openmaic/* SDK](references/extend-sdk.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, API calls, and generated classroom URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API requests to OpenMAIC live-demo or local endpoints and return raw classroom URLs.]

## Skill Version(s):

0.3.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
