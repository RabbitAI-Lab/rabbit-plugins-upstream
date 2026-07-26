## Description: <br>
Tencent Agent Storage helps agents upload, list, search, rename, move, and share files in a user's Tencent Agent Storage cloud drive. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shawnminh](https://clawhub.ai/user/shawnminh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when an agent needs to manage files in Tencent Agent Storage, including upload, directory upload, file listing, search, link generation, folder creation, rename, and move operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can trigger broad cloud uploads and link sharing. <br>
Mitigation: Require explicit user confirmation of local file paths and sharing intent before uploads or link delivery. <br>
Risk: The skill reads storage tokens from multiple local configuration locations. <br>
Mitigation: Use a dedicated least-privilege Tencent Agent Storage token instead of sharing OpenClaw or Hermes credentials. <br>
Risk: The setup guidance includes privileged or curl-based installer commands. <br>
Mitigation: Provision Node.js and the required SDK outside the skill through approved package-management processes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shawnminh/skills/tencent-agent-storage) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/shawnminh) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Tencent Agent Storage operation results, signed download or preview links, file metadata, directory listings, search results, and user-facing status messages.] <br>

## Skill Version(s): <br>
1.0.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
