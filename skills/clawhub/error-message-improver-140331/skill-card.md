## Description: <br>
Helps agents improve vague error messages by explaining what failed, why it failed, and what action the user should take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Application developers, support teams, SaaS operators, and end users use this skill to turn unclear troubleshooting messages into actionable guidance. It can produce revised error text, reusable checklists, workflows, analysis, code changes, or decision support for debugging and support scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad debugging or support prompts where the user did not specifically request error-message wording help. <br>
Mitigation: Prefer explicit invocation when the task is specifically to improve troubleshooting copy or error-message guidance. <br>
Risk: Improved error text can still be misleading if the root cause or operational context is wrong. <br>
Mitigation: Validate proposed wording against the actual failure mode, logs, and user-facing recovery path before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-140331) <br>
- [OpenShift Impersonation for Multi-Cluster Auth](https://github.com/kiali/kiali/issues/10038) <br>
- [error[vg call] No reference paths found](https://github.com/vgteam/vg/issues/4974) <br>
- [SegmentFault error-messages](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, with code blocks or checklists when useful] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should expose assumptions, limits, validation notes, and next steps when helpful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
