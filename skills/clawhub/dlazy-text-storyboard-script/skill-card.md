## Description:

Storyboard script generator, taking user-provided themes, structured copy (such as a script containing hooks, suspense, story development, core viewpoints), or outlines, dismantling them into detailed short video storyboard scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video producers use this skill to turn themes, structured copy, or outlines into detailed short video storyboards with scene descriptions, camera direction, and shot notes while preserving the supplied spoken copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment rates the skill suspicious because of reported undeclared CLI authentication and an external image-generation workflow in a storyboard task; external data handling and possible charges may apply. The scan was partial, so its evidence is incomplete.

Mitigation: Review the CLI behavior and data sent to dLazy before use, and confirm service charges before generation. If using the service, protect the API key and rotate or revoke it when needed.

## Reference(s):

- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with storyboard headings and structured shot fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the user's original spoken copy verbatim; defaults video parameters to 9:16 and 720p when unspecified.]

## Skill Version(s):

1.2.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
