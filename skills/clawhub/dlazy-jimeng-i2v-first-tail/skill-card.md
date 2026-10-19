## Description:

Helps generate a transition video between supplied first and last frame images using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request a Jimeng transition video from first and last frame images via the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input media are sent to the third-party dLazy service.

Mitigation: Share only content you are authorized to upload; review the service terms before use.

Risk: Login can save an API key locally and global installation persists the CLI.

Mitigation: Use an environment variable for the key or run the pinned CLI with npx if you prefer not to save credentials or install globally.

Risk: Example image flags and sample output disagree with this video workflow.

Mitigation: Check current CLI help and supply firstFrame and lastFrame inputs rather than copying the examples verbatim.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON result links]

**Output Format:** [Markdown guidance and shell commands; CLI results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a hosted asset URL or an asynchronous task ID.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
