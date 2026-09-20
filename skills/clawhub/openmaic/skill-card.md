## Description:

OpenMAIC guides agents through Live Demo or local setup, provider configuration, classroom generation, and SDK or product extension workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and agent operators use this skill to set up OpenMAIC, generate multi-agent interactive classrooms from requirements or PDFs, and extend the OpenMAIC product or SDK. It provides stepwise guidance for live demo access, local setup, provider configuration, health checks, generation requests, polling, and customization entry points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured OpenMAIC access code may be sent as a bearer token to the OpenMAIC Live Demo service.

Mitigation: Keep the access code in local OpenClaw config, do not paste it into chat, and review auth-bearing prompts before using Live Demo mode.

Risk: Local setup can involve state-changing commands such as dependency installation, dev servers, Docker, and PDF-based generation.

Mitigation: Require explicit user confirmation before state-changing actions or reading local PDFs, and review commands before running them.

Risk: Provider and model misconfiguration can cause generation failures or unintended provider use.

Mitigation: Configure provider keys and DEFAULT_MODEL only in OpenMAIC server-side config files, keep provider prefixes on model IDs, and avoid request-time provider overrides.

## Reference(s):

- [ClawHub OpenMAIC skill listing](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [Clone Or Reuse Existing Repo](references/clone.md)
- [Startup Modes](references/startup-modes.md)
- [Provider Keys](references/provider-keys.md)
- [Generate Flow](references/generate-flow.md)
- [Live Demo Mode](references/live-demo.md)
- [Extend Or Build On OpenMAIC](references/extend.md)
- [Extend The OpenMAIC Product Cookbook](references/extend-cookbook.md)
- [Consume The OpenMAIC SDK](references/extend-sdk.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and raw classroom URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confirmation-heavy workflow; avoids asking users to paste provider keys or access codes into chat.]

## Skill Version(s):

0.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
