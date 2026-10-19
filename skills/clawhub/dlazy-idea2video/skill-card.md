## Description:

Turns a creative idea into a reviewable video-production plan, then organizes story, character, scene, image, and video-generation steps on a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams can turn an idea into a staged video workflow, review the plan, and generate visual and video assets using dLazy services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks the agent to run dLazy CLI commands, including optional persistent installation.

Mitigation: Review commands before execution; use npx instead of a global installation if preferred, and run one generation command at a time.

Risk: API keys may be saved locally, and prompts or selected media are sent to dLazy services.

Mitigation: Use an environment variable instead of saving the key if preferred, and share only prompts and media you are comfortable sending to dLazy.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package linked by the skill](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project linked by the skill](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Conversational plan summaries and generation instructions with resulting media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User confirmation gates precede plan application and individual CLI generation commands.]

## Skill Version(s):

1.3.34 (source: ClawHub release metadata; embedded skill frontmatter says 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
