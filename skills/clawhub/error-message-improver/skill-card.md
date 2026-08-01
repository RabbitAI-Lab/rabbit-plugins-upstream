## Description: <br>
Helps developers, support teams, and SaaS operators turn vague failures into clearer error messages that explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to convert unclear errors into actionable troubleshooting guidance, templates, checklists, analyses, code changes, or implementation support. It is best suited for communication and support workflows around error handling, not full runtime diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad debugging or support requests when the user needs runtime diagnosis rather than clearer error-message wording. <br>
Mitigation: Use this skill for communication, support, and troubleshooting-message improvements; invoke a more specific debugging skill when code execution, logs, or runtime behavior need diagnosis. <br>
Risk: Generated wording can omit important context if the user provides only a vague original error. <br>
Mitigation: Ask only for missing details that materially affect the message, then state assumptions, constraints, validation notes, and remaining follow-up work. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver) <br>
- [Evidence: No Reference Paths Found](https://github.com/vgteam/vg/issues/4974) <br>
- [Evidence: Unsafe unwrap() Calls](https://github.com/bytedance/g3/issues/1102) <br>
- [Evidence: SegmentFault error-messages](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reusable checklists, workflows, assumptions, validation notes, and follow-up risks when useful.] <br>

## Skill Version(s): <br>
0.20260730.234524 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
