## Description: <br>
Reverse-imports an existing Chinese fiction manuscript into a structured writing project that can be continued with long-form or short-form story writing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Authors and writing-workflow users invoke this skill to import a completed or in-progress novel, analyze it by length, and reconstruct a project directory with source text, analysis assets, outlines, settings, character state, and continuation context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update persistent project files and analysis assets in the target directory. <br>
Mitigation: Invoke it explicitly for fiction-import tasks and review the target directory before allowing file changes. <br>
Risk: Imported manuscript analysis may produce incorrect project structure, character state, or continuation context. <br>
Mitigation: Review the generated writing project, especially outlines, tracking files, and source-text placement, before using it for continuation work. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-import) <br>
- [Publisher Profile](https://clawhub.ai/user/worldwonderer) <br>
- [OpenClaw Source Metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Length Routing Rules](artifact/references/length-routing.md) <br>
- [Long-Form Structure Mapping](artifact/references/structure-mapping-long.md) <br>
- [Short-Form Structure Mapping](artifact/references/structure-mapping-short.md) <br>
- [State Tracking Protocol](artifact/references/state-tracking.md) <br>
- [Character State Reverse Rules](artifact/references/character-state-reverse.md) <br>
- [Format and Structure Reference](artifact/references/format-and-structure.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file and directory specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates persistent writing-project files and analysis assets based on user-provided manuscript text.] <br>

## Skill Version(s): <br>
1.0.13 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
