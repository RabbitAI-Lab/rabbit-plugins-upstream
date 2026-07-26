## Description: <br>
Nm Scribe Session Replay converts a Claude Code session JSONL file into an animated GIF terminal replay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn past Claude Code sessions into GIF replays for pull request evidence, demos, tutorials, or internal sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive local Claude session history by listing previews and rendering full transcripts into shareable GIFs. <br>
Mitigation: Use a narrow turn range, exclude tool output unless needed, and review the generated GIF for secrets or confidential context before sharing. <br>
Risk: Generated session replays may carry confidential development context into pull requests, chat, or tutorials. <br>
Mitigation: Treat generated GIFs as sensitive until redacted and share them only in destinations appropriate for the underlying session content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-session-replay) <br>
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [GIF file path and concise text status, with optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can filter turn ranges and visible layers before rendering; GIF output should be reviewed for sensitive session content before sharing.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
