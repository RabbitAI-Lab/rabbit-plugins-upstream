## Description:

Audio search tool that searches Pixabay Music for royalty-free track URLs and metadata to support background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to search for royalty-free background music tracks by short English style keywords and return candidate URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and command parameters are sent to dLazy's hosted API.

Mitigation: Use the skill only when use of dLazy's cloud service is acceptable, and avoid placing sensitive information in search queries.

Risk: Authentication may save a dLazy API key in the local CLI configuration.

Mitigation: Protect the local dLazy config, use per-invocation credentials when appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Optional download behavior can write result assets to a local path.

Mitigation: Use the save option only with an explicit destination path chosen for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; search queries should use 2-3 short English style keywords.]

## Skill Version(s):

1.3.11 (source: ClawHub release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
