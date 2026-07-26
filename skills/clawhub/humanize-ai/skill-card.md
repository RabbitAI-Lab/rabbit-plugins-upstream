## Description: <br>
Humanize AI content by detecting common AI writing patterns, reporting them, and optionally rewriting selected text with local Python scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[artur-zhdan](https://clawhub.ai/user/artur-zhdan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, writers, and content reviewers use this skill to scan documents for AI-style wording and apply local cleanup passes before manual review. It is intended for user-selected text files or stdin, including batch workflows where diffs can be reviewed afterward. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can rewrite selected text files, so automated replacements may remove nuance or change meaning. <br>
Mitigation: Run it on copies or version-controlled files first, then review diffs before keeping rewritten text. <br>
Risk: Batch commands over broad globs can modify many files at once. <br>
Mitigation: Start with analysis-only runs, limit globs to intended folders, and inspect outputs before replacing originals. <br>
Risk: The detector-bypass framing may conflict with school, workplace, publisher, or platform rules for AI-assisted writing disclosure. <br>
Mitigation: Use only where permitted and follow applicable disclosure and authorship policies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/artur-zhdan/skills/humanize-ai) <br>
- [Publisher Profile](https://clawhub.ai/user/artur-zhdan) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text reports, optional JSON analysis, shell command examples, and rewritten text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads stdin or user-selected text files; humanize.py can write rewritten output to a specified file.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
