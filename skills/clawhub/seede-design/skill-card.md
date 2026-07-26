## Description: <br>
Enables agents and developers to use the Seede CLI to generate editable UI designs, social media graphics, posters, and brand-consistent visual assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hilongjw](https://clawhub.ai/user/hilongjw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to generate design assets from natural-language prompts, uploaded references, brand colors, and format requirements through Seede's non-interactive CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Seede API token for non-interactive CLI access. <br>
Mitigation: Use a dedicated expiring token and avoid exposing it in prompts, logs, shell history, or shared environments. <br>
Risk: Uploaded files and referenced URLs may be sent to Seede for cloud processing. <br>
Mitigation: Upload only files and URLs the user is authorized to send to Seede, and verify reference URLs are intended to be publicly accessible. <br>
Risk: The workflow depends on the installed Seede CLI package and external Seede service. <br>
Mitigation: Verify the Seede CLI package or source before installation and review generated commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hilongjw/skills/seede-design) <br>
- [Seede AI](https://seede.ai) <br>
- [Open Claw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI options] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Seede CLI commands and guidance for creating, uploading, listing, and opening design assets; generated designs are created by the external Seede service.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
