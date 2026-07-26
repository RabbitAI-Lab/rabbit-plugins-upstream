## Description: <br>
Paste Rs uploads text, Markdown, or HTML snippets to paste.rs and returns a shareable URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[banghasan](https://clawhub.ai/user/banghasan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to publish selected logs, configuration snippets, Markdown, HTML, or command output as a paste.rs link when sharing a compact reference is preferable to sending long text inline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected text or files are uploaded to a public paste service. <br>
Mitigation: Review content before upload, keep redaction enabled, and avoid secrets, credentials, proprietary material, or other sensitive content. <br>
Risk: The uploader saves a local Markdown copy before uploading. <br>
Mitigation: Choose an appropriate output directory and delete the saved .md file when local retention is not desired. <br>


## Reference(s): <br>
- [paste.rs API quick reference](references/paste-rs-api.md) <br>
- [paste.rs service](https://paste.rs) <br>
- [ClawHub skill page](https://clawhub.ai/banghasan/skills/paste-rs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Plain-text paste URL on stdout, saved local Markdown path on stderr, and Markdown guidance with shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uploads non-empty content to paste.rs, applies best-effort redaction by default, and saves a local .md copy before upload.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
