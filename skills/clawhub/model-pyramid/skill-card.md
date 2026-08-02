## Description: <br>
Right-size MODEL + EFFORT for the session and for each subagent at fan-out time, and decide whether to attach an advisor. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to choose model, effort, and advisor settings for sessions and subagents before delegation or fan-out. It provides advisory sizing guidance and a local checker for deterministic plan issues; it does not spawn agents or change runtime configuration by itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recommendations may increase token use, tool calls, or runtime cost when higher effort, advisors, or larger max_tokens are selected. <br>
Mitigation: Treat the output as advisory, review each proposed setting before applying it, and use the checker script for deterministic configuration issues. <br>
Risk: Advisor use can expose the full conversation to the advisor model, and manually applied runtime settings may persist across sessions. <br>
Mitigation: Use advisors only when the conversation context is appropriate to share, and confirm model and effort settings before long or cached work. <br>
Risk: Model rosters, effort support, and numeric defaults are dated to the 2026-07-29 baseline. <br>
Mitigation: Re-verify current model documentation and re-run local evaluations after model family or runtime changes. <br>


## Reference(s): <br>
- [model-and-effort](artifact/references/model-and-effort.md) <br>
- [orchestration](artifact/references/orchestration.md) <br>
- [runtime-knobs](artifact/references/runtime-knobs.md) <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/model-pyramid) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with concise report lines and optional JSON input for the checker script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output only; the included checker validates deterministic plan constraints but does not judge whether a sizing decision is wise.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, frontmatter metadata, and CHANGELOG, released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
