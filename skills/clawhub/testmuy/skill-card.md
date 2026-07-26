## Description: <br>
Captures learnings, errors, corrections, and feature requests in local Markdown logs so OpenClaw agents can improve future work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nightsquirrl](https://clawhub.ai/user/nightsquirrl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill in trusted OpenClaw workspaces to record corrections, command failures, feature requests, and reusable workflow improvements in local learning files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local learning logs may retain sensitive workspace context. <br>
Mitigation: Use the skill only in trusted workspaces, avoid logging secrets or full transcripts, and keep .learnings out of version control unless sharing is intentional. <br>
Risk: The optional OpenClaw hook can append transcript-derived error excerpts for later triage. <br>
Mitigation: Enable the hook only where transcript-derived capture is acceptable, and review auto-swept errors before relying on them. <br>


## Reference(s): <br>
- [OpenClaw Integration](references/openclaw-integration.md) <br>
- [Entry Examples](references/examples.md) <br>
- [Uninstall Guide](references/uninstall.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local Markdown log templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local learning, error, and feature-request entries; optional hook excerpts are truncated and redacted before being appended.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
