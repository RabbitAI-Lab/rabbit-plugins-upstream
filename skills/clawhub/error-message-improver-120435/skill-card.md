## Description: <br>
Helps developers, support teams, SaaS operators, and users improve vague error messages so they explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and end users use this skill to turn unclear failures into actionable user-facing messages, troubleshooting checklists, workflows, templates, analysis, code changes, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may invoke the skill for general debugging or support requests where error-message improvement is not the user's intent. <br>
Mitigation: Prefer explicit invocation for user-facing error-message work, or narrow trigger text and disable implicit invocation where precise routing is required. <br>
Risk: Generated guidance can be less useful when the original failure context is incomplete or ambiguous. <br>
Mitigation: State assumptions, ask only for missing information that materially changes the output, and validate the result against the stated success criteria. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-120435) <br>
- [Improve: UI/UX Improvements for Login Page](https://github.com/ronisarkarexe/story-spark-ai/issues/3000) <br>
- [Error message improvements](https://github.com/jump-dev/JuMP.jl/issues/4175) <br>
- [Proposal: Transaction Builder API](https://github.com/graz-sh/graz/issues/267) <br>
- [Investigate LinkedIn OAuth connection verification failure](https://github.com/V-Rubio/Portfolio/issues/106) <br>
- [SegmentFault error-messages](https://segmentfault.com/t/error-messages) <br>
- [Typst 0.15.0 Hacker News discussion](https://news.ycombinator.com/item?id=48545698) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text, with code, shell command, checklist, or configuration blocks when the requested artifact calls for them.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and follow-up work.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
