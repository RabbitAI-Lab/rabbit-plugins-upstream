## Description:

Guides AI agents through installing, authenticating, discovering, and using dLazy CLI tools, including asynchronous jobs and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AI-agent users use this quickstart to discover available dLazy CLI tools, authenticate, run local or cloud tasks, and recover from common errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The download troubleshooting instructions may access local browser session cookies.

Mitigation: Allow browser-cookie import only with the user's explicit, informed consent.

Risk: Authentication keys and local configuration may expose credentials if logged or committed.

Mitigation: Keep DLAZY_API_KEY and ~/.dlazy/config.json out of logs and repositories.

Risk: Installing an unreviewed CLI package may execute untrusted code.

Mitigation: Review before installing and use a trusted, pinned @dlazy/cli version where possible.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-start)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers tool discovery, authentication, asynchronous status checks, and troubleshooting.]

## Skill Version(s):

2.0.26 (source: ClawHub release; bundled guide states 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
