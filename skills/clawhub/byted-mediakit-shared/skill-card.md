## Description: <br>
Byted Mediakit Shared guides agents in using mediakit-cli for media workflows, including setup, authentication, command discovery, local and cloud mode selection, async task polling, and shared error-handling behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volcvnebot](https://clawhub.ai/user/volcvnebot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to configure mediakit-cli, discover supported media commands, run cloud or local media operations, and poll shared async task status safely. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed if real credentials are placed directly on command lines or in insecure locations. <br>
Mitigation: Prefer environment variables, the interactive init flow, or a secure config path for API keys. <br>
Risk: Sensitive media may be uploaded during cloud-mode processing. <br>
Mitigation: Use local mode for sensitive media unless uploading to the MediaKit cloud service is intended. <br>
Risk: The skill depends on the external MediaKit CLI package and service. <br>
Mitigation: Install and use the skill only when the MediaKit CLI package and service are trusted. <br>


## Reference(s): <br>
- [Query Task](reference/query_task.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, tables, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mediakit-cli; cloud mode requires MEDIAKIT_API_KEY, and local media processing may require ffmpeg and ffprobe.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
