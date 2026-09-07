## Description:

Guides agents through safe Mallary CLI, API, MCP, and workflow use for read-only discovery, setup, and clearly requested social-content actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sammydigits](https://clawhub.ai/user/sammydigits)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, CI jobs, and AI agents use this skill to inspect Mallary profiles, connected platforms, posts, jobs, analytics, settings, and webhooks, and to carry out precisely requested Mallary publishing or account-management work with credential and data-handling safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mallary access can publish or manage content on connected social accounts when a user clearly asks.

Mitigation: Require precise profile, destination, content, timing, and expected effect before acting, run each requested action once, and verify results with read-only commands.

Risk: OAuth tokens and API keys can authorize broad Mallary account activity.

Mitigation: Use browser OAuth or a protected secret store, avoid pasting credentials into chat, and never print secrets in logs or shell output.

Risk: Untrusted or one-off CLI installation can expose the agent to a package the user did not intend to trust.

Mitigation: Install only after explicit user approval and prefer a pinned or otherwise trusted Mallary CLI installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sammydigits/skills/mallary)
- [Mallary Website](https://mallary.ai/)
- [Mallary Documentation](https://docs.mallary.ai)
- [Mallary CLI npm Package](https://www.npmjs.com/package/@mallary/cli)
- [Mallary Agent Repository](https://github.com/mallarylabs/mallary-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and redacted operational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only Mallary CLI commands, OAuth setup steps, or user-authorized action guidance; sensitive identifiers and credentials should be redacted.]

## Skill Version(s):

1.1.4 (source: ClawHub release evidence; artifact frontmatter reports 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
