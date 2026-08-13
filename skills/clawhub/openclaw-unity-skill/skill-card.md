## Description:

Unity Plugin lets agents control a trusted local Unity Editor through OpenClaw for scene management, GameObject and component changes, debugging, input simulation, Play Mode control, and related development workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomleelive](https://clawhub.ai/user/tomleelive)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill to inspect and modify Unity projects through OpenClaw, including scene, asset, prefab, test, package, input, and Play Mode workflows in a local or gateway-connected editor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute C# and perform project-changing Unity Editor actions.

Mitigation: Install only for trusted, source-controlled local Unity projects and require explicit approval before script.execute, package changes, deletes, saves, broad input simulation, or other state-changing actions.

Risk: The Unity bridge exposes powerful editor control through a local runtime surface.

Mitigation: Keep the bridge bound to localhost and do not expose it beyond the trusted local machine or network.

Risk: Package installation can add external code to the Unity project.

Mitigation: Verify package names, Git URLs, and expected effects with the user before package changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tomleelive/skills/openclaw-unity-skill)
- [OpenClaw Unity Skill Repository](https://github.com/TomLeeLive/openclaw-unity-skill)
- [OpenClaw Unity Plugin Repository](https://github.com/TomLeeLive/openclaw-unity-plugin)
- [OpenClaw Docs](https://docs.openclaw.ai)
- [Tool Reference](references/tools.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and unity_execute tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide Unity Editor automation through OpenClaw gateway or local MCP bridge workflows.]

## Skill Version(s):

1.6.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
