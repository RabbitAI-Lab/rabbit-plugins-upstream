## Description: <br>
Uploads a local image or file with PicGo and returns a hosted URL for docs, markdown, or sharing when no specific destination is named. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[molunerfinn](https://clawhub.ai/user/molunerfinn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and documentation agents use this skill to turn local screenshots, images, or files into shareable links. It is best suited for inserting assets into README files, blogs, notes, and other markdown documents when the user has not specified another upload destination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload selected local files to publicly accessible image or file hosts. <br>
Mitigation: Confirm before uploading confidential or sensitive non-image files, and tell users that returned links are public to anyone who has the URL. <br>
Risk: A non-local PicGo GUI server endpoint could receive local file paths or GUI server secrets. <br>
Mitigation: Use the default local PicGo endpoint unless the user explicitly trusts another endpoint, and avoid sending secrets to untrusted hosts. <br>
Risk: PicGo tokens and GUI server secrets may be exposed if copied into shared files or logs. <br>
Mitigation: Keep tokens and PICGO_SERVER_SECRET values out of committed files and only pass them when needed for a trusted local setup. <br>


## Reference(s): <br>
- [GUI upload usage](references/gui-upload-usage.md) <br>
- [Upload error triage](references/error-handling.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Plain text or Markdown containing hosted URLs, with shell commands or setup guidance when upload configuration is missing.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return bare URLs, markdown image links, or plain links depending on the user's document context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
