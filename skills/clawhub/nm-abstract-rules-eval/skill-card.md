## Description: <br>
Evaluate Claude Code rules in .claude/rules/. Use for frontmatter, globs, and quality audits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit Claude Code rule files for frontmatter validity, glob pattern quality, content clarity, organization, token efficiency, and redundancy before adopting or publishing rule sets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic triggers may cause this skill to appear for unrelated conversations about rules or validation. <br>
Mitigation: Use it only when intentionally reviewing Claude Code rule files. <br>
Risk: The skill references a larger external plugin experience that is outside the bundled artifact. <br>
Mitigation: Inspect that external plugin separately before installing or relying on it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-rules-eval) <br>
- [Publisher Profile](https://clawhub.ai/user/athola) <br>
- [Night Market Abstract Plugin](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown with structured audit findings and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports rule quality scores, validation issues, and concrete recommendations.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
