## Description: <br>
This skill guides a single-account WeChat content workflow for the "网瘾中年" account, covering topic screening, article drafting, editing, compliance checks, cover generation, draft-box publishing, and performance review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shun1989](https://clawhub.ai/user/shun1989) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and operators use this skill to produce and prepare WeChat public-account articles for the "网瘾中年" account with account-specific editorial, compliance, cover, and draft-box publishing steps. It is scoped to this named WeChat account and is not intended for other social platforms or unrelated coding tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read account-specific local workflow files and use local credentials indirectly during cover generation or publishing-related steps. <br>
Mitigation: Install and run it only for the named WeChat account, and confirm that the local files and credentialed tools are intended for this workflow. <br>
Risk: Broad requests such as "发一篇" or "做选题" can progress toward draft-box publishing actions. <br>
Mitigation: Require explicit user confirmation before any draft-box action and review the title, summary, cover, and final article before publishing to the draft box. <br>
Risk: Articles may violate account-specific editorial or AIGC compliance redlines if checks are skipped. <br>
Mitigation: Run the stated anti-slop and AIGC compliance guard steps, stop on hard-block findings, and send ambiguous findings to manual review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shun1989/skills/wangyin-zhongnian-self-media) <br>
- [AIGC compliance redlines](references/compliance-redlines.md) <br>
- [Data-driven conclusions](references/data-conclusions.md) <br>
- [WeChat writing standards](references/writing-standards.md) <br>
- [Volcengine ARK API endpoint](https://ark.cn-beijing.volces.com/api/v3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown articles, review notes, cover-generation guidance, shell commands, and draft-box publishing diagnostics] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local workflow files, ARK cover generation credentials, and a confirmed WeChat draft-box publishing command when the user requests publishing.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata and artifact skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
