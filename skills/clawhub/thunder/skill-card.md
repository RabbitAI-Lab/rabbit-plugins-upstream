## Description: <br>
Thunder decodes and encodes Thunder/Xunlei thunder:// download links locally and can also decode qqdl:// and flashget:// links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and users can inspect Thunder/Xunlei download links, convert them into standard URLs for tools such as wget or aria2, or encode ordinary URLs into thunder:// format. Agents can use it to explain pasted links, prepare download commands, or batch-convert link lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Decoded links can reveal untrusted or unsafe download URLs. <br>
Mitigation: Check the decoded domain, path, and filename before opening the URL or downloading content. <br>
Risk: Download commands prepared from decoded links may fetch content from sources the user does not trust. <br>
Mitigation: Run wget, aria2, or similar commands only after confirming the source and intended file. <br>


## Reference(s): <br>
- [Thunder/Xunlei official website](https://www.xunlei.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text URLs or encoded links, with optional Markdown guidance and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local Base64 transformations only; decoded URLs should be treated as untrusted until reviewed.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
