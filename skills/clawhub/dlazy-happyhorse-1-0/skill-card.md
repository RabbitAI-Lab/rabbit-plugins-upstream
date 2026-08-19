## Description:

Happy Horse 1.0 is a dLazy-hosted video generation skill that routes text-to-video, first-frame-to-video, reference-to-video, and video editing requests to the matching Happy Horse sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit short videos through dLazy's Happy Horse 1.0 hosted service using prompts, images, and optional video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be uploaded to dLazy's hosted API and media storage for processing.

Mitigation: Review prompts and file paths before invocation, and avoid submitting sensitive media unless dLazy's service terms and data handling are acceptable.

Risk: Authentication can persist an organization API key in the local dLazy CLI configuration.

Mitigation: Prefer per-run DLAZY_API_KEY usage for temporary access, or verify local config file permissions and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated outputs are hosted on dLazy infrastructure and returned as URLs.

Mitigation: Treat returned URLs as externally hosted artifacts and apply the user's normal sharing, retention, and review controls before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Hosted media URLs, Guidance]

**Output Format:** [JSON response with generated media URLs or asynchronous task status, plus agent guidance for command execution and errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are hosted by dLazy; async runs may return a generateId for later polling.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter declares 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
