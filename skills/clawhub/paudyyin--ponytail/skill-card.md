## Description: <br>
Ponytail pushes a coding agent toward the simplest working solution by favoring YAGNI, existing code, standard libraries, native platform features, and minimal diffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use Ponytail to keep implementation work small and pragmatic, emphasizing existing patterns, standard-library/native features, and the shortest working change for coding tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The minimalist coding posture can be a poor fit for deeper design analysis, compliance review, broad architecture work, or intentionally fuller explanations. <br>
Mitigation: Disable the mode with "stop ponytail" or "normal mode" when those tasks need broader analysis. <br>
Risk: Over-minimizing an implementation could undercut required validation, error handling, security measures, accessibility basics, or explicitly requested scope. <br>
Mitigation: Keep those safeguards in scope and use the skill's own boundary guidance that these areas must not be simplified away. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/ponytail) <br>
- [Project homepage](https://github.com/DietrichGebert/ponytail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, code snippets, shell commands, and concise implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Persistent style-mode guidance with lite, full, and ultra intensity modes; no executable artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
