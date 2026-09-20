## Description:

Happy Horse 1.0 generates and edits video from text prompts, first-frame images, reference images, or existing video through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit videos with Happy Horse 1.0 by invoking the dLazy CLI with prompts, media inputs, resolution, aspect ratio, duration, and save or async options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and supplied media may be sent to dLazy hosted API and storage endpoints.

Mitigation: Avoid passing private or sensitive media unless the user is comfortable uploading it to dLazy for processing.

Risk: The skill uses a dLazy API key that may be saved in the local CLI configuration.

Mitigation: Use normal local credential hygiene and rotate or revoke the API key from the dLazy dashboard if exposure is suspected.

Risk: A global npm install leaves a persistent third-party CLI on the system.

Mitigation: Use the pinned npx invocation when a persistent global CLI is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown instructions with CLI command examples and JSON result payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs, async task identifiers, or local saved assets when the dLazy CLI save option is used.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
