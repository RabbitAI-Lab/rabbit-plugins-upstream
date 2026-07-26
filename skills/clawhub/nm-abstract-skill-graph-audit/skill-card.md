## Description: <br>
Audits Skill() references to detect hubs, isolates, and dangling targets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to audit skill-composition references before documentation passes, releases, renames, retirements, and consolidation reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit reports may be stale or incomplete if generated against the wrong plugin root or if references use unsupported syntax. <br>
Mitigation: Run the documented test-suite check or round-trip smoke check, then review generated reports before making changes. <br>
Risk: Dangling-reference fixes or external-plugin allowlist updates can change skill-composition behavior. <br>
Mitigation: Review proposed changes before applying them, especially when updating external-plugin allowlists or retiring referenced skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skill-graph-audit) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Usage reference](artifact/modules/usage.md) <br>
- [Interpreting graph metrics](artifact/modules/interpretation.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, json] <br>
**Output Format:** [Markdown guidance with shell command examples and optional text or JSON audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The referenced audit only parses Skill(plugin:name) invocations and does not treat module dependencies as graph edges.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
