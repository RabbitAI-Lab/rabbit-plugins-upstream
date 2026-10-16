## Description:

Guides developers in deploying and using a self-hosted, OpenAI-compatible gateway for model inference and optional tools such as browser automation, code execution, media generation, storage, and messaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure and run an opt-in self-hosted AI stack and call its OpenAI-compatible endpoint for inference and enabled services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One broad bearer token can grant access to code execution, browser automation, storage, and messaging.

Mitigation: Give access only to trusted agents for explicit tasks; set distinct per-service tokens and enable only needed services.

Risk: A publicly reachable gateway or exposed credentials could allow misuse of high-capability services.

Mitigation: Use a trusted, dedicated host; do not expose port 4000 directly; protect .env, mailbox credentials, and Telethon configuration.

Risk: Running upstream setup targets may deploy services with access to local files and external systems.

Mitigation: Review the upstream repository before running make targets and restrict services to those required.

## Reference(s):

- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup guide](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API requests]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance depends on enabled services and locally configured credentials.]

## Skill Version(s):

11.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
