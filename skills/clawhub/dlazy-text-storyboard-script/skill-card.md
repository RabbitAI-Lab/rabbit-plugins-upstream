## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn complete source copy or outlines into structured storyboard scripts with shot planning, camera guidance, notes, and spoken-script allocation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill is advertised as a text-only storyboard helper while also directing agents toward third-party CLI image generation and hosted result URLs.

Mitigation: Install and run it only when third-party dLazy CLI use, prompt or media transfer to dLazy-hosted services, and hosted output URLs are acceptable for the workflow.

Risk: The security guidance notes that the skill requires a locally available dLazy API key.

Mitigation: Keep the API key in the supported local configuration or environment variable, rotate or revoke it as needed, and avoid using the skill where third-party credentials are not approved.

Risk: The security guidance says the skill is over-scoped and internally inconsistent for text-only storyboard drafting.

Mitigation: For text-only drafting, constrain the agent to produce storyboard script text and do not allow CLI execution unless image generation is explicitly intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown storyboard script with structured sections and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes global video parameters and per-shot fields for paragraph function, scene, camera movement, notes, shooting technique, and spoken script.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
