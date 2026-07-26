## Description: <br>
Hf Minimal packages HeartFlow, a third-party cognitive agent framework for reasoning, memory, self-healing, decision support, code assistance, and agent-facing analysis tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add HeartFlow-style reasoning, memory, verification, planning, emotional analysis, and code-support workflows to an agent runtime. It is best suited for users who can review and deliberately enable its broader execution, storage, and network-facing capabilities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad experimental agent authority, including code execution and self-modification paths, can affect the host environment if enabled without review. <br>
Mitigation: Keep code execution and self-modification settings disabled by default, enable them only for intentional workflows, and run the skill in a constrained workspace. <br>
Risk: The skill can persist local memory and state, which may retain sensitive prompts, decisions, or generated content. <br>
Mitigation: Review configured memory and data directories before use, avoid storing secrets, and clear persisted state according to local retention requirements. <br>
Risk: Optional external calls and embedding-related settings may send queries or metadata outside the local environment when configured. <br>
Mitigation: Review API-key files, environment variables, and network-facing features before deployment; leave external integrations disabled unless required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/mark-heartflow-skill) <br>
- [npm package @yun520-1/heartflow](https://www.npmjs.com/package/@yun520-1/heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local memory or state when enabled; code execution and external calls should remain disabled unless intentionally configured.] <br>

## Skill Version(s): <br>
5.8.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
