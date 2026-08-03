## Description: <br>
LYGO Ops Detector analyzes text, logs, and association descriptions with deterministic local heuristics to surface evasion, association, and institutional-signaling patterns, with evaluation artifacts for reproducible precision, recall, and AUC reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to run local, action-focused heuristic checks on statements, logs, threads, emails, or association descriptions. The skill produces score breakdowns and verdict language that should support, not replace, independent human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The detector can be used for sensitive reputation or association analysis. <br>
Mitigation: Use it only with clear authority over the input data, avoid private communications or association data without consent, and keep findings action-focused rather than identity-focused. <br>
Risk: Heuristic scores and bundled calibration artifacts may be misleading if treated as proof. <br>
Mitigation: Treat outputs as investigative leads, require independent human review, and verify claims against primary sources before taking action. <br>
Risk: Detector output could be misused for public accusations, doxing, or escalation. <br>
Mitigation: Do not publish or escalate reports without explicit consent, raw supporting signals, and human review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-ops-detector) <br>
- [Publisher profile](https://clawhub.ai/user/deepseekoracle) <br>
- [AETHON D9 Blueprint](references/AETHON_D9_BLUEPRINT.md) <br>
- [Security and ethics notes](references/SECURITY.md) <br>
- [Public labeled discourse suite](tests/labeled_discourse_suite.json) <br>
- [Last evaluation report](tests/last_eval_report.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown-style analysis with score breakdowns; optional JSON from the CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes evasion index, association index, combined risk, verdict, and an action-focused disclaimer.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
