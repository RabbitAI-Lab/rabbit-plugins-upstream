## Description: <br>
Canvas as an app platform. Build, store, and run rich visual apps on the OpenClaw Canvas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fraction12](https://clawhub.ai/user/fraction12) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw agent users use Canvas OS to build, serve, load, and update rich HTML/CSS/JavaScript Canvas apps such as dashboards and trackers. It helps agents present visual interfaces on Canvas through localhost serving, direct HTML injection, JavaScript updates, and app templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper can start background local HTTP servers and forcibly stop processes on selected ports. <br>
Mitigation: Check what is listening on the target port before running the helper and use dedicated Canvas app ports to avoid stopping unrelated local services. <br>
Risk: Direct Canvas loading injects active HTML and JavaScript into the Canvas page. <br>
Mitigation: Use trusted, self-contained HTML only, avoid remote content, and review generated JavaScript before evaluation. <br>
Risk: Canvas apps can send openclaw:// callbacks back to the agent. <br>
Mitigation: Treat callbacks as untrusted requests and require user confirmation before taking actions from them. <br>
Risk: Localhost serving can expose app content beyond the intended Canvas workflow if bound too broadly. <br>
Mitigation: Prefer binding local servers to 127.0.0.1 and close servers when the Canvas app session ends. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fraction12/skills/canvas-os) <br>
- [Canvas Loading Reference](CANVAS-LOADING.md) <br>
- [Canvas OS README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell, Python, JavaScript, HTML, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local Canvas app instructions, helper commands, and self-contained HTML app templates for OpenClaw Canvas workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
