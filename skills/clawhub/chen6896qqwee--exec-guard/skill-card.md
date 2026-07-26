## Description: <br>
Intelligent command permission classifier — detect dangerous shell commands before execution. Distilled from Claude Code bashClassifier + yoloClassifier. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chen6896qqwee](https://clawhub.ai/user/chen6896qqwee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to evaluate shell commands before execution in AI-agent workflows, CI/CD checks, database operations, file-system operations, and network-command reviews. It returns allow, ask, or deny verdicts with risk details for command-safety review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional LLM classification can send full command text to a configured endpoint. <br>
Mitigation: Use `--llm` only with trusted endpoints and commands that are acceptable to disclose to that endpoint. <br>
Risk: The checker may allow destructive compound, obfuscated, or override-matched commands. <br>
Mitigation: Treat verdicts as advisory, keep human review for high-impact commands, and combine the skill with sandboxing, least privilege, and independent policy controls. <br>
Risk: Security evidence marks the release suspicious for use as a security guard. <br>
Mitigation: Do not rely on this release as the sole enforcement barrier for command execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page: Exec Guard](https://clawhub.ai/chen6896qqwee/skills/exec-guard) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [JSON or plain text command-risk verdicts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes command, verdict, risk level, matched rules, and reason; optional LLM classification can call a configured endpoint.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
