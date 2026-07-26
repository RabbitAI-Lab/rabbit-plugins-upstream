## Description: <br>
Manages persistent OpenClaw startup hooks that run inline commands, local shell or Python scripts, or downloaded URL packages across gateway, pod, and container restarts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw agent operators use this skill to install, manage, test, and audit startup hooks that should persist across restarts or rebuilds. It is intended for initialization, configuration repair, credential restoration, and other boot-time workspace setup tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent startup hooks can run arbitrary code on every OpenClaw boot. <br>
Mitigation: Install only when persistent boot-time execution is intended, review each hook before enabling it, and audit post-init.sh, start.sh, and workspace/.init-hooks during removal or incident review. <br>
Risk: Remote URL hooks can download and execute code from external sources. <br>
Mitigation: Avoid remote URL hooks unless the source is fully trusted and pinned; prefer reviewed local scripts for sensitive initialization tasks. <br>
Risk: Credential-restoration or configuration hooks can affect sensitive local state. <br>
Mitigation: Review credential-handling scripts carefully before use and verify openclaw.json changes and sync targets after execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/init-hooks) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [Hook authoring best practices](references/best-practices.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python command examples, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational instructions for managing persistent startup hooks; it may also direct the agent to run bundled management scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact documentation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
