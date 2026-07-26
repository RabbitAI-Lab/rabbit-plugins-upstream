## Description: <br>
Polish body text before publishing, in Polish or English, by fixing hanging single-letter conjunctions and prepositions, adding orphan guards, flagging widow risks, and handling ragged-edge risks without rewriting copy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monikazapisekstudio](https://clawhub.ai/user/monikazapisekstudio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, designers, and developers use this skill before publishing long-form Markdown, HTML, or plain text to apply microtypography fixes without changing the copy's wording. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Invisible typography characters such as NBSPs, soft hyphens, smart quotes, and dash substitutions may matter in code-like snippets, URLs, or HTML attributes. <br>
Mitigation: Review the returned text before publishing and avoid applying the skill to code, tables, short UI strings, URLs, and markup attributes unless the user explicitly confirms the target. <br>
Risk: Widow, ragged-edge, and hanging-punctuation outcomes depend on the final rendered layout. <br>
Mitigation: Treat layout-dependent items as review flags or CSS/design-tool suggestions and verify them after the content is rendered. <br>
Risk: English strict single-letter handling and dash style can vary by house style. <br>
Mitigation: Ask for or confirm the intended English typography mode when the input does not already show a consistent style. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/monikazapisekstudio/skills/microtypography) <br>
- [Server-resolved GitHub source](https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/skills/typesetting-engine-skillset/microtypography) <br>
- [Design Engineering Playbook](https://github.com/monikazapisekstudio/design-engineering-playbook) <br>
- [Dry-run test results](examples/test-results.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Same format as the input text, plus a concise Markdown change log and manual-review flags.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May insert NBSP, soft hyphen, dash, quote, multiplication-sign, and CSS guidance changes while preserving wording.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
