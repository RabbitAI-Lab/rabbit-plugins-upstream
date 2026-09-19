## Description:

GPT Image 2 supports text-to-image generation plus image editing and synthesis from reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy GPT Image 2 CLI for text-to-image generation, image editing, and image synthesis with up to five reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference files are sent to the third-party dLazy API and media storage.

Mitigation: Avoid submitting sensitive prompts or files unless the user is comfortable uploading them to dLazy.

Risk: Authentication can persist a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or the npx install alternative when less local persistence is preferred.

Risk: Generated outputs are hosted by dLazy and may be returned as files.dlazy.com URLs.

Mitigation: Review hosted output handling and retention expectations before using generated assets in sensitive workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions]

**Output Format:** [Markdown guidance with bash examples and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs or save image files; async mode returns a task identifier for polling.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
