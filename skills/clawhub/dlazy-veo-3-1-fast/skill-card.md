## Description:

Helps agents generate short videos from text prompts or images using Google Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short text-to-video or image-to-video generation and extend existing videos through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external npm CLI introduces third-party code onto the user's machine.

Mitigation: Review the pinned dLazy CLI before use; use the documented npx option to avoid a persistent global installation.

Risk: Logging in stores a dLazy API key locally.

Mitigation: Protect local credentials, or supply the key per invocation; rotate or revoke it if compromised.

Risk: Prompts and referenced local media are sent to dLazy's cloud service.

Mitigation: Avoid submitting sensitive prompts or private media unless sharing them with dLazy is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI repository (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The command may return a generated media URL or an asynchronous task ID.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
