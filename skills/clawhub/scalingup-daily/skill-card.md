## Description:

Generates structured Markdown daily reports on scaling trends in search, advertising, and recommendation systems, then syncs the reports to IMA and Tencent Docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fandywang87](https://clawhub.ai/user/fandywang87)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to track recent papers, articles, open source projects, and conference updates in search, advertising, and recommender-system scaling. It produces a daily Markdown digest and can publish the result to configured IMA and Tencent Docs destinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates WeChat/Sogou scraping and may encounter platform limits, anti-scraping controls, or brittle search results.

Mitigation: Install only when this collection behavior is acceptable, review generated sources before use, and verify links in the final report.

Risk: The skill can publish generated reports to IMA and Tencent Docs using stored credentials.

Mitigation: Restrict credential file permissions, avoid shared machines, and review report contents before enabling scheduled publication.

Risk: IMA upload behavior depends on helper scripts from a separate IMA skill installation.

Mitigation: Verify the IMA helper scripts come from a trusted installation before enabling upload.

## Reference(s):

- [Known papers reference](references/known_papers.md)
- [Daily report template](templates/daily_report_template.md)
- [ClawHub skill page](https://clawhub.ai/fandywang87/skills/scalingup-daily)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with cited links and optional upload commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is intended to be saved as a Markdown file and may be uploaded to IMA and Tencent Docs when credentials and integrations are configured.]

## Skill Version(s):

3.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
