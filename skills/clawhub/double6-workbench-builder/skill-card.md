## Description:

Builds offline-first, single-file local personal workbenches for repeated real-world tasks while keeping personal data on the current device.

This skill is ready for commercial/non-commercial use.

## Publisher:

[double6-ai](https://clawhub.ai/user/double6-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to turn a clarified recurring personal workflow, study plan, task panel, record log, or review process into a local offline workbench. It guides intake, proposal, build, preflight, browser evaluation, and delivery of a single offline HTML file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates files under a local run directory and can launch a local browser for evaluation.

Mitigation: Run it in a trusted workspace, review generated files before use, and point browser-related environment variables only to trusted local binaries.

Risk: Workbench content may involve personal, child, student, customer, financial, medical, or health-related data.

Mitigation: Use synthetic or redacted data by default, enter real data only with authorization and acceptance of local-only storage, and use the built-in export and clear controls.

Risk: Generated workbenches could be mistaken for connected services or external automation.

Mitigation: Keep account actions, networking, collaboration, payments, orders, messaging, and public publishing as manual handoffs or unsupported flows unless a separate authorized host process handles them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/double6-ai/skills/double6-workbench-builder)
- [Clawdis Homepage](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-workbench-builder)
- [Runtime Contract](references/runtime-contract.md)
- [Host Integration Playbook](references/host-integration-playbook.md)
- [Product Schema](references/product.schema.json)
- [Risk Packs](references/risk-packs.json)
- [Education Rules](references/education-rules.md)
- [Personal Life Content Sources](references/personal-life-content-sources.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON contracts, shell commands, and generated single-file HTML artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local run files and a single offline index.html candidate; browser evaluation may use a trusted local Chromium binary.]

## Skill Version(s):

0.41.0 (source: frontmatter, manifest, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
