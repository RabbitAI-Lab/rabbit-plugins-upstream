## Description:

Audits JPG, PNG, and WebP images for pornographic, political, terrorist, or otherwise unsafe content by compressing images and submitting them to the NX API, then summarizing results in a table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaowu89](https://clawhub.ai/user/xiaowu89)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user asks to audit local image files, folders, or image URLs for unsafe visual content. It prepares images for NX API moderation and reports pass, violation, and failure outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and URLs submitted for audit may be shared with the NX API.

Mitigation: Run the skill only on images or URLs the user intends to submit to NX API for moderation.

Risk: The skill may load configuration from nearby or home-directory .env files.

Mitigation: Run it from a clean working directory, avoid directories with sensitive .env files, and use a scoped or disposable NX_API_KEY.

Risk: The script may automatically install the sharp dependency globally.

Mitigation: Review the installation behavior before use and prefer running in an isolated environment where dependency changes are acceptable.

Risk: The script may create a persistent device identifier in the user's home directory.

Mitigation: Use a disposable environment when persistent local identifiers are not acceptable.

Risk: Obfuscated code can make operational behavior difficult to inspect.

Mitigation: Review and scan the artifact before deployment, and treat the suspicious security verdict as requiring human approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaowu89/skills/skill-function)
- [Publisher profile](https://clawhub.ai/user/xiaowu89)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown table with concise status text and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports per-image pass, violation, or failure status; local files are compressed before API submission.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
