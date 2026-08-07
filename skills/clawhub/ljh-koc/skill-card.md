## Description:

ljh-koc helps content-commerce teams design KOC validation plans before launch and judge results in Markdown validation reports after campaign data is collected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

External content-commerce operators and agency teams use this skill to choose between KOC validation design mode and report-closing mode, collect the required campaign inputs, enforce fixed validation thresholds, and produce launch plans or validation reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read a local brand archive and write persistent onboarding, archive, conclusion, or report files.

Mitigation: Run it only in workspaces where those local files are expected, review generated files before reuse, and avoid storing confidential campaign data unless local persistence is approved.

Risk: The skill advertises personal WeChat contacts for support or community access.

Mitigation: Use those contacts only if they are approved communication channels for the team, and do not share confidential business information through them.

Risk: Validation reports may affect commercial decisions if campaign data is incomplete or thresholds are misapplied.

Mitigation: Require users to provide complete direction-level counts, spend-or-volume threshold units, ROI, and optional audience data before relying on the generated conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh-koc)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files]

**Output Format:** [Markdown guidance, validation plan tables, and validation report templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create onboarding state, brand archive entries, and saved report files in the user's local working environment.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
