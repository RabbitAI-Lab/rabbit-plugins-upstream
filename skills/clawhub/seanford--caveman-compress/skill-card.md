## Description: <br>
Compresses natural-language memory files such as CLAUDE.md, todos, and preferences into shorter caveman-style prose while preserving technical substance, code, URLs, and structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to reduce recurring context cost from project memory and notes files while keeping technical details intact. It is intended for explicit, user-selected natural-language files and creates a readable backup before replacing the original. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected file contents are sent to Claude or Anthropic for compression. <br>
Mitigation: Use only the explicit /caveman:compress <filepath> form and do not run the skill on files containing secrets or private notes that should not cross that third-party boundary. <br>
Risk: Compression overwrites the selected source file. <br>
Mitigation: The skill saves FILE.original.md before writing compressed output, refuses to proceed when a backup already exists, verifies the backup readback, and restores the original if validation fails after retries. <br>
Risk: Subprocess and file I/O behavior can be risky if command arguments or paths are ambiguous. <br>
Mitigation: The artifact uses a fixed subprocess argument list without shell interpolation, reads only the user-selected path, rejects large files, skips code/config files, and denies filenames or paths that look sensitive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/seanford/skills/caveman-compress) <br>
- [README.md](README.md) <br>
- [SECURITY.md](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Compressed Markdown or plain text files plus concise status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates FILE.original.md backups; preserves code blocks, inline code, URLs, headings, file paths, commands, tables, dates, versions, and numeric values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/__init__.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
