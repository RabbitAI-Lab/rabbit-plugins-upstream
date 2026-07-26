## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague errors into clear messages that explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and affected users use this skill to improve vague or blocking error messages into actionable troubleshooting guidance, reusable checklists, workflows, analysis, or implementation support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms may activate the workflow for general debugging or support requests where an error-message improvement workflow was not intended. <br>
Mitigation: Prefer explicit invocation for normal use; maintainers should narrow triggers to explicit error-message rewrite or troubleshooting-message improvement requests. <br>
Risk: Outputs may shape user-facing troubleshooting guidance, so unsupported assumptions could produce unclear or misleading next steps. <br>
Mitigation: Validate each output against the stated failure, likely cause, and next action; keep assumptions, limits, and remaining verification steps visible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-110318) <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [Dify Agent backend deployment issue](https://github.com/langgenius/dify/issues/39161) <br>
- [Dart FutureOr error-message issue](https://github.com/dart-lang/sdk/issues/63818) <br>
- [Medusa migration deadlock issue](https://github.com/medusajs/medusa/issues/16011) <br>
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional checklists, code snippets, shell commands, and implementation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no direct code execution or data access.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
