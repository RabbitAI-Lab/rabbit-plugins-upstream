## Description:

LinkFox Amazon Ads helps agents handle Amazon Ads authorization, SP/SB/SD campaign management, and end-to-end advertising report retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon Ads operators and commerce teams use this skill to authorize ad accounts, inspect or change SP/SB/SD advertising entities, and retrieve structured performance reports. It is suited for workflows that need token handling, campaign metadata operations, or report downloads through LinkFox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform create and update actions that may affect Amazon Ads spend.

Mitigation: Review every create or update action before execution and keep the skill limited to trusted operators.

Risk: The skill handles Amazon Ads API keys, OAuth tokens, report files, stdout logs, and clipboard authorization URLs.

Mitigation: Use a single-user workspace, treat generated LinkFox data directories and temporary report files as sensitive, and delete report or export files when finished.

Risk: Credential-bearing requests can be redirected if endpoint override environment variables are changed.

Mitigation: Keep endpoint override variables unset or restrict them to trusted LinkFox HTTPS hosts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads)
- [Amazon Ads Authorization Reference](references/linkfox-amazon-ads-auth.md)
- [Amazon Ads Management Reference](references/linkfox-amazon-ads-manager.md)
- [Amazon Ads Report Reference](references/linkfox-amazon-ads-report.md)
- [Report Types Index](references/report-types/index.md)
- [Onboarding Reference](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON inputs or outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may save full responses to local JSON files and print either full JSON or summaries depending on response size.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
