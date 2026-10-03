## Description:

Connects an agent to dLazy's project-scoped sandbox assistant for multi-turn conversations and skill execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can start or continue project-based conversations with a hosted agent, select skills, and provide reference files when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy's hosted service.

Mitigation: Avoid sharing sensitive prompts or options unless you trust the service.

Risk: Files specified with --files are uploaded to dLazy.

Mitigation: Review files before attaching them and avoid uploading sensitive content.

Risk: Logging in can store an API key locally.

Mitigation: Use a per-run environment key when local credential persistence is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI repository (linked in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streaming conversational text; format varies by selected skill]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped multi-turn replies.]

## Skill Version(s):

1.2.26 (source: ClawHub release; bundled skill frontmatter says 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
