## Description: <br>
Applies NIST/CWE security hardening to Python and Rust code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit a repository for security hardening gaps, map findings to NIST SSDF and CWE references, and prepare concrete remediation proposals for approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may activate the hardening workflow outside a planned audit. <br>
Mitigation: Invoke the skill deliberately for repository audits and review its planned actions before allowing changes. <br>
Risk: Remediation proposals may modify files, create commits, open issues, or comment on pull requests. <br>
Mitigation: Require user approval for proposed actions and re-run project gates after approved changes. <br>
Risk: Security findings or fixes may be incorrect for the target repository context. <br>
Mitigation: Review each finding's citation, affected file, diff, blast radius, reversal plan, and expected test before applying it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-harden) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with findings tables, remediation proposals, diffs or configuration snippets, shell commands, and validation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file changes, commits, issue creation, or PR comments after user approval.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
