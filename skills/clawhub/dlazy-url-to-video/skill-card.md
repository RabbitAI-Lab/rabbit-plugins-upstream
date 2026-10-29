## Description:

Turns a webpage URL into a promotional, social ad, or product demo video through dLazy’s hosted website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating product marketing and demo content use this skill to turn a website URL into a promotional, social ad, or product demo video, with optional reference file attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URLs and attached files are sent to dLazy’s hosted service, and service credits may be consumed.

Mitigation: Share only URLs and files you are comfortable sending to dLazy, and account for service credit usage.

Risk: The CLI stores the organization API key locally, while its implementation and hosted backend are outside the bundled skill files.

Mitigation: Protect the saved API key and review the pinned CLI before installation.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance, Shell commands]

**Output Format:** [Generated promotional or demo video with conversational text and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through a hosted service; local reference files may be uploaded when attached.]

## Skill Version(s):

1.0.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
