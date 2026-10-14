## Description:

Helps agents find TikTok creators by region, audience size, engagement, product category, language, and other filters using Qinghu's creator database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and agents use this skill to shortlist TikTok creators for outreach by geography, follower count, engagement, and product category.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or upgrade qhkit, npm, or Node and make persistent changes to the host.

Mitigation: Prefer a preinstalled, pinned qhkit version and obtain approval before installing packages or changing PATH.

Risk: Configuring the Qinghu API token may store a credential on the host.

Mitigation: Obtain approval before storing the token and keep it out of shared output.

Risk: External creator lookups can incur Qinghu credit charges that increase with result volume.

Mitigation: Check the current estimate, explain potential charges, and obtain consent before paid calls or large batches.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-tiktok-creator-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Brief creator shortlist with optional tabular export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include site, date range, sample size, and Qinghu credit usage.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
