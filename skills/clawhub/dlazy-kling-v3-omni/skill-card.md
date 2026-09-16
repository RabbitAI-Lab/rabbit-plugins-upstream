## Description:

Generates videos with Kling v3 Omni from prompts and image inputs through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run dLazy's Kling v3 Omni video generation CLI with prompt, image, and optional video references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external @dlazy/cli npm package.

Mitigation: Install only when you trust dLazy and prefer npx or a local install over a persistent global install when possible.

Risk: The dLazy API key is stored locally or passed through the environment.

Mitigation: Use a revocable API key, restrict local config file access to the operating-system user, and rotate or revoke the key if exposure is suspected.

Risk: User-selected media files are uploaded to dLazy's cloud service for generation.

Mitigation: Pass only media files intended for upload to dLazy and review cloud-service handling requirements before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated media URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download generated media to a user-specified save path; async mode returns a generateId for polling.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
