## Description: <br>
Runs parallel prose and craft review agents against a voice profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and agents use this skill to review generated prose against a voice profile, automatically fix hard failures, and present advisory prose and craft recommendations for user decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically modify generated text when it detects hard failures. <br>
Mitigation: Review the diff and final text before publishing, and confirm automatic hard-failure edits are acceptable for the document. <br>
Risk: Learning mode can save local review snapshots under the user's voice profile directory. <br>
Mitigation: Confirm whether learning mode is enabled and where snapshots are stored before using the skill on important or confidential text. <br>
Risk: Advisory prose and craft recommendations may not match the author's intent. <br>
Mitigation: Treat advisory tables as suggestions and rely on the user's accept, reject, or rewrite decisions before finalizing text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-review) <br>
- [Scribe plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown advisory tables and edited text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May apply hard-failure edits before presenting advisory review decisions; may save snapshots when learning mode is enabled.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
