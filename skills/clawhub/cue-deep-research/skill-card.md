## Description:

Cue Deep Research submits public-information research questions to the Cue service to produce sourced, cross-validated Markdown reports across financial, corporate, legal, regulatory, research, fund-flow, and bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to request public-market, company, industry, competitor, regulatory, and compliance research from Cue and receive a sourced Markdown report. The skill is also used to mimic a reference writing style when the user provides a URL or approved local document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill asks users to run an unpinned external Python runner.

Mitigation: Pin and review a specific cue-skills commit before installing or executing the runner.

Risk: The artifact behavior supports uploading a local document when mimic-file is used.

Mitigation: Do not use mimic-file with sensitive, confidential, regulated, personal, or proprietary documents.

Risk: The security guidance notes that Cue share links and credit, referral, or payment guidance may appear in responses.

Mitigation: Review generated reports and outbound links before sharing them in commercial workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-deep-research)
- [Cue Runner Source](https://github.com/sensedeal/cue-skills)
- [Cue Runner Gitee Mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with source links and supporting command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research runs write a local Markdown report and may include a Cue share link when an actual conversation id is returned.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
