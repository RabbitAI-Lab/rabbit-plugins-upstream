## Description:

UI Doctor audits existing application UIs for layout and state synchronization, responsive behavior, accessibility, performance, and chat rendering issues, then fixes root causes in code with evidence-based verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose and repair already-built frontend interfaces that look inconsistent, break at specific viewport sizes, or contain layout/state-sync defects. It also supports chat and workspace UI audits by checking message rendering, markdown tables, code blocks, input controls, installed framework versions, and concrete post-fix verification evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to inspect and modify frontend project code, so an incorrect diagnosis or patch could regress UI behavior or styling.

Mitigation: Review generated code diffs and require the skill's evidence-based verification steps before accepting changes.

Risk: Version-sensitive frontend fixes can be wrong when based on stale assumptions about installed libraries.

Mitigation: Use the skill's mandatory dependency-manifest and lockfile checks, then compare the exact installed versions with current official documentation before applying fixes.

Risk: Build, browser, or dev-server cache staleness can make a valid fix appear ineffective and lead to unnecessary follow-up edits.

Mitigation: Check the relevant cache and HMR behavior for the framework before re-diagnosing a fix that appears not to have taken effect.

## Reference(s):

- [UI Doctor ClawHub Skill Page](https://clawhub.ai/anjasta-tarigan/skills/ui-doctor)
- [Audit Checklist](references/audit-checklist.md)
- [Common Bug Signatures](references/common-bug-signatures.md)
- [Conversational UI Audit](references/conversational-ui-audit.md)
- [Framework Verification](references/framework-verification.md)
- [Layout State Sync](references/layout-state-sync.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown audit reports with code diffs, shell commands, configuration changes, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect and modify frontend project files, verify installed dependency versions against current official documentation, and report concrete evidence for applied fixes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
