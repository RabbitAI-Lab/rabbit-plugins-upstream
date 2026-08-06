## Description: <br>
Improves a voice profile by learning from manual edits. Use after editing generated text to refine registers and close voice drift over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and writers use this skill after manually editing generated drafts to compare post-review and post-edit versions, identify recurring voice patterns, and propose profile updates for user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated, reviewed, and manually edited drafts may be retained in a local voice-profile learning directory. <br>
Mitigation: Install only when local retention is acceptable, and periodically review or clean $HOME/.claude/voice-profiles/*/learning when drafts may contain sensitive material. <br>
Risk: Learning proposals can introduce incorrect, stale, or contradictory voice rules if accepted without review. <br>
Mitigation: Use the skill's evidence thresholds, contradiction checks, and user-approval step before applying profile changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-voice-learn) <br>
- [Scribe homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON snippets and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose accumulator entries, register or craft-rule edits, contradiction notices, and cleanup guidance for local voice-profile learning files.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
