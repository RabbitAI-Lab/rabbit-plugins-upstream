## Description: <br>
AList CLI provides AI agents with command-line workflows for AList file management, including upload, download, listing, folder creation, deletion, moving, search, and URL retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeshunee](https://clawhub.ai/user/leeshunee) <br>

### License/Terms of Use: <br>
GNU General Public License v3.0 <br>


## Use Case: <br>
Developers and agent users use this skill to manage files on an AList cloud storage server from a conversation or coding-agent session. It is suited for browsing storage, uploading or sharing files, retrieving download links, and performing basic file operations when the user has provided an appropriate AList account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup guidance includes privileged install options and shell profile changes. <br>
Mitigation: Prefer a virtual environment, alias, or direct script invocation; use sudo or persistent shell changes only after explicit user approval. <br>
Risk: AList credentials and tokens may be exposed if passwords are saved in shell startup files or command history. <br>
Mitigation: Keep credentials out of repositories and shell profiles, use temporary environment variables or a secrets manager, and avoid printing or storing tokens beyond the active session. <br>
Risk: The skill can delete or move remote files through rm and mv commands. <br>
Mitigation: Require explicit confirmation before destructive file operations and use a least-privilege AList account limited to the paths the agent should manage. <br>
Risk: The bundled OpenAPI reference includes broad administrative API coverage beyond ordinary file management. <br>
Mitigation: Treat the OpenAPI file as reference documentation and restrict routine use to the documented file-management commands unless the user explicitly authorizes broader administrative actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/leeshunee/skills/alist-cli) <br>
- [README](artifact/README.md) <br>
- [Onboarding Guide](artifact/references/ONBOARDING.md) <br>
- [AList OpenAPI Reference](artifact/references/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and command-output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AList preview URLs, signed download URLs, file listings, and setup commands.] <br>

## Skill Version(s): <br>
1.7.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
