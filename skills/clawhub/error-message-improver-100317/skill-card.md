## Description: <br>
Helps application developers, support teams, SaaS operators, and users turn vague error messages into clearer explanations of what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and end users use this skill to clarify error-message goals, produce tailored wording, checklists, workflows, analysis, or code-oriented guidance, and validate that the result is actionable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may cause the skill to trigger during general support or debugging requests. <br>
Mitigation: Tighten trigger wording or disable implicit invocation when a narrower error-message-improvement workflow is desired. <br>
Risk: Generated error-message guidance may be incomplete if the user omits logs, failure context, audience, or success criteria. <br>
Mitigation: Ask for materially missing details, state assumptions clearly, and validate the output against the known failure context before use. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-100317) <br>
- [Improve error messages in config](https://github.com/yrn-dev/project-zero-1773324380/issues/126) <br>
- [Error Messages Topic](https://segmentfault.com/t/error-messages) <br>
- [Designing APIs for Agents](https://news.ycombinator.com/item?id=48929039) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with prose, checklists, templates, code snippets, or command examples as requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include visible assumptions, limits, validation notes, and next steps when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
