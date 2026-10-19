## Description:

Guides agents to generate short videos from text or images using Google Veo 3.1 Fast through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short text-to-video or image-to-video generation and video extension through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI requires an API key and may store it locally.

Mitigation: Protect the local configuration file, or provide the key per invocation instead.

Risk: Prompts and supplied media are sent to dLazy's cloud service.

Mitigation: Submit only prompts and files you intend to share with dLazy.

Risk: Using the globally installed CLI leaves an external package on the system.

Mitigation: Review the package before installation and use the pinned npx option to avoid a persistent global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source referenced by skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions; CLI results are JSON with generated asset URLs or asynchronous task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may be saved locally or accessed by a returned URL.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
