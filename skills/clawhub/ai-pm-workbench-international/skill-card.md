## Description: <br>
AI PM Super Workbench - International Edition is a full-stack intelligent workbench for AI Product Managers worldwide. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[yinjianheng](https://clawhub.ai/user/yinjianheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI product managers, product leaders, founders, and technical teams use this skill to structure AI product strategy, model selection, RAG and agent design, evaluation, safety, pricing, and compliance deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation language may cause the skill to steer many AI product-management, RAG, agent, evaluation, pricing, and compliance requests. <br>
Mitigation: Constrain activation to AI product-management work and ask the base agent to prefer narrower domain skills when the user request is outside that scope. <br>
Risk: Some templates ask for reasoning or Chain-of-Thought style fields that could encourage disclosure of internal reasoning. <br>
Mitigation: Revise production templates to request concise user-facing rationales and summaries rather than hidden internal reasoning. <br>
Risk: The skill provides business, compliance, pricing, safety, and technical planning guidance that may become outdated or may not fit a regulated deployment. <br>
Mitigation: Require human review by product, engineering, security, and legal stakeholders before using generated plans for production decisions. <br>
Risk: The skill appends a long author and legal disclaimer that may be unsuitable for concise product workflows. <br>
Mitigation: Set response policies that preserve required attribution only where appropriate and avoid injecting unrelated disclaimer text into final deliverables. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yinjianheng/skills/ai-pm-workbench-international) <br>
- [README](README.md) <br>
- [AI Industry Trends 2026](references/ai-industry-trends-2026.md) <br>
- [AI PM Deep Methods](references/methodologies/ai-pm-deep-methods.md) <br>
- [AI Product Requirements Document Template](references/templates/ai-prd-template.md) <br>
- [Agent System Design Document Template](references/templates/agent-design-template.md) <br>
- [RAG Design Template](references/templates/rag-design-template.md) <br>
- [AI Evaluation Template](references/templates/ai-evaluation-template.md) <br>
- [AI Safety Template](references/templates/ai-safety-template.md) <br>
- [AI Product Pricing Plan Template](references/templates/ai-pricing-template.md) <br>
- [AI Customer Service Example](references/examples/ai-customer-service-example.md) <br>
- [AI Customer Service Agent Case Library](examples/ai-customer-service-agent-case.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown documents, structured templates, product guidance, and occasional diagrams or configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No artifact-backed tool execution; responses may include long disclaimers and should be reviewed for current business, legal, and technical accuracy.] <br>

## Skill Version(s): <br>
1.2.0-intl (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
