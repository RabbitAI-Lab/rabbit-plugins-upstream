## Description: <br>
Applies NIST/CWE security hardening to Python and Rust code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security engineers use this skill to audit repositories for Python, Rust, supply-chain, CI/CD, container, and frontier security hardening gaps. It produces citation-backed findings and concrete remediation proposals for user approval, filing, deferral, or rejection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad security-hardening audits may trigger from generic Python, Rust, or security language and produce noisy findings. <br>
Mitigation: Review findings and proposals before acting, and use the report-only and approval-gate workflow to decide whether to apply, file, defer, or reject each item. <br>
Risk: Approved fixes can modify source code, CI configuration, dependency policy, or container settings. <br>
Mitigation: Apply changes as discrete, reviewable units, rerun project gates after each change, and revert any change that fails validation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-harden) <br>
- [Source Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [NIST and CWE Citation Backbone](modules/nist-controls.md) <br>
- [Python Hardening Checks](modules/python-checks.md) <br>
- [Rust Hardening Checks](modules/rust-checks.md) <br>
- [Cross-Cutting Hardening Checks](modules/cross-cutting.md) <br>
- [Frontier Hardening Checks](modules/frontier-checks.md) <br>
- [Proposal Shape](modules/proposal-shape.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with findings tables, remediation proposals, diff snippets, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [First run is report-only; applying remediations requires user approval or an explicit auto-apply flag.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
