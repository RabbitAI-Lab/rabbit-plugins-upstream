## Description: <br>
Generates or updates tutorials from VHS tapes and Playwright specs with dual-tone markdown and GIF recording. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to refresh user-facing tutorials, validate VHS and Playwright tutorial assets, record GIF demos, and generate concise project docs plus deeper book-style markdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run project-supplied commands from tape files and manifest prerequisites. <br>
Mitigation: Use it only on repositories you trust, review tape files and manifest requires commands before execution, and avoid skip-validation options on unfamiliar content. <br>
Risk: The skill can rebuild or install binaries such as cargo or make targets before recording tutorials. <br>
Mitigation: Confirm build and install commands before allowing the agent to run them, especially when dependencies or generated binaries changed. <br>
Risk: The skill can edit top-level documentation such as README.md and book/src/SUMMARY.md. <br>
Mitigation: Review documentation diffs before accepting changes so generated tutorials do not introduce misleading or stale guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-tutorial-updates) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Manifest Parsing Module](artifact/modules/manifest-parsing.md) <br>
- [Markdown Generation Module](artifact/modules/markdown-generation.md) <br>
- [Tape Validation Module](artifact/modules/tape-validation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated tutorial asset paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update tutorial markdown, README demo sections, mdBook summaries, and GIF recording assets.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
