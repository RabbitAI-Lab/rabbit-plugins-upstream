## Description: <br>
Extracts writing style patterns from exemplar text into a reusable profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and writing-focused agents use this skill to analyze exemplar text, extract quantitative style features, select representative passages, and produce a reusable style profile for later generation or editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad writing-style requests. <br>
Mitigation: Confirm that the current task is intended to analyze or apply a style profile before collecting exemplars or generating profile content. <br>
Risk: Generated profiles may retain representative excerpts from exemplar text. <br>
Mitigation: Use only exemplar text that is appropriate to analyze and retain, and review generated profiles before sharing or storing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-style-learner) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, shell commands] <br>
**Output Format:** [Markdown and YAML-style style profiles with metrics, exemplars, validation checklists, and optional shell command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Profiles may include representative excerpts from user-provided exemplars.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
