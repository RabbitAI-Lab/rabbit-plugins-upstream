## Description:

Motion graphics, kinetic typography, animated text video, animated infographic, and explainer animation authored as Remotion code for text, shapes, data, logos, and transitions, then polished and exported.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to start or continue dLazy motion-graphics projects that produce code-driven animated graphics, animated infographics, kinetic typography, and explainer videos rather than AI-generated footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a pinned third-party npm CLI that communicates with dLazy hosted services.

Mitigation: Review the dLazy CLI source or npm package before installing in sensitive environments, prefer npx or an isolated user account, and avoid running npm with elevated privileges.

Risk: The dLazy API key can be saved in local CLI configuration or supplied through an environment variable.

Mitigation: Treat the key as a credential, limit local account access, and rotate or revoke the key if it may have been exposed.

Risk: Files attached through the CLI may be uploaded to dLazy media storage before use.

Mitigation: Attach only files that are appropriate to upload to dLazy and avoid submitting sensitive material unless the environment and account controls allow it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and code-oriented motion-graphics instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent replies may be streamed through the pinned dLazy CLI and associated with project-scoped sessions.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
