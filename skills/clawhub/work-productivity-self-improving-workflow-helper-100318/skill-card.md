## Description: <br>
Helps agent users, skill authors, maintainers, and teams turn self-improving workflow needs into practical plans, checklists, scripts, code changes, analysis, and validation notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to adapt popular self-improving workflow patterns into reliable local workflows for bug fixing, setup hardening, reliability improvement, adjacent skill creation, and decision support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad requests about improvement, logs, or bug fixes. <br>
Mitigation: Prefer explicit invocation or narrower routing rules, and confirm the planning workflow is appropriate before using it to guide code or skill changes. <br>
Risk: The skill can produce implementation support such as code changes, scripts, shell commands, or configuration snippets that may be incorrect for the user's environment. <br>
Mitigation: Review generated changes before use and validate outputs against the stated success criteria, assumptions, limits, and remaining risks. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent) <br>
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving) <br>
- [Bound platform-admin Firestore list reads on the admin dashboard](https://github.com/pauljsnider/allplays/issues/3455) <br>
- [OpenClaw must-install Skills article](https://segmentfault.com/a/1190000047666647) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, templates, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, limits, validation notes, remaining risks, and next steps when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
