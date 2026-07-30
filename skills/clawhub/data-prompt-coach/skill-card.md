## Description: <br>
Data Prompt Coach guides data-analysis prompt creation, scenario-aware interviews, template generation, visualization guidance, and tutorial-method distillation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Data analysts, developers, and business users use this skill to turn data-analysis needs into structured prompts and supporting templates for web collection, document extraction, SQL generation, reconciliation, labeling, weekly reporting, and deep-dive reports. Advanced users can also distill tutorials into reusable methodology files after reviewing the resulting diffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit its own method library, routing files, index, audit files, and test prompts during tutorial distillation. <br>
Mitigation: Review diffs after every distillation run before accepting the changes. <br>
Risk: Tutorial inputs can influence future dispatch and methodology behavior if low-quality or adversarial content is mounted. <br>
Mitigation: Use trusted source material, keep the five-method mount limit, and leave questionable candidates unmounted for later review. <br>
Risk: The skill may process sensitive samples such as resumes, contracts, invoices, tables, PDFs, or DDL. <br>
Mitigation: Redact unnecessary personal, financial, contractual, or proprietary data before uploading samples. <br>
Risk: Generated automation artifacts such as BAT scripts, caches, or clear-and-rewrite sync workflows could cause unintended local changes if run unreviewed. <br>
Mitigation: Manually review generated scripts and sync workflows before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/data-prompt-coach) <br>
- [Project homepage](https://github.com/EdwardWason/data-prompt-coach) <br>
- [Scenario router](references/routing/scenario-router.md) <br>
- [Interview flow](references/routing/interview-flow.md) <br>
- [Method composition](references/routing/method-composition.md) <br>
- [Distillation router](references/routing/distillation-router.md) <br>
- [Examples](references/examples.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prompts with optional code blocks and generated template files such as JSON, SQL, Python, CSV, and BAT.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update files when the user requests templates or uses tutorial distillation; distillation mounts at most five methods per run.] <br>

## Skill Version(s): <br>
3.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
