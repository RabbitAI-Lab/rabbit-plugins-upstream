## Description: <br>
Improves a voice profile by learning from manual edits, refining registers and reducing voice drift over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and agent users use this skill after manually editing generated text to compare review and edit snapshots, identify recurring voice patterns, and propose updates to voice-profile rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores generated and edited writing samples in the local voice-profile directory. <br>
Mitigation: Avoid running it on sensitive drafts unless local snapshot retention is acceptable, and review or clean stored snapshots periodically. <br>
Risk: Broad trigger terms could invoke the learning flow when it is not intended. <br>
Mitigation: Invoke the skill deliberately after completing manual edits and confirm proposed profile changes before applying them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-learn) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces pattern analysis, hold/apply recommendations, proposed profile-rule edits, and local accumulator updates for user review.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
