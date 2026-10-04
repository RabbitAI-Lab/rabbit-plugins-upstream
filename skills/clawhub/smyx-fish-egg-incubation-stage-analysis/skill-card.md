## Description:

Analyzes fish-egg images or videos to identify incubation stages and suggest breeding actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Fish breeders and hatchery operators use this skill to assess egg development from images or videos, review incubation history, and plan timely fry care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish-egg media and report-history requests are sent to lifeemergence.com services.

Mitigation: Use only with media you are authorized to share and review the service's data handling before uploading.

Risk: The skill creates or reuses a local identity database that may retain authentication tokens and link reports across sessions.

Mitigation: Run in an isolated workspace and review or delete local data files when persistent identity linkage is unwanted.

Risk: A runtime import-path weakness warrants manual review before installation.

Mitigation: Inspect the installed code and avoid shared temporary installation paths.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-egg-incubation-stage-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON analysis reports or Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incubation stage, observations, suggested actions, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.7 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
