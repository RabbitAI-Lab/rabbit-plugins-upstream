## Description:

Analyzes post-feeding aquarium or fish-feeder videos to estimate fish gathering, feeding intensity, remaining feed, and a 0-100 feeding activity score with appetite-decline alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquarists, aquaculture operators, and developers use this skill to submit aquarium feeding footage or URLs for structured feeding-activity reports, report links, and historical report lookup. The output should be treated as visual activity analysis, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads aquarium videos, local files, or provided URLs to a configured cloud analysis service.

Mitigation: Use only footage appropriate for cloud processing, avoid sensitive shared-space footage, and ask the publisher for retention, deletion, and reset controls before production use.

Risk: The skill can silently create or reuse a cloud identity and store access tokens locally.

Mitigation: Run it with a dedicated account or isolated workspace, review local token storage before deployment, and require clear token rotation and revocation procedures from the publisher.

Risk: The history feature can query reports linked to the automatically managed identity.

Mitigation: Limit use to accounts and workspaces where report history access is expected, and verify that users have controls for deleting or resetting report history.

Risk: Feeding activity alerts may be mistaken for veterinary diagnosis or automated device-control instructions.

Mitigation: Present results as visual activity indicators only, require human review for abnormal findings, and do not perform medication, water-change, or feeder-control actions without explicit authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a structured analysis report, feeding activity score, appetite-decline alert, recommendations, report export link, and account-linked history listing.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
