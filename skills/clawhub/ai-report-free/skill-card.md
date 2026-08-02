## Description: <br>
AI Report Free helps agents structure financial statement analysis with F-score summaries, risk warnings, input validation guidance, and JSON or Markdown report examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide financial report analysis, summarize F-score-style signals, identify warning indicators, and produce structured outputs for human review. It is best suited for assisted analysis workflows where financial decisions remain subject to professional validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad command-execution authority. <br>
Mitigation: Run it only in a sandboxed agent environment or one that requires explicit confirmation before command execution. <br>
Risk: The skill discusses external financial APIs without enough scoping or disclosure. <br>
Mitigation: Confirm data-flow, API destination, and privacy controls before sending proprietary financial reports, credentials, or sensitive business data. <br>
Risk: Financial summaries and warning signals may influence investment, credit, or business decisions. <br>
Mitigation: Treat outputs as decision-support material and require human financial review before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/ai-report-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, Python snippets, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may reference external financial data APIs and should be reviewed before use in investment, credit, or operational decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
