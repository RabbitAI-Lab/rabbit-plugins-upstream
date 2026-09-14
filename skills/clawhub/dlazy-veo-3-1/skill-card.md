## Description:

Generates high-quality cinematic videos with Google Veo 3.1 from text prompts, image inputs, and video-extension inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke the dLazy Veo 3.1 CLI for text-to-video, image-guided video generation, and video extension workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a pinned third-party dLazy npm CLI and hosted dLazy API endpoints.

Mitigation: Install only if you trust dLazy and the @dlazy/cli npm package; prefer npx or a reviewed and sandboxed install.

Risk: The workflow stores or uses a dLazy API key for authenticated generation requests.

Mitigation: Use a revocable dLazy API key and rotate or revoke it from the dLazy dashboard when access is no longer needed.

Risk: User-supplied media paths may be uploaded to dLazy media storage for generation.

Mitigation: Pass only media files that are intended to be uploaded to dLazy.

Risk: The trigger wording is broad and a sample image flag may not match the documented CLI options.

Mitigation: Check `dlazy veo-3.1 -h` before execution and use the documented options for the selected generation mode.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with inline bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return generated media URLs or save downloaded assets; asynchronous runs may return a task ID for polling.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
