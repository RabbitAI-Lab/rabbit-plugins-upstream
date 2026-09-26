## Description:

Generates detailed short video storyboard scripts from user-provided themes, structured copy, or outlines while preserving spoken script text verbatim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to turn structured copy, outlines, or themes into shot-by-shot short video storyboard scripts with scene, camera, notes, and spoken-script sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as a text storyboard helper but can direct agents toward installing and using the dLazy CLI for external generation.

Mitigation: Review skill behavior before deployment and require explicit user confirmation before running CLI commands or external generation steps.

Risk: Prompts and local media paths may be sent to dLazy cloud endpoints at api.dlazy.com and files.dlazy.com.

Mitigation: Use the skill only when cloud processing is acceptable and review prompts or media paths for sensitive information before submission.

Risk: Use of the dLazy CLI requires a locally stored or environment-provided API key.

Mitigation: Use a dedicated dLazy API key, protect the local configuration file, and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown storyboard script with structured shot sections and optional inline shell commands for dLazy CLI setup or generation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Storyboard outputs include video parameters, shot function, scene description, camera movement, notes, shooting technique, and verbatim spoken script.]

## Skill Version(s):

1.2.16 (source: server release evidence; artifact frontmatter reports 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
