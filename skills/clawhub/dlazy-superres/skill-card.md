## Description:

Enhances images with dLazy's hosted super-resolution service and returns a URL for the upscaled result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to improve clarity and detail in low-resolution images and retrieve an upscaled result URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images are uploaded to dLazy's hosted service for processing, and processing may incur charges.

Mitigation: Only submit images you trust dLazy to process, check the service's privacy and retention terms, and confirm charges before use.

Risk: The saved organization API key could be exposed if local CLI configuration is accessed by others.

Mitigation: Protect the local API-key configuration and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image, URL, JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON containing the enhanced image URL and output metadata; optionally a downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task identifier for asynchronous jobs; image inputs are sent to the hosted service for processing.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
