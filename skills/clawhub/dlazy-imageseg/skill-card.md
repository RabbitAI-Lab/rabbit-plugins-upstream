## Description:

This skill uses the dLazy image matting CLI/API to separate foregrounds from image backgrounds and return transparent PNG result URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to run dLazy image segmentation for product photos, character cutouts, and compositing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the dLazy npm CLI and hosted API, so image inputs may be uploaded to dLazy services for processing.

Mitigation: Install only when the user accepts dLazy CLI and cloud-service trust requirements, and only process images suitable for upload to dLazy.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer revocable organization API keys, protect the local config file, and rotate or revoke the key if the machine or CLI environment is no longer trusted.

Risk: A persistent global npm install expands the trusted local toolchain.

Mitigation: Use the pinned on-demand command npx @dlazy/cli@1.2.3 for non-persistent use, and avoid running npm with administrator privileges.

## Reference(s):

- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI returns hosted PNG image URLs, or an asynchronous task identifier when --no-wait is used.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
