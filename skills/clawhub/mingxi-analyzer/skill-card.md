## Description: <br>
Mingxi Analyzer provides a Chinese-language structured analysis framework for system diagnosis, contradiction analysis, game-scenario reasoning, content quality evaluation, knowledge management, and cross-checking with confidence labels and review plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[122201](https://clawhub.ai/user/122201) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to apply repeatable analysis disciplines to policy analysis, market research, strategic planning, content review, organizational diagnosis, and complex problem decomposition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may trigger on common Chinese words such as analysis or evaluation. <br>
Mitigation: Use it when a structured analysis workflow is intended, and rely on TCR classification to bypass the framework for simple facts, ordinary tasks, and casual conversation. <br>
Risk: The optional judgment tracker stores local analysis history under ~/.openclaw/judgment_tracker.db. <br>
Mitigation: Review or avoid the tracker script when persistent local records are not desired. <br>
Risk: Framework-driven analysis can produce overconfident conclusions if source quality and failure conditions are skipped. <br>
Mitigation: Preserve the skill's confidence labels, invalidation conditions, review dates, and safety-gate checks for deep-analysis outputs. <br>


## Reference(s): <br>
- [TCR Task Classification Route](references/00-tcr.md) <br>
- [Core Principles](references/00-core-principles.md) <br>
- [OCGS Six-Dimensional System Diagnosis](references/01-ocgs.md) <br>
- [Five-Layer Reasoning Method](references/02-five-layer.md) <br>
- [Contradiction Analysis Method](references/03-contradiction.md) <br>
- [Policy Signal Interpretation](references/04-policy-signal.md) <br>
- [Six-Prism Content Evaluation](references/05-six-prism.md) <br>
- [T1-T4 Credibility Levels](references/06-credibility.md) <br>
- [Safety Gates](references/07-safety-gates.md) <br>
- [Judgment Tracker](references/08-judgment-tracker.md) <br>
- [Review Template](references/09-review-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown analysis guidance and command-line helper output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Deep-analysis outputs may include confidence labels, invalidation conditions, review dates, and optional local judgment-tracker records.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
