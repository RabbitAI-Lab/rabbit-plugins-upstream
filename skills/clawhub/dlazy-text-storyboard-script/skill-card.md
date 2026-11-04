## Description:

Turns user themes, structured copy, or outlines into detailed short-video storyboard scripts while preserving the supplied wording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and video production teams can turn a theme, outline, or structured script into shot-by-shot visual directions and spoken lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill promises text-only storyboard writing but also contains directions for image generation, CLI installation, and account setup.

Mitigation: Prefer a text-only storyboard workflow without rendering, installation, or authentication steps.

Risk: Cloud rendering may send prompts or media to dLazy and incur API charges; the external CLI implementation and credential-storage permissions are unverified.

Mitigation: Before cloud rendering, obtain explicit approval for the data shared and any charges; use device login rather than entering an API key in a command.

## Reference(s):

- [CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [CLI package on npm (linked in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage (linked in skill metadata)](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured shot headings and labeled fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes global video ratio, resolution, and dimensions, plus per-shot scene, camera, notes, and spoken copy.]

## Skill Version(s):

1.2.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
