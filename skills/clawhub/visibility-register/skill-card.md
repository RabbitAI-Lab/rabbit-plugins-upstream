## Description:

Walk one platform from the visibility catalog end to end for this project - re-check the live submission page, build the artifacts it needs, run the publish step after an explicit yes, hand the account, payment, DNS and form steps to the user, then verify the listing and update the ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orensegal](https://clawhub.ai/user/orensegal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project maintainers use this skill to prepare and manage a listing for their project on one selected platform, including identifying prerequisites, producing listing materials, and handing account or submission steps to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may reference an unpinned `npx skills` command.

Mitigation: Review the command and verify or pin the package version before executing when version reproducibility matters.

Risk: The security scan had incomplete coverage because some referenced local paths could not be resolved.

Mitigation: Review the unresolved references and relevant files before relying on the scan as a complete assessment.

## Reference(s):

- [Project homepage](https://github.com/OrenSegal/visibility)

## Skill Output:

**Output Type(s):** [Guidance, Files, Markdown, Shell commands]

**Output Format:** [Markdown guidance, checklists, and platform-specific listing artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by platform; may include generated files, listing copy, and a checklist of steps for the user.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
