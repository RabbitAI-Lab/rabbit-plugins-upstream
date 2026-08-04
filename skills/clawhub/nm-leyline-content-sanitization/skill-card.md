## Description: <br>
Provides sanitization guidelines for external content in skills and hooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to decide when external content needs sanitization and to apply checklist-based protections before using untrusted web, GitHub, or user-provided content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may assume automated sanitization is active when only this guideline skill is installed. <br>
Mitigation: Confirm the separate plugin hook is installed for automated enforcement; otherwise apply the sanitization checklist manually. <br>
Risk: Workflows that fetch public web or GitHub content can ingest prompt-injection text, hidden formatting, or unsafe code-execution patterns. <br>
Mitigation: Review those workflows and apply truncation, boundary markers, instruction stripping, hidden-text stripping, and code-execution prevention before using external content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-content-sanitization) <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown] <br>
**Output Format:** [Markdown guidance with checklist steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code is included in the artifact; automated-hook behavior requires a separate plugin hook installation.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
