## Description: <br>
Lovart Skill enables agents to generate images, videos, audio, and music through Lovart AI while managing Lovart projects, conversation threads, uploads, downloads, user settings, and generation modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lovart-admin](https://clawhub.ai/user/lovart-admin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request Lovart AI media generation or manage Lovart project and thread state from an agent. It supports reference uploads, generated artifact downloads, project canvas links, and mode or model selection for Lovart generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, selected attachments, and generated-artifact traffic are sent to Lovart using the user's Lovart API keys. <br>
Mitigation: Install and use the skill only when this Lovart data flow is acceptable for the user's content and account. <br>
Risk: The skill can reuse local Lovart project and thread history stored in ~/.lovart/state.json. <br>
Mitigation: Review or clear ~/.lovart/state.json when project or conversation continuity should not be reused. <br>
Risk: TLS verification can be weakened when LOVART_INSECURE_SSL is set. <br>
Mitigation: Avoid setting LOVART_INSECURE_SSL unless the user knowingly accepts weaker TLS protection. <br>
Risk: Some high-cost generation operations may consume Lovart credits. <br>
Mitigation: Require explicit user confirmation before running confirmation commands for credit-consuming operations. <br>


## Reference(s): <br>
- [Lovart Skill on ClawHub](https://clawhub.ai/lovart-admin/skills/lovart-skill) <br>
- [Lovart Project Canvas](https://www.lovart.ai/canvas?projectId={project_id}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON command output, and downloaded media files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Lovart API credentials; generated artifacts may be downloaded to local paths and project/thread state may be persisted in ~/.lovart/state.json.] <br>

## Skill Version(s): <br>
1.0.12 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
