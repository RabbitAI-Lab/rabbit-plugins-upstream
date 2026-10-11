## Description:

Turns a supplied website or URL into a promotional video, social ad, or product demo using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers provide a website URL to make a promotional video, social ad, or product demo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy's hosted service, and attached files are uploaded to dLazy storage.

Mitigation: Use only with content you are comfortable sharing with dLazy; review attachments before sending.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Use the environment-variable option if you do not want the key stored locally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source (linked in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text responses and video project updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation runs through dLazy's hosted service.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
