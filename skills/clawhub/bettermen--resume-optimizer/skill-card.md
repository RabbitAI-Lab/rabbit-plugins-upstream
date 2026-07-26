## Description: <br>
简历优化两步走编排器：第一步调用 resume-assistant 按 JD 重组内容并量化成果，第二步调用 humanizer 去除 AI 写作痕迹，产出既专业又像本人写的简历。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers, career changers, and students use this skill to turn resume material and an optional job description into a structured, quantified, less AI-sounding resume draft. It coordinates resume-assistant for structure and metrics, then humanizer for natural final wording. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume and job-description content may contain personal or sensitive career information shared with the agent workflow and its two named sub-skills. <br>
Mitigation: Use the skill only when comfortable sharing that content with the workflow, and avoid adding unnecessary sensitive details. <br>
Risk: Final resumes may retain placeholders or contain incorrect numbers, project facts, technologies, or contact details. <br>
Mitigation: Review the final resume carefully before sending it, especially all placeholders, metrics, project facts, and contact information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/resume-optimizer) <br>
- [场景 #18 · 简历优化 — 两步走消除 AI 味](references/scene-18-overview.md) <br>
- [Before/After 写法对比](references/before-after-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, text] <br>
**Output Format:** [Markdown resume draft with a placeholder checklist and follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Coordinates two named sub-skills and preserves user-provided facts, numbers, and placeholders.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
