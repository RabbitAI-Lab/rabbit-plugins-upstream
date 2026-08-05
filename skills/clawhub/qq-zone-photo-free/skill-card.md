## Description: <br>
This skill helps agents guide QQ Zone photo album workflows for QR-code login, album listing, and photo browsing in the free edition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to operate an agent-assisted QQ Zone album browsing workflow: log in by QR code, list albums, and retrieve photo URLs for inspection. It is intended for the free feature set and does not cover uploading, downloading, or creating albums. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles full-account cookies that can expose private QQ Zone data if leaked. <br>
Mitigation: Use a dedicated cookie file with restrictive filesystem permissions and do not share or upload cookie contents. <br>
Risk: The skill asks for command and write access while key implementation details are under-specified. <br>
Mitigation: Review proposed commands before execution, run them in a controlled workspace, and limit inputs to login, album listing, and photo browsing tasks. <br>
Risk: Callback URL behavior is under-specified and may expose album or session-related data. <br>
Mitigation: Avoid providing a callback URL unless its recipient and payload handling are fully understood. <br>
Risk: The skill depends on an unofficial social-space API that may change or fail unexpectedly. <br>
Mitigation: Expect breakage after platform changes and re-authenticate or review updated behavior before relying on results. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/thcjp/skills/qq-zone-photo-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local cookie files, album IDs, callback URLs, and command options supplied by the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
