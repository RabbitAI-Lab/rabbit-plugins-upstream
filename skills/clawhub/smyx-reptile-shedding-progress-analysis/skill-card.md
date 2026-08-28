## Description:

Analyzes reptile enclosure images or videos to classify shedding phase, eye and skin signals, dysecdysis risk, and care recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers, breeders, and enclosure-monitoring developers use this skill to analyze reptile media, track shedding progress, flag image-quality or species-context issues, and produce care guidance for possible stuck shed risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media, URLs, identity data, and cloud-history requests may be sent to remote services.

Mitigation: Install and run the skill only where account-linked cloud analysis is acceptable, and avoid submitting sensitive enclosure media or private URLs unless that data sharing has been approved.

Risk: The skill may create or reuse a local account identity and persist returned tokens in a workspace SQLite database.

Mitigation: Review local credential and token storage before deployment, restrict workspace access, and remove persisted tokens when the skill is no longer needed.

Risk: Care guidance may be mistaken for veterinary diagnosis or treatment.

Mitigation: Use outputs as visual triage guidance only; require a qualified reptile veterinarian for persistent or severe dysecdysis, eye-cap, toe, or tail-tip concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis)
- [Skill API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured text or JSON report with shedding phase, risk indicators, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud history or save reports when requested.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
