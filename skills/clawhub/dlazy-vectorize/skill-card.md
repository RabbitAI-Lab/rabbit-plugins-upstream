## Description:

Converts raster images such as PNG and JPG into color vector SVG and returns a URL for scalable reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can convert logos, icons, and flat illustrations from PNG or JPG into color SVG assets for scalable reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image files and prompts sent through the hosted conversion workflow may contain sensitive information.

Mitigation: Only upload images and prompts that are appropriate to share with dLazy for cloud processing.

Risk: API calls use paid organization credits.

Mitigation: Review the cost estimate with --dry-run and check available credits before submitting a conversion.

Risk: The dLazy organization API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local configuration and environment, and rotate or revoke the key if it may have been exposed.

Risk: The examples contain inconsistent fields, so returned output may not match the expected SVG format.

Mitigation: Inspect the returned file and confirm that it is a valid SVG before relying on it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image asset, URL, JSON response]

**Output Format:** [Hosted asset URL in a JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID; verify the returned file format before relying on SVG output.]

## Skill Version(s):

1.2.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
