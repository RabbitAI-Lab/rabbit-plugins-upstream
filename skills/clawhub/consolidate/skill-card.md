## Description: <br>
Consolidate and respond to external PR and issue feedback by gathering AI reviews, classifying findings, posting review summaries, and registering deferred items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and maintainers use this skill to consolidate external pull request or issue feedback, classify findings by validity and severity, decide review posture, post summaries, and carry forward deferred follow-up work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent GitHub review and repository tracking changes. <br>
Mitigation: Use interactive review for drafted posts and run only with accounts and repositories where review-state mutation authority is intended. <br>
Risk: Headless execution may post REQUEST_CHANGES, comments, or tracking updates without sufficient user review. <br>
Mitigation: Avoid headless runs on repositories where automatic review or tracking-file edits would be inappropriate. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/consolidate) <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [PR Workflow](pr.md) <br>
- [Collect AI Reviews](collect.md) <br>
- [Analyze and Classify](classify.md) <br>
- [Decide Review Response](decide.md) <br>
- [Post Summary and Review](post.md) <br>
- [Next Action Ask](next.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown review summaries, GitHub review or comment bodies, status text, shell commands, and tracking guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may lead to persistent GitHub review state changes and deferred-item tracking updates.] <br>

## Skill Version(s): <br>
0.4.0 (source: frontmatter, release evidence, and changelog released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
