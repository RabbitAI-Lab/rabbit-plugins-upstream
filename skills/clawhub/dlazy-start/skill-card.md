## Description:

Guides AI orchestrators through installing and authenticating @dlazy/cli, discovering and invoking media tools, polling cloud tasks, and troubleshooting failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using AI agents can follow this quickstart to set up @dlazy/cli, select available media tools, run local or cloud tasks, and recover from common failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Allowing an agent to run the CLI automatically can expose authentication configuration stored locally.

Mitigation: Review the skill before enabling automatic execution and restrict access to local credentials.

Risk: Using cookies_from_browser for video downloads can grant access to a browser profile's cookies.

Mitigation: Do not enable cookies_from_browser unless intentionally granting access to a specific browser profile for that download.

Risk: Installing an unpinned CLI version can change the behavior of commands an agent runs.

Mitigation: Prefer a reviewed, pinned @dlazy/cli version before letting an agent invoke it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to invoke tools that produce media assets or consume paid credits.]

## Skill Version(s):

2.0.31 (source: ClawHub release metadata; skill frontmatter says 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
