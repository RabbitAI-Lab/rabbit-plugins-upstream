## Description: <br>
One Novel Skill helps writers create Chinese web novels from project setup through chapter drafting, continuity tracking, review, and revision with optional local LLM provider support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xincen0725](https://clawhub.ai/user/xincen0725) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External writers and developers use this skill to initialize Chinese novel projects, draft and continue chapters, review quality and consistency, and maintain project state across long-form writing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create and modify files inside a novel project. <br>
Mitigation: Install and run it only in the intended project workspace, review generated changes before relying on them, and keep backups for important drafts. <br>
Risk: Local generation mode may use API keys or local providers already available in the environment. <br>
Mitigation: Confirm which providers are configured before enabling local mode and use provider credentials with appropriate scope and billing controls. <br>
Risk: Long-form writing automation can produce continuity, quality, or safety issues that are not fully caught by automated checks. <br>
Mitigation: Use the built-in review and quality-gate workflows as aids, then perform human editorial review before publication. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xincen0725/skills/one-novel-skill) <br>
- [Reference Index](artifact/references/index.json) <br>
- [Architecture Overview](artifact/docs/wiki/architecture/ARCHITECTURE.md) <br>
- [Quality Gate Workflow](artifact/docs/wiki/workflows/QUALITY_GATE.md) <br>
- [Original Genre Opening Templates](artifact/references/original/genre-opening-templates.md) <br>
- [Hook Density Model](artifact/references/original/hook-density-model.md) <br>
- [Platform Strategy](artifact/references/platform-strategy.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text and Markdown, with JSON state files and shell commands when local workflows are used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify novel project files and may call configured LLM providers in local generation mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
