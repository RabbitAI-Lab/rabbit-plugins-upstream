## Description: <br>
This skill guides an agent to conduct role-specific mock interviews for job seekers, adapt question difficulty by experience level, score answers, suggest improvements, and produce a session scorecard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External job seekers use this skill for self-directed mock interview practice across engineering, product, business, and functional roles. It helps them answer one question at a time, receive scoring and improvement feedback, and review a final scorecard for targeted study. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill declares broad read, exec, and write authority for a mock interview workflow. <br>
Mitigation: Prefer a version that removes exec and write access, or require explicit user confirmation before any file operation or command execution. <br>
Risk: The artifact describes create, modify, delete, import, and export behavior without a clear scope for a mock interview skill. <br>
Mitigation: Limit any save, export, or import actions to user-requested interview notes or scorecards and review generated actions before execution. <br>
Risk: Interview scoring and advice may be incomplete or misleading for specialized roles or high-stakes hiring decisions. <br>
Mitigation: Treat the generated scorecard as practice feedback and supplement it with human review or domain-specific preparation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/interview-sim-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown and structured text with optional JSON-style summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces interview questions, per-question feedback, scores, ideal-answer guidance, and a final session scorecard.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
