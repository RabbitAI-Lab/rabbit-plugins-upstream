## Description:

Analyzes post-feeding aquarium or smart-feeder videos to estimate fish gathering, feeding intensity, remaining feed, and a 0-100 feeding activity score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarium keepers, aquaculture operators, and developers use this skill to analyze post-feeding camera footage, generate structured feeding activity reports, view account-linked report history, and surface appetite-decline alerts without making disease diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload aquarium media or forward media URLs to configured network services.

Mitigation: Use only footage and URLs approved for that service, and avoid private camera URLs, signed links, or sensitive footage unless the service and retention practices are trusted.

Risk: The skill silently creates or reuses an internal identity and queries account-linked report history.

Mitigation: Run it only in workspaces where that account association is expected, and review history output before sharing it outside the intended user context.

Risk: The skill stores service tokens in the workspace.

Mitigation: Keep the workspace access-controlled, rotate credentials after shared or untrusted use, and remove stored tokens when the skill is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Fish feeding activity API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON structured analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a caller-provided output file and can return account-linked history from the configured cloud service.]

## Skill Version(s):

1.0.12 (source: server release metadata; SKILL.md frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
