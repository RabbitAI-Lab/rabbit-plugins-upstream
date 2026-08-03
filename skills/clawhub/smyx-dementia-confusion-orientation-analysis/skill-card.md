## Description: <br>
Analyzes fixed-camera and optional microphone inputs from dementia care settings or homes to identify confusion and disorientation signals, produce structured reports, and guide orientation-soothing follow-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Care teams, operators, and agent workflows use this skill to submit dementia-care audio/video or URLs for cloud analysis, receive structured confusion/disorientation findings, and review history reports. It is intended to support caregiver review and orientation workflows, not to provide medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive dementia-care audio/video and identity data may be sent to Lifeemergence cloud services. <br>
Mitigation: Use only with documented consent from the person, family, or care setting; review cloud processing, retention, access controls, and local legal requirements before deployment. <br>
Risk: The release overstates automatic soothing and escalation behavior compared with the inspected code. <br>
Mitigation: Validate speaker, lighting, caregiver-app, and emergency integrations separately before relying on automated intervention. <br>
Risk: Persistent local account tokens and default user identity handling can expose care records if the workspace is shared or poorly protected. <br>
Mitigation: Run in a controlled workspace, restrict access to local data files, and rotate or revoke tokens when moving or decommissioning an installation. <br>
Risk: Behavior recognition results may be incomplete or misleading for clinical decisions. <br>
Mitigation: Treat outputs as caregiver-support information only, require human review, and do not use the skill to diagnose dementia or related medical conditions. <br>


## Reference(s): <br>
- [Skill API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text with structured findings, recommendations, history tables, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
