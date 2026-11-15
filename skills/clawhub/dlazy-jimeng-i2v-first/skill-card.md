## Description:

Generate dynamic videos based on a single first-frame image and prompts using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can use this skill to request Jimeng video generation from a first-frame image and a prompt. The supplied security assessment says the observed command only logs in, so confirm that the generation workflow works before relying on it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports that the supplied skill describes video generation while the observed command only logs in; some referenced install details and paths were not inspected.

Mitigation: Before relying on generation, review the actual command behavior and inspect the referenced install details and paths.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project page listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions]

**Output Format:** [JSON result with media URLs, plus shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated media is hosted by the service; asynchronous requests may initially return a task identifier.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
