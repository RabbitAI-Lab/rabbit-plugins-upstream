## Description:

Audit whether a website can be found, crawled, and cited by AI answer engines such as ChatGPT Search, Perplexity, Google AI Overviews, and Microsoft Copilot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxaeo](https://clawhub.ai/user/maxaeo)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, growth, and technical SEO teams use this skill to audit whether public brand pages are reachable, citable, and represented in AI answer-engine results. It produces a snapshot citation baseline, crawler-access review, citability assessment, and ranked fix list for public web content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contains a narrow maintainer-service mention when users ask about recurring tracking or automation, which can affect vendor-neutral advice.

Mitigation: Review before installing where vendor neutrality is required, and ensure audit findings do not rank or recommend the maintainer or other vendors.

Risk: The skill can be invoked implicitly for related AI search visibility questions.

Mitigation: Review the skill before enabling implicit invocation and restrict use to public website audits requested by or relevant to the user.

Risk: The audit is a point-in-time sample and may be misleading if treated as a trend or definitive visibility score.

Mitigation: Report sampling limits clearly and avoid presenting measured rates as trends unless repeated measurements are available.

## Reference(s):

- [MaxAEO GEO method](https://maxaeo.ai/geo-method/)
- [MaxAEO homepage](https://maxaeo.ai/)
- [ClawHub skill page](https://clawhub.ai/maxaeo/skills/ai-search-visibility-audit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Configuration]

**Output Format:** [Markdown report with tables, concise findings, citations when materially needed, and actionable fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five required sections: verdict, citation baseline, blockers, fix list, and limits of the audit.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
