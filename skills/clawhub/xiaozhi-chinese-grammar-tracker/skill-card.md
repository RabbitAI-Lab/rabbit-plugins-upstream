## Description: <br>
Helps students identify and improve recurring Chinese grammar issues by tracking error patterns only after explicit consent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students and learning assistants use this skill to check Chinese writing, identify repeated grammar-error patterns, practice targeted corrections, and generate progress summaries when the student asks for them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can build a grammar-error history that may reveal learning patterns. <br>
Mitigation: Enable tracking only after explicit user consent and avoid storing or sharing the history when the user has not opted in. <br>
Risk: Sharing grammar-history summaries with related learning or reminder skills could expose more information than needed. <br>
Mitigation: Share only the minimum necessary fields with related skills and only when the user permits that specific use. <br>
Risk: Grammar correction guidance may be misleading if accepted without review. <br>
Mitigation: Use the skill's prompt-and-practice flow to help the student verify the correction instead of treating suggestions as final answers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/qizhitang) <br>
- [Grammar error library](references/grammar-error-library.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown and conversational text with structured correction prompts, practice exercises, reminders, and progress reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Consent-gated tracking of grammar-error history and minimal sharing with related learning skills when the user permits it.] <br>

## Skill Version(s): <br>
99999.0.2 (source: server release metadata; artifact frontmatter reports 2.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
