## Description:

Generates a video from a single first-frame image and a text prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can turn a still image and prompt into a 5- or 10-second Jimeng video. The skill returns generated media and can save it to a local path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy services, and generation may incur charges.

Mitigation: Send only media and prompts you are comfortable processing in the cloud, and confirm you accept the generation charges before running the request.

Risk: The CLI stores its API key in a local user configuration file when using the login flow.

Mitigation: Choose whether to store the key on the current device, protect access to the configuration, and rotate or revoke the key if needed.

Risk: The documented command examples use an image-input flag that differs from the listed option.

Mitigation: Check `dlazy jimeng-i2v-first -h` and follow the installed CLI's help before sending a request.

## Reference(s):

- [dLazy CLI repository (metadata link; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video asset with JSON task or result metadata]

**Output Parameters:** [1D (prompt, first-frame image, duration)]

**Other Properties Related to Output:** [The result may be returned as a hosted asset or saved locally; asynchronous requests can return a task ID.]

## Skill Version(s):

1.3.33 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
