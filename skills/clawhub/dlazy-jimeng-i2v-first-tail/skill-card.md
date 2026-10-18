## Description:

Generate coherent transition videos from first and last frame images using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate transition videos from a first frame, last frame, and prompt through the dLazy Jimeng CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy cloud services, which also host generated outputs.

Mitigation: Review the material before sending it and use only content appropriate for the service.

Risk: Installing the third-party CLI grants it access to supplied media and credentials.

Mitigation: Review the pinned @dlazy/cli package before installation; prefer on-demand npx or a per-invocation DLAZY_API_KEY to reduce persistence.

Risk: The documented examples use an inconsistent --image flag.

Mitigation: Use the documented --firstFrame and --lastFrame options instead.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands; the CLI returns JSON with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous calls may return a task ID; the CLI can save generated media locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
