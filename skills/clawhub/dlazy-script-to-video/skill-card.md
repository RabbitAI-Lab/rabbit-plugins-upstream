## Description:

Turns scripts and shot lists into storyboarded, shot-by-shot videos through the dLazy hosted agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a screenplay or scene breakdown into a multi-shot animated video, including storyboarding, shot generation, assembly, and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Only send scripts and files that you are comfortable sharing with dLazy.

Risk: Authentication may save an API key locally, and the CLI can be installed globally.

Mitigation: Protect the local API key; review the CLI package before installing, or use npx to avoid a persistent global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streaming text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project-scoped storyboard and video-generation results from the hosted service.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata; skill frontmatter states 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
