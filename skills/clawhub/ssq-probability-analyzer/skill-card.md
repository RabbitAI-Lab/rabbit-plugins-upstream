## Description:

双色球一站看 helps agents generate entertainment-only Double Color Ball lottery reports with public expert-view summaries, random pick ideas, draw-result checks, and responsible-play warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to produce lottery analysis reports, entertainment pick combinations, draw-result checks, and explanations of why lottery picks do not improve expected returns. It is also used to run local health checks around the report-generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs Python scripts that access the network and write local reports.

Mitigation: Run it in an isolated environment or with explicit current-user output paths, and review generated files before relying on them.

Risk: The skill describes privileged background automation and local profile inspection beyond what a lottery-report tool normally needs.

Mitigation: Avoid administrator privileges and do not install or follow SYSTEM scheduled-task setup on shared machines.

Risk: Lottery analysis can be misunderstood as improving expected returns.

Mitigation: Keep responsible-play warnings in outputs and present all picks as entertainment-only with no improved odds or profit expectation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/ssq-probability-analyzer)
- [FAQ](references/faq.md)
- [Methodology](references/methodology.md)
- [Operations](references/operations.md)
- [Responsible Play 2026](references/responsible_play_2026.md)
- [Scripts Reference](references/scripts.md)
- [SSQ Web Research 2026](references/web_research_ssq_2026.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python shell commands and generated local report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are entertainment-only and should include responsible-play warnings.]

## Skill Version(s):

2.1.51 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
