## Description: <br>
Story Import turns an existing Chinese-language novel or short story into a structured writing project that can be continued with related story-writing skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and writing-workflow agents use this skill to import an existing manuscript, analyze it by length, and rebuild it as a long-form or short-form project with settings, outlines, tracking files, benchmark references, and continuation-ready context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can copy, create, or overwrite manuscript-derived project files in local writing-project directories. <br>
Mitigation: Invoke it explicitly, point it only at intended manuscript sources, and review overwrite notices and generated files before continuing the writing workflow. <br>
Risk: Importing a directory that contains unrelated private material could expose that material to the analysis workflow. <br>
Mitigation: Use a dedicated manuscript file or clean project directory, and avoid selecting folders that contain unrelated sensitive files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-import) <br>
- [Metadata Source](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Length Routing Rules](references/length-routing.md) <br>
- [Long-Form Structure Mapping](references/structure-mapping-long.md) <br>
- [Short-Form Structure Mapping](references/structure-mapping-short.md) <br>
- [Character State Reverse Rules](references/character-state-reverse.md) <br>
- [State Tracking Protocol](references/state-tracking.md) <br>
- [Text Format and Structure Rules](references/format-and-structure.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file paths, project-structure plans, status summaries, and command-style workflow handoffs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces or updates local manuscript-derived project files under directories such as 拆文库/, the book project directory, 对标/, 追踪/, and .active-book.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
