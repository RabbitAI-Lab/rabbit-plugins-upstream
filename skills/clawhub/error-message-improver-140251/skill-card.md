## Description: <br>
Helps developers, support teams, SaaS operators, and users turn vague error messages into clearer guidance that explains what failed, why it failed, and what to do next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and users use this skill to rewrite or plan clearer error messages, troubleshooting workflows, checklists, analyses, code changes, and decision support artifacts. It is intended for productivity and support tasks where errors should make failure causes and next actions visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked too broadly because its activation wording covers general work-productivity, debugging, user feedback, and support requests. <br>
Mitigation: Prefer explicit invocation for rewriting or improving error messages, and tighten triggers before broad publishing if narrower activation is required. <br>
Risk: Generated error-message guidance can still be incomplete, misleading, or mismatched to the product context. <br>
Mitigation: Review proposed messages and workflows against the actual failure mode, user audience, and available remediation path before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-140251) <br>
- [Better, less technical user-facing error messages](https://github.com/edrlab/thorium-reader/issues/3696) <br>
- [Renovate configuration validation issue](https://github.com/midnghtsapphire/revvel-standards/issues/15809) <br>
- [Miden protocol asset composition issue](https://github.com/0xMiden/protocol/issues/3168) <br>
- [Scafctl resolver/provider/CLI gaps issue](https://github.com/oakwood-commons/scafctl/issues/611) <br>
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages) <br>
- [Hacker News search result](https://news.ycombinator.com/item?id=48862125) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with prose, checklists, templates, analysis, and inline code or configuration when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, limits, validation notes, and remaining risks when helpful.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
