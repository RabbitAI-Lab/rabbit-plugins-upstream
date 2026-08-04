## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague errors into clearer messages that explain what failed, why it failed, and what to do next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and affected users use this skill to rewrite confusing error states into actionable messages, checklists, templates, analyses, code changes, or decision support. It is intended for troubleshooting and support workflows where users need clear failure cause and next-step guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms may route the skill into general debugging or support conversations where another skill would be more precise. <br>
Mitigation: Invoke it explicitly for error-message rewrite work, choose a more specific skill for unrelated debugging, or disable implicit invocation when routing precision matters. <br>
Risk: The skill can produce wording or implementation suggestions that may still be inaccurate for a specific product state. <br>
Mitigation: Review generated messages against product behavior, logs, and support policy before shipping them to users. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-120249) <br>
- [Developer Onboarding Funnel Metrics with Dropoff Analysis](https://github.com/sethdford/shipwright/issues/746) <br>
- [FEATURE: Improved error handling](https://github.com/Ankita15k/GitNest/issues/746) <br>
- [SegmentFault error-messages](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with optional code and checklist sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and next-step guidance.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
