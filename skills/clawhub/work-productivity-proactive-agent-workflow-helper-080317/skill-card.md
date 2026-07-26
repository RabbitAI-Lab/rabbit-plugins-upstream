## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical proactive-agent workflows, checklists, analysis, code changes, and verification notes for productivity and reliability tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, maintainers, and teams use this skill to turn proactive-agent productivity needs into concrete workflows, checklists, templates, analysis, code changes, or decision support. It is intended for local-hardware-friendly work that clarifies goals, produces an actionable artifact, and validates the result against success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit invocation may cause the skill to activate when a user did not explicitly request this workflow. <br>
Mitigation: Narrow the trigger phrases or disable implicit invocation when deployments require explicit user selection. <br>
Risk: Generated workflow or implementation guidance could be incorrect or too general for the user's environment. <br>
Mitigation: Validate outputs against the stated success criteria and keep assumptions, limits, and follow-up checks visible to the user. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-proactive-agent-workflow-helper-080317) <br>
- [Popular ClawHub skill demand: Proactive Agent](https://clawhub.ai/skills/proactive-agent) <br>
- [Popular ClawHub skill demand: Self-Improving + Proactive Agent](https://clawhub.ai/skills/self-improving) <br>
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology) <br>
- [Feed-poll HTTP client hardening issue](https://github.com/wmo-raf/cap-aggregator/issues/78) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tailored artifacts, reusable checklists or workflows, and verification notes.] <br>

## Skill Version(s): <br>
0.1.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
