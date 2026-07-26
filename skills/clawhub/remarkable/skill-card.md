## Description: <br>
Send files and web articles to a reMarkable e-ink tablet via the reMarkable Cloud. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickian](https://clawhub.ai/user/nickian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and reMarkable users use this skill to upload PDF or EPUB files, convert web articles into readable ebook files, and browse or manage reMarkable Cloud folders from an agent-assisted shell workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connecting rmapi gives a third-party command-line tool access to the user's reMarkable Cloud account. <br>
Mitigation: Use a reviewed or pinned rmapi release and install only when that account access is acceptable. <br>
Risk: rmapi caches authentication tokens under ~/.rmapi. <br>
Mitigation: Protect the local token directory and clear ~/.rmapi when the account should no longer be available from the machine. <br>
Risk: The skill can upload the wrong URL, local file, or destination folder if inputs are not checked. <br>
Mitigation: Confirm the URL, local path, and target reMarkable folder before sending content to the cloud. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nickian/skills/remarkable) <br>
- [rmapi project](https://github.com/ddvk/rmapi) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce EPUB, PDF, or HTML files during article conversion before uploading through rmapi.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
