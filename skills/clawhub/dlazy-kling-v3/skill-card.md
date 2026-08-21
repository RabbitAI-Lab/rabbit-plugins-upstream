## Description:

Powerful video generation with Kling v3, supporting high-quality text-to-video and image-to-video through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Kling v3 videos from text prompts and optional image references through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only when cloud processing by dLazy is intended, avoid submitting sensitive media, and review the generated payload with dry-run when appropriate.

Risk: Authentication requires a dLazy API key that may be saved in the local CLI configuration.

Mitigation: Use scoped keys, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables for temporary use.

Risk: Global CLI installation persists an executable on the system and API calls may consume account credits.

Mitigation: Use the pinned npx invocation for temporary runs and dry-run mode to estimate cost before submitting generation requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated media URLs or asynchronous task status, plus concise command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local media paths supplied by the user may be uploaded to dLazy; dry-run mode can preview payload and cost before an API call.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
