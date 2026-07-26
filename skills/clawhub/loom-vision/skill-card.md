## Description: <br>
Process a Loom share URL into multimodal context: downloaded video, sampled frames at one frame per 5 seconds, and the auto-generated transcript. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scrollinondubs](https://clawhub.ai/user/scrollinondubs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to process Loom walkthroughs, bug reports, code reviews, design reviews, and demos into transcript and visual frame context that an agent can inspect. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Downloaded Loom videos, transcripts, and sampled frames may contain credentials, internal screens, source code, or personal data. <br>
Mitigation: Treat the output directory as sensitive and delete generated files when they are no longer needed. <br>


## Reference(s): <br>
- [Loom Vision on ClawHub](https://clawhub.ai/scrollinondubs/skills/loom-vision) <br>
- [Publisher profile](https://clawhub.ai/user/scrollinondubs) <br>
- [Behalf.bot](https://behalf.bot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and generated local files such as video, transcript, and sampled image frames.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local per-video output directories and may include sensitive video, transcript, and frame files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
