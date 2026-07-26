## Description: <br>
Reviews logged incidents and activity to improve agent configuration through proposed edits to core files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonexplorer5](https://clawhub.ai/user/dragonexplorer5) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent operators, and external users use this skill to review logged incidents and activity patterns, then produce targeted proposals for improving agent configuration files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Proposed edits could introduce incorrect or misleading guidance into agent configuration files. <br>
Mitigation: Review generated proposals before applying them, especially when they affect governance or workflow instructions. <br>
Risk: When AUTO_APPLY is deliberately enabled, the skill can apply limited configuration edits after drafting proposals. <br>
Mitigation: Leave AUTO_APPLY set to false unless automatic edits are acceptable; rely on proposal review and backups for controlled changes. <br>
Risk: Identity and user-context files can contain sensitive or high-impact instructions. <br>
Mitigation: Keep manual approval for SOUL.md and USER.md changes, as described by the skill behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonexplorer5/skills/self-review) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown proposal summaries and plain-language review guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create trainer state, proposal, log, and backup files when used as documented.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
