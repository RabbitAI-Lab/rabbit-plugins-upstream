## Description: <br>
Wenchang Review diagnoses or edits content drafts and recommends whether to publish, lightly edit, fully edit, rewrite, switch platforms, or stop investing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and content teams use this skill to assess whether a draft is worth publishing and identify the smallest useful next action. When explicitly requested, it can also produce an edited draft while preserving the author's core position. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Draft recommendations can be wrong when the input contains unsupported claims or weak evidence. <br>
Mitigation: Review the recommendation before publishing and verify evidence near important claims. <br>
Risk: Full-edit mode may alter emphasis or wording in a way the author does not intend. <br>
Mitigation: Compare edited drafts against the original core position and confirm substantive changes before use. <br>


## Reference(s): <br>
- [Wenchang Review on ClawHub](https://clawhub.ai/yangchao228/skills/wenchang-review) <br>
- [Project homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/wenchang-review) <br>
- [Minimal Input Example](examples/minimal-input.md) <br>
- [Expected Output Notes](examples/expected-output-notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown with optional YAML content_state block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Diagnosis mode is the default; full edited drafts are returned only when explicitly requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
