## Description: <br>
HeartFlow is a local cognitive preprocessor that produces structured cognition data for downstream models, including state awareness, self-cognition, judgment, memory search, emotion analysis, and reasoning checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mark-heartflow](https://clawhub.ai/user/mark-heartflow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use HeartFlow to run a local Node.js cognitive preprocessing and MCP tool layer that structures user input, analyzes memory, emotion, psychology, and reasoning signals, and returns data or guidance for downstream model responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory may save prompts or derived memories by default. <br>
Mitigation: Review memory configuration before use and avoid processing sensitive prompts unless local storage behavior is acceptable. <br>
Risk: Daemon behavior is documented inconsistently and may run in the background with selected API-key environment variables. <br>
Mitigation: Do not start the daemon unless the operator has reviewed its configuration, environment access, and runtime scope. <br>
Risk: High-impact optional capabilities and inconsistent documentation warrant caution even without artifact-backed exfiltration, destructive install behavior, or hidden C2. <br>
Mitigation: Review the release before installation, keep optional capabilities disabled unless explicitly needed, and monitor local execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mark-heartflow/skills/heartflow) <br>
- [npm package @yun520-1/heartflow](https://www.npmjs.com/package/@yun520-1/heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, structured text, JSON-like data, and CLI or MCP responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local execution can persist prompts or derived memories depending on configuration; optional daemon behavior should be reviewed before use.] <br>

## Skill Version(s): <br>
6.0.7 (source: ClawHub release evidence; artifact package and SKILL.md report 6.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
