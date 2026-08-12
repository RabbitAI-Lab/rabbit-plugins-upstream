## Description:

Control Unreal Engine Editor through the OpenClaw Unreal Plugin for level and actor management, transforms, PIE control, debugging, input simulation, console commands, screenshots, and logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomleelive](https://clawhub.ai/user/tomleelive)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and Unreal Engine teams use this skill to inspect and modify trusted local Unreal Editor projects through OpenClaw. It supports common editor tasks such as listing levels and actors, creating or deleting actors, changing transforms, starting PIE, running console commands, collecting logs, and taking screenshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad Unreal Editor authority, including operations that can change or damage a project.

Mitigation: Install only for trusted local projects, keep projects under source control, and require explicit user confirmation before actor deletion, level save/open, console execution, asset import, input simulation, screenshots, or log sharing.

Risk: Screenshot and log tools can expose credentials, tokens, source paths, or sensitive project details.

Mitigation: Review screenshots and logs before sharing them outside the local machine.

Risk: Local editor-control bridges can receive commands from local processes if authentication is not configured.

Mitigation: Use the optional shared-secret token when supported and keep the bridge available only on trusted machines.

Risk: Routine requests can map to state-changing editor actions.

Mitigation: Confirm once before the first state-changing call in a session, especially for vague requests such as cleanup, save, run, or import tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tomleelive/skills/openclaw-unreal-skill)
- [OpenClaw Unreal Skill homepage](https://github.com/TomLeeLive/openclaw-unreal-skill)
- [OpenClaw Unreal Plugin](https://github.com/openclaw/openclaw-unreal-plugin)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON tool results and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May queue state-changing Unreal Editor commands and return screenshots or project logs through tool results.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter, package.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
