## Description: <br>
Helps developers, support teams, SaaS operators, and users rewrite vague errors into clear messages that explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and affected users use this skill to turn vague troubleshooting failures into actionable error messages, checklists, workflows, or implementation guidance. It is intended for work-productivity, debugging, user feedback, support, and troubleshooting requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger language may activate the skill for general support or troubleshooting requests where a narrower skill would be preferred. <br>
Mitigation: Use explicit invocation or narrower routing when precise skill selection matters. <br>
Risk: Generated error-message guidance may be incomplete if the user omits the failing system, audience, constraints, or reproduction context. <br>
Mitigation: Restate assumptions, ask only material clarification questions, and validate the final message against what failed, why it failed, and the next action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver-234346) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [GitHub issue: 42 Project Badge action request](https://github.com/midnghtsapphire/revvel-standards/issues/16198) <br>
- [GitHub issue: HTML5 Validator action request](https://github.com/midnghtsapphire/revvel-standards/issues/16182) <br>
- [GitHub issue: unawaited should support FutureOr](https://github.com/dart-lang/sdk/issues/63818) <br>
- [SegmentFault: HarmonyOS developer community](https://segmentfault.com/brand/harmonyos-next) <br>
- [SegmentFault: JavaScript tag](https://segmentfault.com/t/javascript) <br>
- [SegmentFault: TypeScript tag](https://segmentfault.com/t/typescript) <br>
- [SegmentFault: C++ singleton compile answer](https://segmentfault.com/q/1010000004886164/a-1020000004886445) <br>
- [SegmentFault: error-messages tag](https://segmentfault.com/t/error-messages) <br>
- [SegmentFault: Vue custom directive error question](https://segmentfault.com/q/1010000009322969) <br>
- [Hacker News: Ghostel.el discussion](https://news.ycombinator.com/item?id=48905348) <br>
- [Hacker News: A road to Lisp discussion](https://news.ycombinator.com/item?id=48862125) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, with code blocks when implementation support is requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a reusable checklist, workflow, assumptions, validation note, and next-step guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
