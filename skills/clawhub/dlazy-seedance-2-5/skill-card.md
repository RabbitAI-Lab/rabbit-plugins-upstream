## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, multi-modal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate video assets through the dLazy Seedance 2.5 CLI, including prompt-based generation, multi-modal references, first/last-frame control, and optional local saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and referenced media to a hosted dLazy video-generation service.

Mitigation: Only submit media and prompts approved for that service, and avoid passing sensitive local files unless the user explicitly intends to upload them.

Risk: The skill requires a dLazy API key stored in local config or supplied through an environment variable.

Mitigation: Protect the API key like other credentials, avoid exposing it in logs or shared shells, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Installing the CLI globally can persist third-party executable code on the host.

Mitigation: Prefer the pinned npx invocation when possible, review the upstream CLI in sensitive environments, and avoid running npm with administrator or root privileges.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted file URLs, with optional local download when the CLI save option is used.]

## Skill Version(s):

1.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
