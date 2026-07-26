## Description: <br>
Access a self-hosted Supernote Private Cloud instance to browse files and folders, upload documents (PDF, EPUB) and notes, convert web articles to EPUB/PDF and send them to the device, check storage capacity, and navigate the directory tree. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickian](https://clawhub.ai/user/nickian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Supernote users and agents use this skill to manage documents and notes on a self-hosted Supernote Private Cloud instance, including browsing folders, checking capacity, uploading files, and sending converted web articles to an e-ink device. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Account credentials and reusable tokens may be exposed or reused if the runtime environment or token file is not protected. <br>
Mitigation: Run the skill only in trusted environments, prefer account-scoped credentials where available, and remove /tmp/.supernote_token after use. <br>
Risk: Files and converted articles may include sensitive content that is uploaded to the configured Supernote server. <br>
Mitigation: Use only a trusted Supernote server, prefer HTTPS, and upload only files or URLs that are intended for that account. <br>
Risk: Passwords, file paths, filenames, or folder names containing quotes or unusual characters may behave unexpectedly in shell-based commands. <br>
Mitigation: Use simple paths and names where possible, and review generated commands before execution when inputs contain special characters. <br>
Risk: The Supernote Private Cloud API is reverse-engineered and unofficial, so endpoint behavior may change. <br>
Mitigation: Test login, listing, and upload workflows with non-sensitive files after server, firmware, or API changes. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and command output; scripts may produce EPUB, PDF, or HTML files and text listings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SUPERNOTE_URL, SUPERNOTE_USER, and SUPERNOTE_PASSWORD; article conversion requires Python dependencies including requests, readability-lxml, beautifulsoup4, lxml, and ebooklib.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
