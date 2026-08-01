## Description: <br>
Double-blind comparison of AI model responses -- query models in parallel, judge anonymized outputs, rank on merit. Trigger with "mdls" or "modelshow". <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[schbz](https://clawhub.ai/user/schbz) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers, evaluators, and external OpenClaw users use ModelShow to compare several configured model responses to the same prompt through blind judging, ranked scores, and judge commentary. It is suited for fact checks, creative comparisons, technical decision support, code review, and brainstorming where side-by-side model behavior is useful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, model responses, judge analysis, and metadata may be sent to multiple configured model providers and persisted on disk. <br>
Mitigation: Use ModelShow only where provider policies and the configured output directory are acceptable; avoid secrets, private credentials, regulated personal data, and proprietary text unless explicitly approved. <br>


## Reference(s): <br>
- [ModelShow homepage](https://github.com/schbz/modelshow) <br>
- [ModelShow ClawHub listing](https://clawhub.ai/schbz/skills/modelshow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown result summaries with scored rankings and judge commentary, plus saved JSON and Markdown result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Each run can include full model responses, judge analysis, ranking metadata, and an anonymization key in local saved results.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter, skill.json, release metadata, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
