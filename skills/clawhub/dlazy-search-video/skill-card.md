## Description:

Video search tool that queries the Pixabay video API by keyword and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to search for stock video assets by keyword and retrieve video URLs and metadata through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy as an intermediary service and requires a dLazy API key.

Mitigation: Install only if that SaaS dependency is acceptable, protect the API key, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Search requests and eligible media inputs may be sent to dLazy service endpoints.

Mitigation: Avoid submitting sensitive prompts or files unless the user has approved sending them to dLazy-hosted services.

Risk: The CLI can save returned assets to a local path.

Mitigation: Use the save option only with a path the user explicitly approves.

Risk: A global CLI install persists the dLazy binary on the system.

Mitigation: Prefer the pinned npx invocation when the user does not want a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI project link](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON response envelope with stock video URLs and metadata, described through Markdown usage guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports query, video type, category, duration, pagination, dry-run, async task polling, timeout, and optional local save path parameters.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
