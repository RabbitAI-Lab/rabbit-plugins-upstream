## Description:

motion graphics, kinetic typography, animated text video, animated infographic, explainer animation — authored as Remotion code (text, shapes, data, logos, transitions), then polished and exported. Use for code-driven animated graphics rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content creators can use this skill to create code-driven motion graphics such as kinetic typography, animated infographics, and explainer animations, then polish and export the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill configures dLazy CLI authentication and can list organization projects; the security review says these steps are not fully explained by its animation purpose and notes that the CLI was not inspected.

Mitigation: Review the CLI and its access before authenticating, use credentials only for an organization you trust, and revoke the API key if you no longer use the skill.

Risk: Prompts and attached local files are sent to dLazy hosted services, as described in the skill documentation.

Mitigation: Avoid sending confidential prompts or files unless your organization permits sharing them with dLazy and you have reviewed the applicable service terms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy website](https://dlazy.com)
- [CLI source URL listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Remotion project code and motion-graphics files, with command-line instructions and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or continue a project and export an animated video; attached local files are uploaded to dLazy media storage.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
