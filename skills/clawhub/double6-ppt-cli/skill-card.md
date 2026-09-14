## Description:

Double6 PPT CLI helps agents create, fill, inspect, verify, and narrowly repair native editable PPTX decks from Markdown, structured content, templates, and local authorized images while preserving stable object identity for iterative edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[double6-ai](https://clawhub.ai/user/double6-ai)

### License/Terms of Use:

Apache License 2.0

## Use Case:

Developers and presentation-building agents use this skill to author, template-fill, inspect, verify, and apply bounded repairs to editable PPTX decks. It is suited for workflows that need native PowerPoint objects, stable object identities, package diffs, verification receipts, and explicit visual review or waiver.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a suspicious verdict because the skill can create local run artifacts, invoke OfficeCLI, LibreOffice, or PowerPoint automation, and bootstrap an npm dependency.

Mitigation: Install and run it in a constrained workspace, review OfficeCLI package source and integrity before bootstrap, and bootstrap only with explicit user authorization.

Risk: Vendored PPT Master content includes a nested SKILL.md that could be mistaken for a separate active skill.

Mitigation: Treat the vendored nested PPT Master skill file as dependency evidence only unless the user intentionally wants those broader upstream workflows.

Risk: Native verification depends on macOS PowerPoint automation, while portable verification does not complete a PowerPoint roundtrip.

Mitigation: Use the native tier when macOS PowerPoint and automation permissions are available; use the portable tier only with clear delivery statements and visual review or a user-approved waiver.

## Reference(s):

- [Double6 PPT CLI homepage](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-ppt-cli)
- [PPT Master upstream](https://github.com/hugohe3/ppt-master)
- [OfficeCLI upstream](https://github.com/iOfficeAI/OfficeCLI)
- [Authoring contract](references/authoring-contract.md)
- [Delivery gates](references/delivery-gates.md)
- [Repair policy](references/repair-policy.md)
- [Machine contracts](references/machine-contracts.md)
- [Verification tiers and test report](references/test-report-and-verification-tiers.md)
- [Licenses and upstreams](references/licenses-and-upstreams.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON receipts, and PPTX workflow artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local run directories, inspection maps, package diffs, render manifests, verification receipts, and delivery manifests.]

## Skill Version(s):

0.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
