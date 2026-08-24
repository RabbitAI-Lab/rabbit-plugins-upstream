## Description:

Analyzes snake mouth images or videos for visual indicators of stomatitis risk, including mucosal color changes, pus points, ulcers, necrotic tissue, image quality, and relevant husbandry context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External snake keepers, reptile veterinary teams, breeding facilities, and developers can use this skill to screen uploaded snake mouth images or videos, produce structured visual risk reports, and review cloud-stored analysis history. The output is visual screening support and should not be treated as a veterinary diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images or videos are sent to remote cloud analysis services, and historical analysis is queried from cloud APIs.

Mitigation: Use only media appropriate for remote processing, review configured service endpoints before deployment, and avoid sensitive media unless this data flow is acceptable.

Risk: The skill may silently create or reuse an identity and store authentication tokens in the workspace data directory.

Mitigation: Run the skill in a controlled workspace, restrict access to local workspace data, and clear stored tokens when they are no longer needed.

Risk: Visual screening output could be mistaken for veterinary diagnosis or treatment guidance.

Mitigation: Use the output as visual triage support only and route urgent or repeated high-risk findings to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Usage Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and optional JSON or plain-text CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk levels, visual findings, suggested next actions, report links, and historical report tables; analysis relies on remote cloud services.]

## Skill Version(s):

1.0.10 (source: evidence.release.version and target metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
