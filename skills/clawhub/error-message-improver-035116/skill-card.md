## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague error messages into clear explanations, next actions, checklists, and validation notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and end users use this skill to rewrite unclear error messages so they explain what failed, why it failed, and what action to take next. It can produce a tailored response, reusable workflow or checklist, implementation support, and a short verification note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the skill to be invoked for adjacent debugging or support requests where error-message improvement is not the main task. <br>
Mitigation: Invoke the skill explicitly for error-message work or tighten implicit routing where the host environment supports that. <br>
Risk: A rewritten error message can be misleading if the original error, user impact, or expected recovery action is underspecified. <br>
Mitigation: Follow the skill workflow by restating the outcome and constraints, asking only for materially missing information, and validating the result against the stated success criteria. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-035116) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Dart SDK issue: unawaited should support FutureOr](https://github.com/dart-lang/sdk/issues/63818) <br>
- [Dart language issue: const constructor initializer inference](https://github.com/dart-lang/language/issues/4728) <br>
- [SegmentFault error-messages topic](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tailored explanations, checklists, workflows, validation notes, templates, or implementation support depending on the user's request.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
