## Description: <br>
Helps agents rewrite or design clearer application error messages that explain what failed, why it failed, and what action the user should take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to turn vague or blocking error messages into actionable wording, workflows, checklists, or implementation guidance for troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may activate the skill for generic debugging, support wording, or unrelated work-productivity tasks. <br>
Mitigation: Prefer explicit invocation for error-message work and disable or ignore the skill when it appears in unrelated tasks. <br>
Risk: Improved wording or troubleshooting guidance can still be incorrect or misleading if the original error context is incomplete. <br>
Mitigation: Validate outputs against the user's stated constraints and list assumptions, limits, and remaining risks before use. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver) <br>
- [ASK HN: Why has technology become so unreliable?](https://news.ycombinator.com/item?id=49056900) <br>
- [GitHub issue: No reference paths found](https://github.com/vgteam/vg/issues/4974) <br>
- [GitHub issue: Frontend error taxonomy](https://github.com/Waffle-finance/waffle-finance-core/issues/320) <br>
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with prose, checklists, templates, code snippets, or verification notes as needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Text-only workflow; may produce reusable checklists or local-hardware-friendly implementation outlines.] <br>

## Skill Version(s): <br>
0.20260728.90410 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
