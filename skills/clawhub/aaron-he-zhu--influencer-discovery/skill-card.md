## Description:

Finds influencer candidates across platforms, screens for audience fit and authenticity red flags, and produces a tiered shortlist for downstream scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and agent operators use this skill to build influencer rosters from a niche, platform, follower band, or brand goal. It returns screened candidate pools, creator profiles, authenticity red flags, and shortlist tiers for later fit scoring or outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A support file tells the agent to save creator dossiers, which can conflict with the skill contract requiring explicit approval before writes.

Mitigation: Require a clear destination and separate user approval before writing any report, dossier, cache entry, CSV, CRM import, or registry proposal.

Risk: Influencer discovery can collect creator contact details and profile data.

Mitigation: Use only public business contact paths or user-supplied data, mark unconfirmed gaps plainly, and do not guess private contact details.

Risk: Candidate quality and authenticity signals may be preliminary and incomplete.

Mitigation: Treat red flags and triage scores as discovery signals only, then pass shortlisted creators to downstream fit scoring or human review before outreach.

## Reference(s):

- [Influencer Discovery on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/influencer-discovery)
- [Publisher Profile](https://clawhub.ai/user/aaron-he-zhu)
- [ClawHub Metadata Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills)
- [Creator Dossier Method](references/creator-dossier.md)
- [Platform-Specific Creator Vetting](references/platform-vetting.md)
- [Influencer Discovery Templates](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown discovery report with tables, creator profiles, shortlist tiers, and handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inline delivery by default; report saves, cache promotions, CSV or CRM exports, and registry proposals require separate explicit authorization.]

## Skill Version(s):

19.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
