## Description: <br>
Helps developers, support teams, and SaaS operators turn vague application errors into clear messages that explain what failed, why it failed, and what action to take next. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Application developers, support teams, SaaS operators, and affected users use this skill to improve troubleshooting copy and support workflows when unclear errors slow diagnosis. It helps produce tailored error-message rewrites, reusable checklists, workflow guidance, analysis, code-oriented suggestions, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may activate the skill during general debugging or support conversations where error-message improvement is not the user's main goal. <br>
Mitigation: Prefer explicit invocation when error-message help is desired, and confirm the user's intended outcome before producing detailed rewrites or workflow changes. <br>
Risk: Generated troubleshooting copy could misstate a system cause when the available error context is incomplete. <br>
Mitigation: Ask only for missing facts that materially change the result, state assumptions clearly, and include a verification note for the proposed message or workflow. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [[SDK] Migrate stop-loss.ts input validation to zod schemas](https://github.com/CoralSwap-Finance/coralswap-sdk/issues/489) <br>
- [[idea] Enhance Error Handling](https://github.com/samoletovs/rosette/issues/74) <br>
- [error-messages](https://segmentfault.com/t/error-messages) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with optional inline code or checklist sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and next steps when useful.] <br>

## Skill Version(s): <br>
0.20260802.40421 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
