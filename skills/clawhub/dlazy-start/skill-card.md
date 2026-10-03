## Description:

A quickstart for AI agents using the dLazy CLI to install and authenticate, discover and invoke media tools, poll tasks, and troubleshoot failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this guide to set up the dLazy CLI, discover available tools and costs, run cloud or local media tasks, and handle asynchronous results and common errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using browser-stored cookies for video downloads may expose sensitive session data.

Mitigation: Require explicit approval of the browser, profile, and site before using cookies_from_browser; prefer standard authentication or limited-scope exported cookies.

Risk: Installing and running the CLI can invoke networked media tools and store authentication in local configuration.

Mitigation: Install only if you trust the dLazy CLI, protect its authentication configuration, and pin the npm package version when reproducibility matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (declared CLI reference)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes JSON input examples and task-polling guidance.]

## Skill Version(s):

2.0.25 (source: ClawHub release; bundled frontmatter states 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
