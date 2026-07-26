## Description: <br>
Compresses older OpenClaw agent session history into a bounded, lane-change-aware context capsule that keeps recent messages verbatim, flags abandoned directions, quarantines injected instructions, and redacts secrets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parad0x-labs](https://clawhub.ai/user/parad0x-labs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this ContextEngine plugin to reduce token load in long agent sessions by replacing older transcript history with a bounded extractive capsule while keeping recent messages verbatim. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Older history is summarized into a compact capsule, so exact wording, nuance, and low-priority details can be lost. <br>
Mitigation: Use it for long sessions where bounded context is acceptable; keep normal history or another transcript source when exact wording must be preserved. <br>
Risk: The plugin reads and transforms OpenClaw conversation history, and its secret redaction is best-effort. <br>
Mitigation: Do not use it as the only protection for highly sensitive workflows, and avoid placing secrets or regulated data in chat history. <br>
Risk: Summarized older history may be placed into the model's system context. <br>
Mitigation: Review whether the plugin's context-injection behavior matches the deployment's privacy and instruction-hierarchy requirements before enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/parad0x-labs/skills/context-capsule) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/parad0x-labs) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Bounded extractive context capsule text with configuration options] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Keeps recent messages verbatim by default and caps the injected capsule with maxCapsuleTokens and capsuleTokenRatio.] <br>

## Skill Version(s): <br>
1.6.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
