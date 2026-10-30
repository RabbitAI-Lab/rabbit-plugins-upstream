## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn a static character image into an action video by providing a prompt and image to Jimeng Dream Actor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media are sent to dLazy hosted services for generation.

Mitigation: Submit only media you are comfortable uploading and review the service terms.

Risk: Video generation can incur usage costs.

Mitigation: Use the documented dry-run option to preview the request and cost estimate before calling the API.

Risk: The separately installed CLI uses an API key to authenticate requests.

Mitigation: Protect the API key and review the CLI before installing or running it.

## Reference(s):

- [Clawhub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Hosted media URL and JSON response; optionally a saved media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before the generated media is ready.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
