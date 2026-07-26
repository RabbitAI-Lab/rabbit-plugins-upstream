## Description: <br>
Presents adaptive codebase challenge questions with multiple-choice and trace exercises. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to test contributor knowledge of a codebase through adaptive challenge questions, answer evaluation, scoring, and progress tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Challenge workflows can read and update local .gauntlet state, including knowledge, pending challenge, progress, and pass-token files. <br>
Mitigation: Review the generated challenge and any proposed state changes before relying on scoring or gate results. <br>
Risk: Operational use may involve service credentials or retained incident notes, according to the ClawHub security guidance. <br>
Mitigation: Use scoped tokens, review commands before destructive actions or outbound email, and avoid storing sensitive incident details unnecessarily. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-challenge) <br>
- [claude-night-market gauntlet](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown with challenge prompts, scoring feedback, and concise setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local .gauntlet knowledge, pending challenge, progress, and pass-token state files.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
