## Description: <br>
Creates a persistent trust profile for AI agents by monitoring behavior and risk to allow, require approval, or block actions accordingly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lola0786](https://clawhub.ai/user/lola0786) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security teams, and AI governance reviewers use this skill to define agent behavioral identity signals, evaluate runtime trust, and decide whether an action should be allowed, reviewed, or blocked. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill can involve sensitive operational context such as agent identity, permissions, behavior history, and approval records. <br>
Mitigation: Use it only in environments where tracking and audit trails are appropriate, and limit access to the resulting trust profiles and decision evidence. <br>
Risk: The artifact is guidance-only and does not itself collect telemetry or enforce allow/review/block decisions. <br>
Mitigation: Treat generated decisions and fingerprints as inputs to a reviewed control process before relying on them for enforcement. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lola0786/skills/agent-dna) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with decision summaries and inline CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe agent fingerprints, behavioral trust scores, risk scores, allow/review/block decisions, and explanations.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
