## Description: <br>
Helps developers, support teams, SaaS operators, and users improve vague error messages so they explain what failed, why it likely failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and end users use this skill to rewrite, evaluate, or plan clearer troubleshooting guidance for error messages. It supports practical outputs such as improved message copy, checklists, workflows, analysis, code changes, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may select the skill for general debugging or support requests outside focused error-message work. <br>
Mitigation: Use it when the requested outcome is to rewrite, design, or evaluate error messages or troubleshooting guidance; otherwise confirm the intended scope first. <br>
Risk: Improved error text can still be misleading if the underlying failure cause is unknown or the available diagnostic context is incomplete. <br>
Mitigation: State assumptions, distinguish confirmed facts from likely causes, and include a verification step or next diagnostic action in the output. <br>
Risk: Suggested code or logging changes may alter user-facing behavior or suppress useful diagnostics. <br>
Mitigation: Review changes against support and observability needs, then test both expected failures and edge cases before release. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver) <br>
- [Improve error messages for Trusted Publishing](https://github.com/pypa/twine/issues/1355) <br>
- [Nushell confusing conversion error issue](https://github.com/nushell/nushell/issues/18749) <br>
- [SegmentFault error-messages topic](https://segmentfault.com/t/error-messages) <br>
- [Hacker News discussion signal](https://news.ycombinator.com/item?id=49045494) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown or plain text with optional code snippets, checklists, and implementation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include rewritten error copy, troubleshooting checklists, validation notes, or small local scripts when requested.] <br>

## Skill Version(s): <br>
0.20260730.3907 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
