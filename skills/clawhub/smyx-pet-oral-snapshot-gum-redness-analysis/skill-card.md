## Description:

Analyzes pet oral snapshot images or videos through server-side APIs to report visible gum color, gum redness level, tartar coverage, oral-health risk observations, and report links without providing disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, pet-camera products, smart pet devices, and pet health platforms use this skill to submit pet oral images, videos, or URLs for cloud analysis and retrieve structured oral-health observations or history reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report history are sent to lifeemergence.com services for cloud analysis.

Mitigation: Use only media and URLs appropriate for third-party cloud processing, avoid private household media or internal/private URLs, and use a test workspace or dedicated account when evaluating the skill.

Risk: The skill can silently create or reuse an account identity and store API tokens in the workspace data directory.

Mitigation: Install only in workspaces where this identity and token behavior is acceptable, and review or rotate stored credentials according to local policy.

Risk: The scanner verdict is suspicious and the skill can retrieve cloud report history.

Mitigation: Review the skill before installation and limit use to accounts and report data intended for this service.

Risk: Oral-health outputs are observations rather than veterinary diagnoses.

Mitigation: Treat results as care reference information and seek veterinary review for medical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown summaries and JSON-style structured analysis results, with optional shell commands for running analysis or listing cloud reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud-backed results may include oral-health observations, risk notes, suggestions, and report links; detailed output can be saved to a file.]

## Skill Version(s):

1.0.14 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
