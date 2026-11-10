## Description:

Generate coherent transition videos using Jimeng's first and tail frame models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can provide a prompt and first and tail frame images to create a coherent transition video with Jimeng through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had partial reference coverage and did not establish how the CLI login flow connects to video generation.

Mitigation: Review the dLazy CLI and login flow before connecting an account.

Risk: Prompts and local image files are sent to dLazy hosted services for processing.

Mitigation: Use only prompts and images you are comfortable sharing with that service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Hosted video asset URL or saved video file, with a JSON result response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transition video generated from first and tail frame images; 5- or 10-second duration; generation may return asynchronously.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
