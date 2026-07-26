## Description: <br>
LYGO Ops Detector analyzes text, described actions, and association patterns with deterministic heuristics to surface evasion, coordination, and institutional-signaling indicators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents, analysts, and developers use this skill to evaluate supplied statements, logs, or behavior descriptions for measurable evasion and coordination signals. Its output is advisory and should support human review, not identity-based judgments or public accusations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Detector scores can be mistaken for proof of wrongdoing or identity-based conclusions. <br>
Mitigation: Use scores only as advisory pattern signals, review the cited evidence manually, and avoid public accusations, employment decisions, legal claims, or identity-based judgments without independent evidence and human review. <br>
Risk: Sensitive or untrusted text may contain misleading, poisoned, or incomplete context. <br>
Mitigation: Run analysis locally, verify primary sources, separate observed signals from inference, and quarantine suspicious inputs before relying on results. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/deepseekoracle/skills/lygo-ops-detector) <br>
- [AETHON D9 Blueprint](references/AETHON_D9_BLUEPRINT.md) <br>
- [Security and Ethics](references/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown analysis with optional JSON or CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes score breakdowns, observed signals, verdicts, and action-focused disclaimers.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
