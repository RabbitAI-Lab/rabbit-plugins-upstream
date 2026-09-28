## Description:

Merges an account revision using supplied field guidance and records the local result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account-maintenance users and developers use this skill to merge an account revision into a local record according to supplied field guidance and inspect the resulting changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merged account details can be written to a local JSON receipt.

Mitigation: Choose a dedicated output directory and avoid sensitive account data unless local storage of the receipt is acceptable.

## Reference(s):

- [Account Merge Workbench on ClawHub](https://clawhub.ai/wxt-ai/skills/revision-handling-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local JSON receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the merged record, changed and preserved fields, and a receipt in the selected output directory.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
