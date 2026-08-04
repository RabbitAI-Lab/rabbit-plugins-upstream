## Description: <br>
GitHub README Writing System helps agents write or rewrite README files with tagline guidance, first-screen structure, section copywriting, AI-agent integration guidance, anti-patterns, and a pre-publish checklist. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gingiris-1031](https://clawhub.ai/user/gingiris-1031) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, and documentation-focused agents use this skill to draft, rewrite, or review a specific GitHub README so it explains the project quickly, provides a clear quick start, and avoids common README copywriting anti-patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: README edits may overstate product claims, add questionable star-request language, or introduce badges, install commands, and external links that are not accurate. <br>
Mitigation: Review README changes before publishing, with special attention to claims, star requests, badges, install commands, and external links. <br>
Risk: Because the skill can edit files, it may change documentation outside the intended release workflow if used in the wrong repository. <br>
Mitigation: Run the skill only in the intended repository and inspect the resulting file diff before publishing or committing changes. <br>


## Reference(s): <br>
- [ClawHub gr-readme skill page](https://clawhub.ai/gingiris-1031/skills/gr-readme) <br>
- [Claude Code Skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills) <br>
- [Claude Code Memory documentation](https://docs.anthropic.com/en/docs/claude-code/memory) <br>
- [Anthropic prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) <br>
- [AFFiNE README case reference](https://github.com/toeverything/AFFiNE) <br>
- [Dify README case reference](https://github.com/langgenius/dify) <br>
- [InsForge README case reference](https://github.com/insforgehq/insforge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, checklists, and README review notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose edits to README files and should be reviewed before publication.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
