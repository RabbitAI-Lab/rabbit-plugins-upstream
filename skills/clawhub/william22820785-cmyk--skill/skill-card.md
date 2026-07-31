## Description: <br>
算命老师傅 provides a Chinese-language fortune-telling consultation persona for long-term life readings and concrete event readings, using structured input collection, hidden calculation steps, validation scripts, and concise conversational responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External users use this skill for Chinese-language divination-style consultations about personal life themes, relationships, work, finances, timing, and specific decisions. Developers and reviewers can also use the bundled schemas and validators to understand the expected consultation flow and output constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may collect sensitive birth details and contextual life information during consultations. <br>
Mitigation: Use only with information users are comfortable sharing, and avoid entering data that should not be retained in local intermediate files. <br>
Risk: The skill can provide confident divination-style guidance about health, legal, financial, relationship, or safety-adjacent topics. <br>
Mitigation: Treat outputs as cultural or entertainment interpretation, not professional medical, legal, financial, or safety advice. <br>
Risk: Implicit invocation can start the persona when trigger terms appear. <br>
Mitigation: Review activation behavior before deployment and ensure users understand when the divination persona is active. <br>
Risk: The skill intentionally hides internal reasoning and calculation details from end users. <br>
Mitigation: Rely on reviewer inspection of source files, schemas, and validators rather than expecting user-visible reasoning to expose how conclusions were produced. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/william22820785-cmyk/skills/skill) <br>
- [Master identity](references/master-identity.md) <br>
- [Consultation method](references/consultation-method.md) <br>
- [Interpretation method](references/interpretation-method.md) <br>
- [Consultation plan schema](references/consultation-plan-schema.md) <br>
- [Liuyao method](references/liuyao-method.md) <br>
- [Liuyao plan schema](references/liuyao-plan-schema.md) <br>
- [Ling et al., CSCW 2026: GenAI fortune-telling trust, feedback, and process](https://arxiv.org/abs/2603.27784) <br>
- [APA Dictionary: Barnum effect](https://dictionary.apa.org/barnum-effect) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown conversation text with occasional Markdown tables, JSON schemas, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to hide internal reasoning while preserving concise judgments, timing windows, conditions, and safety boundaries.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
