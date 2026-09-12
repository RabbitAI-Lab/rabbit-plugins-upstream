## Description:

Amazon Shopper helps agents search amazon.es anonymously, compare available listings, decode product specs, and recommend purchases by normalized value metrics such as price per kilogram or gigabyte.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to narrow an Amazon.es shopping request, ask only load-bearing follow-up questions, and recommend buyable products by the metric that matters for the category.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping queries and extracted product data may be sent to an OpenClaw gateway or a locally configured LLM CLI.

Mitigation: Use the skill only when that disclosure is acceptable, configure a trusted LLM path, and avoid entering sensitive shopping intent.

Risk: Optional off-Amazon research can broaden network access beyond Amazon.es to producer domains and DuckDuckGo.

Mitigation: Leave AMAZON_SHOPPER_ALLOW_WEB_RESEARCH unset unless that broader lookup is needed, especially on networks where internal HTTPS services are reachable.

Risk: Subprocesses may inherit unrelated environment variables and use existing CLI accounts.

Mitigation: Run the skill with a minimal environment and dedicated, least-privileged API credentials for optional Apify or Amazon Creators API paths.

## Reference(s):

- [Amazon Shopper ClawHub listing](https://clawhub.ai/globalcaos/skills/tinker-amazon-shopper)
- [TinkerClaw repository](https://github.com/globalcaos/tinkerclaw)
- [Apify integrations settings](https://console.apify.com/settings/integrations)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI subcommands emit one JSON object on stdout; recommendations include ranked products, pricing metrics, availability state, and skipped items when specifications cannot be resolved.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
