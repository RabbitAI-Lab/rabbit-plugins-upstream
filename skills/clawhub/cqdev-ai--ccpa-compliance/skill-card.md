## Description: <br>
CCPA Compliance helps teams perform local CCPA/CPRA self-checks, assess consumer rights and opt-out workflows, and generate compliance reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Compliance, privacy, and engineering teams use this skill to run local CCPA/CPRA readiness checks, review consumer-rights and opt-out controls, and draft initial compliance report artifacts. It is an aid for internal assessment and documentation, not a substitute for legal advice. <br>

### Deployment Geography for Use: <br>
United States (California-focused) <br>

## Known Risks and Mitigations: <br>
Risk: Users may over-rely on generated compliance reports as legal advice. <br>
Mitigation: Use outputs as internal assessment aids and have qualified counsel review material CCPA/CPRA decisions. <br>
Risk: Optional pandas and jinja2 dependencies may introduce dependency risk if installed without review. <br>
Mitigation: Pin and audit optional dependencies before installing them in a managed environment. <br>
Risk: Reports are written to the path supplied through --output. <br>
Mitigation: Review output paths before execution and avoid writing reports to sensitive or shared locations unintentionally. <br>
Risk: Some documentation references outdated or missing scripts and versions. <br>
Mitigation: Verify commands against the files present in the artifact before running them. <br>


## Reference(s): <br>
- [CCPA/CPRA Reference Summary](references/ccpa-law.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/cqdev-ai/skills/ccpa-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, code, shell commands, configuration, guidance] <br>
**Output Format:** [CLI reports and generated documents in text, JSON, Markdown, HTML, or CSV.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally; reports may be printed to stdout or written to a user-specified output path.] <br>

## Skill Version(s): <br>
1.1.0 (source: changelog and package.json, released 2026-07-19) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
