## Description:

Collects and analyzes public Kuaishou video, creator-post, and comment data for competitor research, content topic discovery, KOL screening, sentiment review, and trend insight workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketers, MCNs, business analysts, and developers use this skill to collect public Kuaishou data and turn it into structured inputs for competitor monitoring, topic research, KOL discovery, comment analysis, and downstream reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends queried keywords or Kuaishou URLs to guaikei.com as a third-party Kuaishou data provider.

Mitigation: Use the skill only with public, non-sensitive targets after confirming data sharing and authorization requirements for the deployment.

Risk: The skill requires a GUAIKEI_API_TOKEN for access to the third-party API.

Mitigation: Configure a dedicated token through environment variables and rotate or revoke it according to the user's credential policy.

Risk: The evidence reports no packaged executable code, so referenced scripts may need to be supplied elsewhere before the skill can run as described.

Mitigation: Verify that the runtime environment includes the referenced Kuaishou command scripts before relying on operational behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/kuaishou-skill-20260901)
- [Guaikei](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results or error summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14.0+; successful calls return status-bearing JSON for search results, creator posts, comments, and analytics.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
