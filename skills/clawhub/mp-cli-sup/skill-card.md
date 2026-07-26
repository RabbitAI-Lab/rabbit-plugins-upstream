## Description: <br>
Debugs a live WeChat Mini Program runtime through the system `vince-mp` JSON CLI, using a persistent session for page data, element actions, screenshots, scans, console output, health checks, and request-log correlation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to connect an agent to WeChat DevTools and inspect, diagnose, and act on a live Mini Program runtime. It is suited for session-based debugging, UI uid workflows, camera-less scan checks, Skyline/media investigation, project health checks, and backend log correlation by requestId. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on a live WeChat Mini Program by tapping, navigating, changing storage, applying mocks, or instrumenting media and network behavior. <br>
Mitigation: Use non-invasive reads by default, require explicit user requests for state-changing actions, and verify each action with returned CLI JSON evidence. <br>
Risk: Admin credentials and backend logs may expose sensitive operational or user data. <br>
Mitigation: Use admin tokens only when log retrieval is explicitly requested, prefer non-production environments, and redact sensitive log details from summaries. <br>
Risk: Runtime commands depend on a local WeChat DevTools session and the system `vince-mp` CLI being available and compatible. <br>
Mitigation: Start with the session workflow and health checks, report concrete CLI error codes, and avoid switching to unrelated automation backends. <br>


## Reference(s): <br>
- [CLI Contract](references/cli-contract.md) <br>
- [Runtime Protocol](rules/runtime-protocol.md) <br>
- [UI Element Workflow](rules/ui-element-workflow.md) <br>
- [Skyline and Media Workflow](references/skyline-media.md) <br>
- [Evidence and Known Failures](references/evidence-and-failures.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are expected to use structured JSON evidence and keep file outputs under the active workspace root.] <br>

## Skill Version(s): <br>
0.2.1 (source: server evidence, target metadata, frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
