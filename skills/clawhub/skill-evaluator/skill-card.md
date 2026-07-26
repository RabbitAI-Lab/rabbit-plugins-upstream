## Description: <br>
Evaluates Clawdbot skills for quality, reliability, and publish-readiness using automated structural checks plus a 25-criteria rubric. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terwox](https://clawhub.ai/user/terwox) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and maintainers use this skill to review, audit, score, and prepare Clawdbot skills for publication. It combines automated checks for structure, metadata, scripts, and basic security with a manual rubric for deeper quality assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The evaluator inspects local skill folders, so running it on unintended folders may expose or summarize files outside the intended review scope. <br>
Mitigation: Run it only against skill folders you intend to inspect and review generated findings before publishing. <br>
Risk: Generated EVAL.md content may include incomplete or incorrect judgments from automated checks or manual scoring. <br>
Mitigation: Review the completed evaluation against the rubric before relying on it for release decisions. <br>
Risk: Optional pip or npx tools referenced by the skill are third-party dependencies. <br>
Mitigation: Install and run optional dependencies only in a trusted environment. <br>


## Reference(s): <br>
- [Skill Evaluation Rubric](references/rubric.md) <br>
- [Evaluation Template](assets/EVAL-TEMPLATE.md) <br>
- [SkillLens](https://www.npmjs.com/package/skilllens) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with optional plain-text or JSON evaluation reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Automated checks cover structure, scripts, trigger metadata, and basic security; full scoring requires manual rubric review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
