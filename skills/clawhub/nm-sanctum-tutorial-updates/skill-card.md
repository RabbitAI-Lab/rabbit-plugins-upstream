## Description: <br>
Generates or updates tutorials from VHS tapes and Playwright specs with dual-tone markdown and GIF recording. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation engineers use this skill to refresh user-facing tutorials by discovering tutorial manifests and tapes, validating commands, recording terminal or browser demos, and generating docs and book markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run project-defined shell commands from tapes and manifest prerequisites. <br>
Mitigation: Use it only in trusted repositories, review tape and manifest commands before execution, and keep validation enabled for untrusted content. <br>
Risk: The skill can rebuild or install CLI binaries and launch background services while preparing recordings. <br>
Mitigation: Confirm build targets and service prerequisites before recording, and run in a controlled workspace where background processes can be stopped cleanly. <br>
Risk: The skill can edit README, docs, book, and tutorial asset paths. <br>
Mitigation: Review generated file changes before committing and verify that demos and markdown match the intended release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-tutorial-updates) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Manifest Parsing Module](modules/manifest-parsing.md) <br>
- [Markdown Generation Module](modules/markdown-generation.md) <br>
- [Tape Validation Module](modules/tape-validation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands, file paths, manifest snippets, and tutorial asset instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose updates to README, docs, book, tape, manifest, and GIF asset paths.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
