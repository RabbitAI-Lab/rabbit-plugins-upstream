## Description: <br>
Generates text in a learned writing voice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and content teams use this skill to draft prose in an authorized, extracted writing voice. The skill loads local voice profiles, selects an appropriate register, frames source material as working notes, and produces polished text for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local voice profile files and optional project voice overrides, which may contain personal writing samples or sensitive context. <br>
Mitigation: Install only where the agent may access those files, and review profile and override contents before use. <br>
Risk: Generated text may imitate a writing voice that the user is not authorized to use. <br>
Mitigation: Use only voice profiles you are authorized to imitate and review generated text before publication. <br>
Risk: The workflow may silently rewrite banned phrases or punctuation before showing the final draft. <br>
Mitigation: Review the final output against the source material and style requirements before sharing it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-scribe-voice-generate) <br>
- [Scribe Plugin Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Generation Pipeline Module](artifact/modules/generation-pipeline.md) <br>
- [Register Selection Module](artifact/modules/register-selection.md) <br>
- [Source Framing Module](artifact/modules/source-framing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or prose text with optional inline guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May silently clean banned phrases and punctuation before presenting the draft.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
