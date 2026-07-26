## Description: <br>
Evaluate Claude Code rules in .claude/rules/ for frontmatter, globs, and quality audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit Claude Code rule files in .claude/rules/, including frontmatter, path globs, content quality, naming, organization, and token efficiency. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on general requests involving rules, validation, or evaluation. <br>
Mitigation: Invoke it explicitly for .claude/rules/ audits when precise scoping matters. <br>
Risk: Rule audit recommendations could be applied too broadly if the target directory is ambiguous. <br>
Mitigation: Provide the intended .claude/rules/ path or a specific rules directory when requesting an audit. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-rules-eval) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Frontmatter Validation](modules/frontmatter-validation.md) <br>
- [Glob Pattern Analysis](modules/glob-pattern-analysis.md) <br>
- [Content Quality Metrics](modules/content-quality-metrics.md) <br>
- [Organization Patterns](modules/organization-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown analysis with scores and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include rule quality scores by category and remediation guidance.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence; artifact frontmatter is 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
