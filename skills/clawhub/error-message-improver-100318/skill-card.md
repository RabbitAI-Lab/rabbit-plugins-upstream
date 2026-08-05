## Description: <br>
Helps developers, support teams, SaaS operators, and users rewrite vague error messages so they explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, SaaS operators, and end users use this skill to turn vague application errors into clear messages with failure context, likely cause, and actionable next steps. It can produce templates, checklists, analysis, code-oriented guidance, and troubleshooting workflows for support or product-facing error communication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger keywords may cause the skill to appear for general debugging or support requests where error-message rewriting is not the intended task. <br>
Mitigation: Prefer explicit invocation when the user specifically wants clearer user-facing or support-facing error messages. <br>
Risk: Suggested error text can misstate a failure cause if the user provides incomplete logs, product context, or remediation constraints. <br>
Mitigation: State assumptions, keep uncertain causes qualified, and ask for missing details only when they materially affect the message or next step. <br>


## Reference(s): <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-100318) <br>
- [Developer Onboarding Funnel Metrics with Dropoff Analysis](https://github.com/sethdford/shipwright/issues/746) <br>
- [What I had to unlearn as a perfectionist before I could ship](https://news.ycombinator.com/item?id=48774284) <br>
- [Replace manual config validation with zod](https://github.com/SchneiderDaniel/cheasee-pi/issues/1208) <br>
- [You shouldn't copy-paste errors into Claude Code](https://news.ycombinator.com/item?id=48727244) <br>
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with optional code blocks, checklists, templates, and concise validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only workflow; no hidden execution, credential use, persistence, or destructive behavior found in server security evidence.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
