## Description: <br>
Helps creators generate or edit banner illustrations with an image-generation API, resolution choices for draft-to-final iteration, and file naming guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to guide single-image banner generation or editing, including prompt iteration, resolution selection, API key configuration, and output file naming. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad command execution without a scoped script. <br>
Mitigation: Review proposed commands before running them and use the skill only in workspaces where broad command execution is acceptable. <br>
Risk: Prompts, source images, and credentials may be sent to the configured image-generation provider. <br>
Mitigation: Use environment variables for API keys and avoid submitting sensitive images, proprietary prompts, or secrets. <br>
Risk: The artifact includes placeholder command references, which may lead an agent to improvise execution details. <br>
Mitigation: Confirm the actual script, dependencies, and provider configuration before executing generation or editing commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/banner-gen-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-style result descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create PNG image files through a configured image-generation API; supports draft, standard, and final resolution guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
