## Description:

Configure OpenClaw installations with optimized settings, channel setup, security hardening, and production recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to configure OpenClaw installations, including messaging channels, agent defaults, gateway access, automation, memory, tools, and security settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad tool profiles and full exec access can expose high-impact command capabilities.

Mitigation: Prefer minimal or coding-specific tool profiles, sandbox exec, and avoid exec.security full unless a reviewed use case requires it.

Risk: Remote gateway, browser relay, session transcript, email body, and memory settings can expose private data or control surfaces.

Mitigation: Keep personal Chrome relay off unless needed, use local memory search for sensitive work, exclude session transcripts and email bodies by default, and require reviewed gateway authentication.

Risk: Credential examples rely on local environment files that may contain sensitive tokens.

Mitigation: Protect ~/.openclaw/.env with restrictive permissions or use a proper secret store.

## Reference(s):

- [Setup skill page](https://clawhub.ai/ivangdavila/skills/setup)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance for OpenClaw setup and hardening.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
