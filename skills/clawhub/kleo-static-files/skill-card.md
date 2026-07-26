## Description: <br>
Host static files on subdomains with optional authentication for HTML, images, CSS, JavaScript, and other static content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[awaaate](https://clawhub.ai/user/awaaate) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to create static-file hosting sites, upload files or directories, configure optional basic authentication, inspect hosted files, and manage site lifecycle operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish, overwrite, delete, and share hosted content through a privileged static-file service. <br>
Mitigation: Use a dedicated API key, require explicit confirmation before delete, overwrite, clean-deploy, or share operations, and review commands before execution. <br>
Risk: The one-line installer requests privileged server setup authority. <br>
Mitigation: Inspect and pin the installer to a trusted commit before running it, or use the documented manual installation path. <br>
Risk: Basic authentication alone may be insufficient for highly sensitive files. <br>
Mitigation: Avoid hosting highly sensitive material behind only basic auth; apply stronger access controls or a separate secure sharing channel. <br>


## Reference(s): <br>
- [Installation Guide](references/install.md) <br>
- [Bun Runtime](https://bun.sh) <br>
- [Caddy Web Server](https://caddyserver.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include site URLs, API endpoint examples, status checks, and deletion or upload commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
