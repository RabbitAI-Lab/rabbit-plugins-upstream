## Description:

Use this skill when a research task's final presentation format is unknown; it compares research reports, academic papers, table-first reports, decision memos, and custom formats, then supports the recommendation with authoritative standards and real examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and research agents use this skill before research planning to select and justify an appropriate final presentation format, such as a research report, academic paper, table-first report, decision memo, timeline, FAQ, or custom form. It records structure preference strength and writes a format proposal for user confirmation before downstream report planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend a presentation format based on source choices or examples that do not fit the user's actual research task.

Mitigation: Review the generated format_proposal.json, including cited sources and rationale, before confirming the format for downstream planning.

Risk: The skill performs web or academic source searches, so weak or non-primary sources could affect the proposal if validation is not checked.

Mitigation: Confirm that the proposal uses validated primary guidelines or real examples and that any fallback reason is acceptable for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-report-format-discovery)

## Skill Output:

**Output Type(s):** [guidance, JSON]

**Output Format:** [JSON file with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces format_proposal.json in the report directory for user confirmation before formal research planning.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
