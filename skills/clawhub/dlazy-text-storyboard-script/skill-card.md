## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines while preserving spoken-script text word for word.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and video-production teams use this skill to turn structured copy or outlines into shot-by-shot short-video storyboard scripts with scene, camera, note, technique, and spoken-script sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags the skill as suspicious because it presents as a text storyboard generator while also installing and directing use of a networked dLazy media-generation CLI.

Mitigation: Review the @dlazy/cli package and account terms before installation, and install only when a dLazy-powered media workflow is intended.

Risk: Prompts and referenced media paths may be sent to dLazy services and generated result URLs may be hosted by files.dlazy.com.

Mitigation: Avoid sensitive input, use a revocable API key, and prefer npx for testing before installing the CLI globally.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown storyboard script with basic video parameters and repeated shot sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves user-provided spoken script text verbatim and defaults unspecified video parameters to 9:16 at 720p.]

## Skill Version(s):

1.2.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
