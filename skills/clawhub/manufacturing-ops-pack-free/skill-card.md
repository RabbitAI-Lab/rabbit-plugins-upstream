## Description:

A local checker for Chinese manufacturing and production worksheets that runs 14 consistency checks per object directory and reports one conclusion line per object with source file and line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Manufacturing cost accountants, production statisticians, workshop accounting staff, and finance managers use this skill during monthly closing, production report review, inventory and fixed asset checks, subcontract settlement, outsourced processing review, and certificate renewal tracking. It helps them identify arithmetic and consistency issues in exported worksheet text, with source line references for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may overread arithmetic and consistency findings as audit, legal, compliance, or business approval conclusions.

Mitigation: Treat the output as worksheet checking support only, and route audit opinions, payment decisions, compliance judgments, and business approvals through the appropriate qualified reviewers.

Risk: The checker reads files from user-selected local input paths.

Mitigation: Run it only against directories and files intended for review, and avoid pointing it at unrelated or sensitive folders.

Risk: Incomplete, malformed, or partially covered materials can leave checks unexecuted.

Mitigation: Provide one object per directory with recognizable Chinese table headers or section markers, and treat insufficient input or unexecuted checks as no conclusion rather than a pass.

Risk: The workflow and outputs are Chinese-language manufacturing/accounting materials.

Mitigation: Confirm that reviewers can interpret the Chinese headers and findings, or involve domain staff who can validate the worksheet context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/manufacturing-ops-pack-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or machine-readable JSON, with per-object conclusions and source file line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local manufacturing worksheet consistency results; insufficient or partial input is reported as not run rather than treated as a pass.]

## Skill Version(s):

1.0.21 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
