## Description:

Mallary OpenClaw Skill guides agents through read-only Mallary discovery, OAuth setup, and explicit user-authorized social publishing or account workflows while omitting executable write syntax.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sammydigits](https://clawhub.ai/user/sammydigits)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, operators, and CI maintainers use this skill when they need an agent to inspect Mallary resources, set up Mallary authentication, or carry out a clearly requested Mallary publishing or account workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad Mallary social-account authority and allows real publishing, scheduling, uploads, or replies after the agent interprets a request as clear.

Mitigation: For brand, client, or public-facing accounts, explicitly ask for a preview and final approval before posting, and keep actions limited to the current user request.

Risk: Mallary authentication can grant read, publish, engage, and manage access, and API keys are bearer credentials.

Mitigation: Use browser OAuth when appropriate, keep API keys in a secret manager or masked CI secret, and never paste or print credentials in chat, logs, shell history, or shared artifacts.

Risk: Read-only Mallary discovery can expose sensitive operational data such as profile IDs, account labels, post content, analytics, settings, webhooks, and provider metadata.

Mitigation: Request only the data needed for the task and redact identifiers, account details, customer data, credentials, and unnecessary metadata before sharing output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sammydigits/skills/mallary)
- [Mallary Website](https://mallary.ai/)
- [Mallary Documentation](https://docs.mallary.ai)
- [Mallary CLI npm Package](https://www.npmjs.com/package/@mallary/cli)
- [Mallary Agent Repository](https://github.com/mallarylabs/mallary-agent)
- [Mallary Profiles Reference](PROFILES.md)
- [Supported Media Formats](SUPPORTED_FILE_TYPES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, local JSON previews, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent outputs should minimize and redact sensitive profile, account, post, analytics, settings, webhook, token, and API-key data.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
