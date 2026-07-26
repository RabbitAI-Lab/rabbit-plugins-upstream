## Description: <br>
Pancake Skills helps agents interact with the Pancake Platform API to manage pages, conversations, messages, customers, statistics, tags, posts, users, media uploads, and chat plugin operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[suminhthanh](https://clawhub.ai/user/suminhthanh) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to prepare Pancake Platform API shell commands and guidance for reading operational data and performing authorized updates to pages, conversations, messages, customers, staff assignments, exports, uploads, and chat plugin messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact token and write actions may be executed against Pancake pages, conversations, customers, uploads, exports, or chat plugin messages. <br>
Mitigation: Install only in a trusted workspace, keep Pancake credentials out of logs and transcripts, and require explicit user intent before running commands that mutate data or expose sensitive exports. <br>
Risk: Some high-impact actions bypass the skill's stated CONFIRM_WRITE guard. <br>
Mitigation: Patch the scripts to require CONFIRM_WRITE=YES for pages-generate-token and chat-plugin-send before use, as recommended by the security guidance. <br>
Risk: Credential values passed through shell helpers could be mishandled if command inputs are logged or interpolated unsafely. <br>
Mitigation: Use credentials only in trusted shells, avoid pasting secrets into agent chat, and patch url_encode to pass data as a Python argument instead of interpolating it into code. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/suminhthanh/skills/pancake-skills) <br>
- [OpenAPI Pancake specification](references/openapi-pancake.yaml) <br>
- [Pancake support](https://www.pancake.biz/contact) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Pancake access tokens and explicit confirmation for most write operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
