## Description: <br>
Helps agents plan, draft, revise, and quality-check long-form Chinese web fiction using structured workflows for concepts, worldbuilding, characters, outlines, chapters, and continuity tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External writers and writing agents use this skill to build and maintain long-form web novel projects, including topic selection, setting and character design, serialized outlining, chapter drafting, revision, and local prose checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or modify many project files during outlining, drafting, revision, and tracking. <br>
Mitigation: Install and run it in a dedicated writing project, then review generated file changes before accepting them. <br>
Risk: The skill may run local Node.js cleanup and check scripts against draft files. <br>
Mitigation: Inspect the script commands and their reported findings before applying rewrites or punctuation normalization. <br>
Risk: The skill includes guidance for adapting existing stories, which can create originality or rights concerns for publishable work. <br>
Mitigation: Use benchmark works as high-level craft references only, and perform originality and rights review before publication. <br>
Risk: Some genre guidance uses gendered audience patterns that may not fit every publication context. <br>
Mitigation: Review and override gendered assumptions to match the intended audience and editorial standards. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-write) <br>
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Core skill workflow](artifact/SKILL.md) <br>
- [Reader contract and progression](artifact/references/reader-contract-and-progression.md) <br>
- [Artifact protocols](artifact/references/artifact-protocols.md) <br>
- [Daily writing workflow](artifact/references/workflow-daily.md) <br>
- [Revision workflow](artifact/references/workflow-revision.md) <br>
- [Quality checklist](artifact/references/quality-checklist.md) <br>
- [Anti-AI writing guidance](artifact/references/anti-ai-writing.md) <br>
- [AI-pattern check script](artifact/scripts/check-ai-patterns.js) <br>
- [Degeneration check script](artifact/scripts/check-degeneration.js) <br>
- [Punctuation normalization script](artifact/scripts/normalize-punctuation.js) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown prose, project files, and inline shell commands for local checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify outline, chapter, setting, tracking, and reference files in the active writing project.] <br>

## Skill Version(s): <br>
1.1.15 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
