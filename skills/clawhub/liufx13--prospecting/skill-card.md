## Description:

B2B manufacturing proactive prospecting: search Google Maps for potential customers based on existing client profiles, enrich leads with business details, score and rank them, and output actionable CSV and JSON lead lists with custom sales openers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liufx13](https://clawhub.ai/user/liufx13)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business development users use this skill to turn known B2B customers into search profiles, find similar businesses in selected geographies, rank prospects, and prepare call-ready lead files. It is intended for public business information and B2B outreach workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically broaden lead collection beyond the initial search plan.

Mitigation: Set explicit geography, keyword, and result limits before execution, and review coverage reports before using the generated lead list.

Risk: Generated call lists may be used in jurisdictions or channels with B2B outreach, opt-out, or data-source restrictions.

Mitigation: Verify source terms, telemarketing rules, anti-spam requirements, and opt-out lists before outreach.

Risk: Prospect files can contain business contact data that should not be retained longer than needed.

Mitigation: Delete or archive prospect batches when a campaign ends, restrict access to authorized users, and move completed batches to encrypted storage when required.

Risk: Cross-session learning may retain prospecting knowledge beyond the current task.

Mitigation: Disable or monitor global memory updates unless persistent prospecting learnings are intended.

## Reference(s):

- [Customer Profiling](references/profiling.md)
- [Search Strategy Framework](references/search-strategy.md)
- [Google Maps Batch Search](references/maps-search.md)
- [Chain Store Prospecting Strategy](references/chain-strategy.md)
- [Data Integrity Checklist](references/data-integrity-checklist.md)
- [Coverage Report Format](references/coverage-report.md)
- [Post-Session Review](references/post-session-review.md)
- [ClawHub Skill Page](https://clawhub.ai/liufx13/skills/prospecting)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, Guidance]

**Output Format:** [Markdown guidance with generated JSON prospect records and CSV call lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prospect batches are written under prospect-data/{batch}/ with index, per-prospect records, call-list CSV, and coverage reporting when executed.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 2.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
