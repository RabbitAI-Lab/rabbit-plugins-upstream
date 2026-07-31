## Description: <br>
Defines the contract for deferred-item capture across plugins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and plugin maintainers use this skill to define and validate deferred-capture wrapper behavior, including issue titles, source labels, duplicate checks, and JSON status output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A separate deferred-capture wrapper could create issues in an unintended repository. <br>
Mitigation: Review the wrapper target repository before use. <br>
Risk: Deferred-item context or artifact paths may include sensitive information. <br>
Mitigation: Review context text and artifact paths before allowing a wrapper to create issues. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-deferred-capture) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with CLI argument specifications and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The artifact is documentation only; conforming wrappers may emit JSON status objects for created, duplicate, or error results.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
