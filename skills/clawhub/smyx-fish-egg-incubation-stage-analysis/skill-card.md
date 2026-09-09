## Description:

This skill analyzes fish egg images or videos to identify incubation stages from egg color changes and embryonic eye-spot signals, then returns structured stage reports, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquaculture operators, ornamental fish breeders, and laboratory users use this skill to analyze fish egg macro images or videos, classify incubation progress, and review cloud-linked historical incubation reports. The skill is advisory and supports breeding-timing decisions such as preparing first foods or separating fry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-backed analysis uploads local media or passes URLs to a remote service.

Mitigation: Use only media approved for remote processing and review endpoint configuration before running the skill.

Risk: The skill silently creates or reuses an internal identity and retrieves account-linked history.

Mitigation: Use separate workspace or account contexts for different users and review report-history access before use in shared workspaces.

Risk: Service tokens are stored in a local workspace database.

Mitigation: Avoid shared workspaces for sensitive use, restrict local file access, and clear retained tokens according to local policy.

Risk: Incorrect visual classification could lead to poor breeding decisions.

Mitigation: Treat outputs as advisory and confirm unclear images, species, water temperature, and spawn-time context before acting.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-fish-egg-incubation-stage-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, Markdown tables, JSON-compatible analysis payloads, and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured incubation metrics, advisory actions, cloud report links, and optional saved output files.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
