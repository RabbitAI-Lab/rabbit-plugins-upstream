## Description:

OpenMAIC helps agents set up OpenMAIC through the Live Demo or a local install and generate multi-agent interactive classrooms from a requirement or PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, educators, and external users use this skill to connect to OpenMAIC Live Demo or a local OpenMAIC checkout, configure provider credentials safely, and request classroom generation from requirements or PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local mode may run OpenMAIC project code and install dependencies.

Mitigation: Proceed only after user confirmation and only when the user trusts the project and selected checkout.

Risk: Live Demo access codes and provider keys are credentials that could be exposed in chat or mishandled in config.

Mitigation: Guide users to store credentials in local config files, avoid pasting secrets into chat, and rotate exposed credentials.

Risk: Classroom generation depends on OpenMAIC server-side provider and model configuration.

Mitigation: Direct users to fix .env.local or server-providers.yml instead of attempting request-time provider overrides.

## Reference(s):

- [OpenMAIC ClawHub skill page](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [Live Demo Mode](references/live-demo.md)
- [Generate Flow](references/generate-flow.md)
- [Provider Keys](references/provider-keys.md)
- [Startup Modes](references/startup-modes.md)
- [Clone Or Reuse Existing Repo](references/clone.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and raw classroom URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses confirmation-heavy setup steps, avoids asking users to paste credentials into chat, and polls long-running classroom generation jobs conservatively.]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
