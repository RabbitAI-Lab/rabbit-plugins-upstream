## Description: <br>
Provides source-grounded lookup and response guidance for Hu Xishu's Jingfang clinical system, including six-channel diagnosis, formula differentiation, diet and recovery models, dosage frameworks, and searchable lecture references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jangviktor-web](https://clawhub.ai/user/jangviktor-web) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, practitioners, researchers, and agent developers use this skill to navigate Hu Xishu's TCM lecture material and produce source-grounded answers about six-channel diagnosis, formula comparison, dosage reasoning, diet, recovery, and related reference passages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat diagnosis, formula, or herb dosage output as personal medical advice. <br>
Mitigation: Frame the skill as historical or educational TCM reference material and require qualified clinician supervision for diagnosis, formulas, herbs, and dosing. <br>
Risk: General users may rely on the skill for self-diagnosis or self-treatment. <br>
Mitigation: Add explicit medical boundaries, warnings against self-administering herbs from agent output, and escalation guidance for emergencies or red-flag symptoms. <br>
Risk: The artifact includes actionable dosage frameworks without clear safety boundaries. <br>
Mitigation: Keep dosage responses tied to source context, avoid personalized dosing instructions, and direct users to licensed medical professionals for any treatment decision. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jangviktor-web/skills/huxishu) <br>
- [Skill index](artifact/SKILL.md) <br>
- [Shanghan lecture module](artifact/modules/01_shanghan.md) <br>
- [Jingui lecture module](artifact/modules/02_jingui.md) <br>
- [Core philosophy reference](artifact/references/01-core-philosophy.md) <br>
- [Decision heuristics reference](artifact/references/02-decision-heuristics.md) <br>
- [Expression style reference](artifact/references/03-expression-dna.md) <br>
- [Antipatterns and boundaries reference](artifact/references/04-antipatterns-boundaries.md) <br>
- [Biography and legacy reference](artifact/references/05-biography-legacy.md) <br>
- [Diet and wellness reference](artifact/references/06-diet-wellness.md) <br>
- [Dosage framework reference](artifact/references/07-dosage-framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text responses with source-grounded references to the bundled skill material] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code or tool calls are bundled; output should stay within the available source texts and medical safety boundaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
