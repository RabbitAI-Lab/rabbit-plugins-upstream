## Description:

Generates a video from a single first-frame image and a text prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn a still image and prompt into a short Jimeng video through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to the dLazy service, and generated media is hosted there.

Mitigation: Only submit prompts and media you are comfortable sharing with the service.

Risk: Logging in stores an API key in the local dLazy CLI configuration, and generation can consume account credits.

Mitigation: Protect the local account configuration, rotate or revoke exposed keys, and check the cost estimate or account balance before generation.

Risk: The external dLazy CLI executable remains unverified, and the examples use flags inconsistently.

Mitigation: Review the CLI source before installation and check `dlazy jimeng-i2v-first -h` to confirm supported flags.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy service](https://dlazy.com)
- [CLI repository (skill metadata link)](https://github.com/dlazy-ai/cli)
- [CLI package (skill metadata link)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video with a JSON result or task-status response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Videos can be 5 or 10 seconds; results can be saved to a local path.]

## Skill Version(s):

1.3.37 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
