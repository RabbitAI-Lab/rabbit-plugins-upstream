## Description: <br>
Compiles prompts or multi-source content such as PDFs, videos, URLs, images, and documents into reusable AI skill packages with evidence grading, honest boundaries, and modular architecture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to convert reusable prompts or multi-source materials into maintainable agent skill packages. It supports skill design, file generation, evidence grading, honest boundary setting, and validation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated skills may include incorrect boundaries, unsupported claims, or misleading guidance if source evidence is weak. <br>
Mitigation: Review generated skills, evidence grades, and validation results before installing or deploying them. <br>
Risk: The skill can guide agents to parse files, URLs, repositories, and media that may contain sensitive or untrusted content. <br>
Mitigation: Use it only with sources the user is comfortable having the agent parse, and scan generated skill packages before release. <br>
Risk: Non-Chinese video or multilingual inputs may need different transcription language handling. <br>
Mitigation: Adjust the transcription language setting or request automatic language detection for multilingual media inputs. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/qomob/SkillCompiler) <br>
- [ClawHub Skill Compiler page](https://clawhub.ai/qomob/skills/skillcompiler) <br>
- [Evidence grading reference](references/evidence-grading.md) <br>
- [Honest boundaries reference](references/honest-boundaries.md) <br>
- [Ingestion pass reference](references/pass-ingestion.md) <br>
- [Validation pass reference](references/pass-6-validate.md) <br>
- [Skill IR schema](schemas/ir-schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown skill package with generated files, schemas, and validation report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include evidence grades, honest boundaries, validation results, and platform-specific profiles.] <br>

## Skill Version(s): <br>
1.2.2 (source: ClawHub release metadata; artifact frontmatter says 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
