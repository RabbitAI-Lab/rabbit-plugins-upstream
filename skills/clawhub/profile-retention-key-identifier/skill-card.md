## Description: <br>
Plan a profile governance setting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wxt-ai](https://clawhub.ai/user/wxt-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Workspace governance users use this skill to turn a supplied profile configuration or governance request into a concise retention-policy key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Future versions that request credentials, private files, command execution, or network access would materially change the reviewed behavior. <br>
Mitigation: Review those capability requests before installation and treat them as out of scope for this lightweight text-processing skill. <br>
Risk: A generated governance key may be too terse or mismatched for a workspace policy decision. <br>
Mitigation: Review the returned key against the supplied profile_note before using it in policy configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/profile-retention-key-identifier) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Text field named key] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a concise key from the user-provided profile_note; no credentials, private-file access, command execution, or network access are required.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
