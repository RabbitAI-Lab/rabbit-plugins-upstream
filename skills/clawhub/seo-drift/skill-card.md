## Description:

SEO Drift monitors user-specified pages by capturing SEO baselines, comparing later page states, and reporting regressions in critical on-page signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and site operators use this skill to establish a known-good SEO snapshot before a deployment, compare a later page state against that baseline, and inspect drift history for a URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores historical SEO snapshots locally for monitored URLs.

Mitigation: Use it only for sites you are comfortable monitoring and delete the local cache when historical SEO data should no longer be retained.

Risk: The skill may contact external page and PageSpeed services for URLs supplied by the user.

Mitigation: Run it only against URLs approved for monitoring in the user's environment.

## Reference(s):

- [SEO Drift Comparison Rules](references/comparison-rules.md)
- [ClawHub Skill Page](https://clawhub.ai/asale-ai/skills/seo-drift)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local SEO baseline, comparison, and history records for user-provided URLs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
