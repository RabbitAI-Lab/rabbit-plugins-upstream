## Description:

Generates PatentMax technology-roadmap and patent-portfolio guidance for comparing R&D routes, planning filings, designing around competitor patents, and aligning application timing with business constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, patent teams, and business users use this skill to collect roadmap constraints, create PatentMax analysis tasks, monitor progress, and turn results into route comparisons, filing plans, disclosure-timed schedules, and patent risk summaries. The output is technical and business guidance, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential patent-roadmap materials and business constraints may be sent to PatentMax or to a configured base URL.

Mitigation: Use sanitized summaries when possible and avoid setting PATENTMAX_BASE_URL unless the endpoint is trusted and approved.

Risk: PATENTMAX_API_KEY is required for live use and could expose account access if mishandled.

Mitigation: Store the key as a secret, avoid committing or logging it, and rotate it if exposure is suspected.

Risk: The create workflow can incur charges for paid PatentMax analysis tasks.

Mitigation: Confirm cost and user consent before using --yes, and use idempotency and status checks instead of duplicate submissions.

Risk: Patent roadmap outputs may be mistaken for legal conclusions.

Mitigation: Treat outputs as technical and business guidance; obtain patent-agent or attorney review for infringement, patentability, claim drafting, and freedom-to-operate decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ip930/skills/patentmax-roadmap)
- [Publisher profile](https://clawhub.ai/user/ip930)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API console](https://api.ip930.com)
- [Context guide](references/context-guide.md)
- [Workflow guide](references/workflow.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI subcommands return JSON and can download a DOCX report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PATENTMAX_API_KEY; sends submitted patent-roadmap materials and business constraints to PatentMax; paid create tasks require explicit --yes confirmation.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
