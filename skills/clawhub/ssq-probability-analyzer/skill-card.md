## Description:

双色球一站看 aggregates public Double Color Ball expert views, generates entertainment-only number combinations, checks draw results, and calculates Dantuo savings while emphasizing that lottery selections do not beat random chance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to produce entertainment-only Double Color Ball analysis, number-selection reports, draw checks, and responsible-play guidance. It is not a betting, investment, or guaranteed-outcome tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run Python scripts, fetch public web data, and write generated reports to a desktop or other cross-profile path.

Mitigation: Review generated files and prefer manual `python run_ssq.py` execution; use the documented offline mode when network fetching is not desired.

Risk: Included Windows registration helpers may create recurring SYSTEM scheduled tasks.

Mitigation: Use scheduled-task helpers only when recurring automation is explicitly wanted, and inspect or disable Windows scheduled tasks after installation.

Risk: The skill inspects WorkBuddy automation state and includes background automation behavior beyond a simple on-demand analyzer.

Mitigation: Review WorkBuddy automation state before enabling recurring use, and keep unwanted automation disabled.

Risk: Lottery analysis can be misunderstood as predictive or financial advice.

Mitigation: Keep the entertainment-only, no-guarantee, and responsible-play warnings visible in user-facing outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hmily741963/skills/ssq-probability-analyzer)
- [README](README.md)
- [Changelog](CHANGELOG.md)
- [FAQ](references/faq.md)
- [Methodology](references/methodology.md)
- [Responsible Play Guide](references/responsible_play_2026.md)
- [Operations Guide](references/operations.md)
- [Scripts Index](references/scripts.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with generated HTML and JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are entertainment-only and may include draw checks, public-data summaries, self-check status, and responsible-play warnings.]

## Skill Version(s):

2.1.36 (source: frontmatter, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
