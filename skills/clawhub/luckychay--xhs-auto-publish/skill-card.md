## Description: <br>
Generates and publishes Xiaohongshu notes from a supplied topic or an automatically selected topic, including cover text and required hashtags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckychay](https://clawhub.ai/user/luckychay) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Social media operators and agents use this skill to generate and publish one Xiaohongshu note about Singapore private university study-abroad topics from either a manual topic or automatic topic selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish public Xiaohongshu posts without a final user approval step. <br>
Mitigation: Add a preview-and-confirm step before publishing and verify the account selected by the xhs integration. <br>
Risk: Scheduled execution can repeatedly publish generated content before the operator has reviewed quality or account impact. <br>
Mitigation: Avoid cron scheduling until the generated content, posting frequency, and account configuration have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luckychay/xhs-auto-publish) <br>
- [Artifact README](README.md) <br>
- [Detailed usage guide](references/README.md) <br>
- [Publishing script](references/xhs-auto-publish-v2.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text guidance with shell command examples and generated agent prompts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May publish directly to a logged-in Xiaohongshu account without a final approval step.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
