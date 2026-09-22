## Description:

Creates code-driven motion graphics, kinetic typography, animated text videos, animated infographics, and explainer animations as Remotion code, then helps polish and export them rather than generating footage directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to create code-driven animated graphics videos through the dLazy motion-graphics template and continue project-scoped revisions over multiple turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected attached files may be sent to the external dLazy SaaS.

Mitigation: Use the skill only when that data transfer is acceptable, and avoid attaching confidential files unless approved for dLazy processing.

Risk: The dLazy API key is stored locally by the CLI after login or manual configuration.

Mitigation: Protect the local config file and rotate or revoke the key from dLazy if it may have been exposed.

Risk: The skill depends on an npm CLI and external dLazy API and file endpoints.

Mitigation: Review the pinned CLI package and ensure npm, npx, api.dlazy.com, and files.dlazy.com are acceptable in the deployment environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and shell commands returned through the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated project outputs and uploaded user-selected files through the dLazy service.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
