## Description:

Deploys and checks project infrastructure for an online fiction writing toolkit across supported coding agents and generic agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Writers and developers use this skill to set up or diagnose a fiction-writing workspace, including agent instructions, writing references, and platform-specific configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent project hooks can run after setup.

Mitigation: Install only in a trusted writing project and review and trust only the hooks you expect.

Risk: Bypassing hook trust or running a remote upgrade script removes important review opportunities.

Mitigation: Do not automate --dangerously-bypass-hook-trust; avoid the curl-to-bash upgrade path.

Risk: Browser control may access an authenticated Chrome session.

Mitigation: Use browser-cdp only when you intend to grant access to that session.

Risk: Automatic GitHub version checks may be unwanted in restricted environments.

Mitigation: Set STORY_NO_UPDATE_CHECK=1 when automatic update checks are not acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Project link listed in skill metadata (not verified import provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Deployment instructions by host](references/deploy-generic.md)
- [Deployment diagnostics](references/diagnostics.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown setup or diagnostic report with configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local project configuration and agent instruction files when deployment is authorized.]

## Skill Version(s):

1.1.40 (source: ClawHub release metadata; bundled skill frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
