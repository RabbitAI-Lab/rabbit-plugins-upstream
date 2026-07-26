## Description: <br>
Optimizes EPUB reading experience by rewriting CSS, improving bilingual layout, applying reader-friendly fonts, styling code blocks and tables, and fixing color-contrast rendering issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and EPUB maintainers use this skill to inspect EPUB packages, rewrite stylesheets, repair formula-as-image layout, optionally subset embedded fonts, and rebuild standards-compliant EPUB files without changing book text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local EPUB edits can overwrite or replace working files if paths are chosen incorrectly. <br>
Mitigation: Keep a backup of the original book and confirm exact input and output paths before running helpers. <br>
Risk: Optional remote font or repository fetching can introduce untrusted content. <br>
Mitigation: Fetch remote resources only with explicit user approval, from trusted sources, and pinned release tags. <br>
Risk: Missing dependencies or host tools may lead to unsafe ad hoc installation steps. <br>
Mitigation: Fail closed on missing dependencies and ask the user to approve any manual installation. <br>
Risk: LaTeX shell escape can execute commands when enabled on untrusted content. <br>
Mitigation: Keep shell escape disabled unless the user consents, the environment is sandboxed, and the content is trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samonysh/skills/epub-reader-optimizer) <br>
- [LXGW WenKai Lite regular font release](https://github.com/lxgw/LxgwWenKai-Lite/releases/download/v1.522/LXGWWenKaiLite-Regular.ttf) <br>
- [LXGW WenKai Mono Lite regular font release](https://github.com/lxgw/LxgwWenKai-Lite/releases/download/v1.522/LXGWWenKaiMonoLite-Regular.ttf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and editable CSS/Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce optimized EPUB files when applied to user-provided books; network fetching and dependency installation require explicit approval.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
