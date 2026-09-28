## Description:

Through fixed enclosure cameras, the skill analyzes reptile behavior videos to report movement frequency, dwell duration, thermal-zone preference, activity rhythm, and recommended husbandry follow-up for basking, hiding, cool, and transition zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, vivarium operators, and developers use this skill to analyze fixed-camera reptile enclosure video or media URLs and produce thermal-zone utilization reports. It supports welfare-oriented review of basking, hiding, movement frequency, activity rhythm, and non-diagnostic recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile enclosure media or media URLs may be sent to the configured cloud service.

Mitigation: Use only media you are authorized to share, review the service and retention behavior before deployment, and avoid sensitive household footage unless the cloud-processing path is approved.

Risk: The skill creates or reuses an internal identity and stores service tokens locally.

Mitigation: Run the skill in an isolated workspace, review local token storage before use, and clear workspace credentials when the skill is no longer needed.

Risk: Historical cloud reports may be queried without clear user-facing control.

Mitigation: Confirm that the operator is authorized to access historical reports and review returned report links before using them for decisions.

Risk: Behavior analysis can be mistaken for veterinary diagnosis.

Mitigation: Treat outputs as welfare and environment-review guidance only, avoid medication or disease conclusions, and consult a qualified reptile veterinarian for health concerns.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON-like structured analysis reports with command examples and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include enclosure ID, species, zone dwell ratios, movement frequency, rhythm consistency, thermal preference label, alert level, recommended actions, and disclaimers.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
