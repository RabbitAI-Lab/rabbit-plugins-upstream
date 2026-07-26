## Description: <br>
Records long-form user thoughts by running a local script that appends the original message to a dated Markdown file and returns confirmation details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill when a user wants to persist a reflection, opinion, or other long-form thought in the workspace. It writes the raw message to daily-thoughts/raw/YYYY-MM-DD.md and returns file statistics plus content previews as proof of the write. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores full raw user messages in local daily-thoughts/raw files, which may expose secrets, credentials, confidential business material, health information, or other sensitive content. <br>
Mitigation: Use it only for content the user explicitly intends to save; avoid sensitive material or modify the skill to require consent and redact or suppress sensitive text before writing. <br>
Risk: The confirmation flow echoes file excerpts back into chat, which can disclose private content in conversation logs or shared workspaces. <br>
Mitigation: Suppress or redact previews when operating in shared, logged, or sensitive environments. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Markdown, Files] <br>
**Output Format:** [Markdown confirmation based on JSON script output, with a dated Markdown file written in the workspace] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Appends stdin content to daily-thoughts/raw/YYYY-MM-DD.md and exposes the first and last 100 characters in the agent response.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
