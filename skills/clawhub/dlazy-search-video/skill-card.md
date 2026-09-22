## Description:

Video search tool that queries the Pixabay video API by keyword and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to find stock video clips by keyword, category, type, duration, and pagination parameters. It is suited for footage sourcing workflows that need returned video URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the third-party dLazy CLI and dLazy-hosted endpoints with API-key-authenticated requests.

Mitigation: Install and run it only when the user is comfortable sending search inputs and authenticated requests to dLazy services.

Risk: A saved API key may persist in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The save option can write downloaded assets to a local path.

Mitigation: Use --save only with an intentionally chosen path and review downloaded assets before reusing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON results from the dLazy CLI, with command-line guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when run with no-wait behavior; saved assets are written only when a save path is provided.]

## Skill Version(s):

1.3.20 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
