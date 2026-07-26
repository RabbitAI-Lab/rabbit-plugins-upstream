## Description: <br>
Cmclaw connects an agent to YouCloud Creative Manager to generate advertising strategy analysis, creative inspiration, and material strategy reports from selected asset scopes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youcloud](https://clawhub.ai/user/youcloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and growth teams with a paid YouCloud Creative Manager account use this skill to request ad strategy reports or iterative creative brainstorming against selected asset scopes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends prompts, selected material scope, and account-derived identifiers to the YouCloud API using a YouCloud API key. <br>
Mitigation: Use it only with an authorized YouCloud Creative Manager account and avoid including material that should not be sent to YouCloud. <br>
Risk: The optional DAM_API_BASE setting can redirect requests to a different endpoint. <br>
Mitigation: Leave DAM_API_BASE unset for the production YouCloud endpoint unless the alternate endpoint is trusted. <br>


## Reference(s): <br>
- [Cmclaw on ClawHub](https://clawhub.ai/youcloud/skills/cmclaw) <br>
- [DamClaw Skill API](references/cm-claw-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report or conversational markdown response with a YouCloud conversation detail link.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires YOUCLOUD_API_KEY. DAM_API_BASE is optional and should only point to a trusted endpoint. Responses may take up to 650 seconds.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
