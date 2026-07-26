## Description: <br>
Convert memory, conversation history, or completed tasks into reusable OpenClaw skills that can be packaged and published. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zfanmy](https://clawhub.ai/user/zfanmy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to turn prior conversations, memory markdown, or completed workflow notes into reusable skill packages with scripts, documentation, and optional publishing steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private chat history, memory content, secrets, or personal details can be copied into generated skill files. <br>
Mitigation: Use narrow source files, avoid full session logs when possible, and manually review generated conversation, memory, summary, README, SKILL.md, and script files before publishing. <br>
Risk: Generated files can include executable scripts that are later published externally. <br>
Mitigation: Inspect and sanitize every generated file, scan scripts before use, and confirm the GitHub repository and ClawHub slug before running publish or create-and-publish. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zfanmy/skills/skill-from-memory) <br>
- [Publisher Profile](https://clawhub.ai/user/zfanmy) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions and generated skill files with bash scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local files and publish to GitHub or ClawHub when the bundled scripts are run with credentials and targets.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
