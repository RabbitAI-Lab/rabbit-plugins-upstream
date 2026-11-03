## Description:

Convert static character images into action videos using Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to turn a still character image into an action video by providing a prompt and image to Jimeng Dream Actor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy hosted services, and generation uses service credits.

Mitigation: Only submit media and prompts intended for cloud processing, and use the documented --dry-run option to review the payload and estimated cost before generation.

Risk: The reusable API key is saved in the CLI configuration unless supplied per invocation.

Mitigation: Protect the key and configuration file, avoid exposing the key in prompts or shared logs, and rotate or revoke it if exposed.

Risk: The pinned external CLI implementation and its claimed credential-file permissions were not independently verified.

Mitigation: Review the pinned CLI source before installing it and verify the actual permissions on the credential configuration file.

## Reference(s):

- [CLI project link listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Hosted video asset or JSON generation/task result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may complete asynchronously; an output can optionally be saved to a local path.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
