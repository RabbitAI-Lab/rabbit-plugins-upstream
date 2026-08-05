## Description: <br>
Generates text in a learned writing voice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and writers use this skill to draft prose in a selected learned voice profile, with register selection, source-material framing, style cleanup, and optional review dispatch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local voice profile files and project voice overrides, which may contain personal writing patterns or sensitive context. <br>
Mitigation: Install and run it only when the agent may access those profile files, and review generated text before sharing it. <br>
Risk: Generated writing can be presented as a real person's authorial voice. <br>
Mitigation: Review the draft yourself, especially when it represents a real person or public authorial identity. <br>
Risk: Automatic banned-phrase and punctuation cleanup can silently change the generated draft. <br>
Mitigation: Inspect the final text after cleanup and before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-generate) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [Configured homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Generation pipeline module](artifact/modules/generation-pipeline.md) <br>
- [Register selection module](artifact/modules/register-selection.md) <br>
- [Source framing module](artifact/modules/source-framing.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown prose with inline shell snippets and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local voice profile files and can apply automatic style cleanup before presenting drafts.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
