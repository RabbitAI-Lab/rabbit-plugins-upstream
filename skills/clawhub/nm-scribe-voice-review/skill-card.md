## Description: <br>
Runs parallel prose and craft review agents against a voice profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and content teams use this skill to review generated or existing prose against a voice profile, separate hard failures from advisory feedback, and apply selected improvements before saving the final text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad review-related triggers may activate the skill on drafts the user did not intend to process. <br>
Mitigation: Install only when the user is comfortable with this review workflow and confirm the target draft before running it. <br>
Risk: Automatic hard-failure fixes can change prose before advisory review. <br>
Mitigation: Review the reported fixes and final diff before relying on or publishing the saved text. <br>
Risk: Learning mode can save additional draft snapshots that may contain sensitive or proprietary text. <br>
Mitigation: Avoid sensitive drafts unless storage locations and retention expectations are understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-review) <br>
- [Claude Night Market scribe plugin](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, files] <br>
**Output Format:** [Markdown advisory tables, user decision prompts, prose edits, and saved text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May auto-fix hard failures, present advisory changes for user choice, save final text, and optionally save learning snapshots.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
