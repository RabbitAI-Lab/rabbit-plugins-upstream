## Description: <br>
审稿共享引擎。提供所有审稿 skill 通用的分段标注框架、整体审稿框架、审稿核心原则、事实核查分类、审稿自查清单。不单独运行，由其他审稿 skill 引用其 references/ 目录下的文档。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and review-skill authors use this shared package to reuse common review frameworks, checklists, fact-check categories, and optional JSON validation helpers across review-focused agent skills. It is not intended to run independently. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package is shared review infrastructure and may produce incomplete results if treated as a standalone reviewer. <br>
Mitigation: Use it through downstream review skills or workflows that cite the relevant reference documents and define the review task. <br>
Risk: The optional validation scripts process local checklist JSON and may print findings or checklist metadata to the terminal. <br>
Mitigation: Review the scripts before operational use and run them only on intended checklist files in an appropriate local environment. <br>
Risk: Suggested-item warnings are advisory and may be misread as mandatory blockers. <br>
Mitigation: Decide in the consuming workflow whether suggested checks are informational or enforced before using script output for release decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mayf3/skills/review-common-core) <br>
- [Review principles](artifact/references/review-principles.md) <br>
- [Segment annotation framework](artifact/references/segment-annotation-framework.md) <br>
- [Holistic review framework](artifact/references/holistic-review-framework.md) <br>
- [Sensitivity checklist](artifact/references/sensitivity-checklist.md) <br>
- [Fact-check framework](artifact/references/fact-check-framework.md) <br>
- [Dual-host dialogue guide](artifact/references/dual-host-dialogue-guide.md) <br>
- [Review checker](artifact/references/review-checker.md) <br>
- [Theme consistency checklist](artifact/references/theme-consistency-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown guidance with optional JSON checklist outputs and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Shared reference package; optional local scripts validate intended checklist JSON files and emit pass, fail, or warning text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
