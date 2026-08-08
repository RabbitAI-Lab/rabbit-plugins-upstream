## Description:

電子書轉換工具箱：支援 EPUB / PDF / MOBI / AZW3 / FB2 → TXT / Markdown / HTML / JSON；批量轉換、封面萃取、元資料讀寫、圖書館自動分類。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to convert, extract, organize, and report on local ebook and PDF collections through command-line workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local EPUB and PDF files, including optional OCR and parser-heavy conversion paths.

Mitigation: Run it only on ebook and PDF files you intend the agent to process, prefer trusted inputs, and avoid untrusted EPUB/PDF files until temporary-path handling is improved.

Risk: Batch conversion, metadata editing, recursive scans, and organization modes can create, copy, rewrite, or link files across local directories.

Mitigation: Review proposed commands before execution, use dry-run or link-only modes where available, and keep backups for libraries before metadata edits or recursive organization.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xuan905/skills/ebook-converter-pro)
- [README](README.md)
- [Skill Definition](SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated ebook, metadata, report, image, JSON, HTML, and text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create converted files, metadata exports, reports, extracted cover images, organized library folders, or symlinks depending on the selected script and command options.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
