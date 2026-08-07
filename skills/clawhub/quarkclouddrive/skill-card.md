## Description: <br>
Quark Drive skill lets agents authenticate with Quark Drive and manage cloud files, including upload/download with resume, sharing and saving shared links, file search, photo organization, and AI-assisted file summarization or Q&A. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[quarkdrive](https://clawhub.ai/user/quarkdrive) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to connect to Quark Drive, search and organize cloud files, upload or download files, create or consume share links, and ask AI-assisted questions over selected drive content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer may change the local Node.js environment or system packages and can update the skill from a remote zip. <br>
Mitigation: Install in an isolated environment first and review publisher trust before allowing installation or update actions. <br>
Risk: The skill can access Quark Drive files and metadata and can create share links. <br>
Mitigation: Use it only with accounts and files where cloud access and sharing are acceptable; review share-link outputs before distributing them. <br>
Risk: Prompts and selected drive content or metadata may be sent to Quark services for search, organization, summarization, or Q&A. <br>
Mitigation: Avoid highly sensitive files or prompts unless those data flows are acceptable for the intended use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/quarkdrive/skills/quarkclouddrive) <br>
- [Publisher profile](https://clawhub.ai/user/quarkdrive) <br>
- [Quark Drive](https://pan.quark.cn) <br>
- [Assistant capability guide](references/assistant.md) <br>
- [Authorization and account management](references/auth.md) <br>
- [File operations guide](references/file-ops.md) <br>
- [Photo organization guide](references/file-organize.md) <br>
- [File read guide](references/file-read.md) <br>
- [Save shared links guide](references/file-saveas.md) <br>
- [File search guide](references/file-search.md) <br>
- [File sharing guide](references/file-share.md) <br>
- [File upload guide](references/file-upload.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and structured command-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local files produced by Quark Drive commands and may present search, sharing, upload, download, organization, or AI-assistant results.] <br>

## Skill Version(s): <br>
1.0.11 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
