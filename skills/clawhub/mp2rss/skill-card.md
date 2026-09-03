## Description:

mp2rss helps an agent use the Mp2rss CLI to manage WeChat public account and X/Twitter RSS subscriptions, retrieve posts and articles, and manage Feed Key authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[areyoubugcoder](https://clawhub.ai/user/areyoubugcoder)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route natural-language requests into safe Mp2rss CLI commands for RSS subscription management, feed-content lookup, authentication, installation, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remote shell installer could execute code directly during installation.

Mitigation: Prefer the npm package or direct release download path before using a curl-to-shell install command.

Risk: A subscription removal command could remove the wrong WeChat public account if the account identity or mpId is ambiguous.

Mitigation: Confirm the exact public account and mpId before allowing the agent to proceed with removal.

Risk: Authenticated operations expose the configured Feed Key and subscription data to the Mp2rss service.

Mitigation: Use the Feed Key only through the documented CLI authentication flow and avoid exposing full keys in agent output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/areyoubugcoder/skills/mp2rss)
- [Publisher profile](https://clawhub.ai/user/areyoubugcoder)
- [Mp2rss service](https://mp2rss.bugcode.dev)
- [Mp2rss documentation](https://areyoubugcoder.github.io/Mp2RSS/)
- [mp2rss CLI repository](https://github.com/areyoubugcoder/mp2rss-cli)
- [mp2rss CLI releases](https://github.com/areyoubugcoder/mp2rss-cli/releases/latest)
- [Authentication management](references/auth.md)
- [Installation and upgrade](references/install.md)
- [WeChat public account commands](references/mp.md)
- [X/Twitter commands](references/x.md)
- [Error handling](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON parsing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses mp2rss CLI JSON output when structured results are needed; requires a local mp2rss binary and a Feed Key for authenticated operations.]

## Skill Version(s):

0.2.2 (source: server release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
