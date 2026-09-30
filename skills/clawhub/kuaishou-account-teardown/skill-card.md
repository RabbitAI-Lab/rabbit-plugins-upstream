## Description:

Retrieves public Kuaishou videos, creator posts, and comments to support account benchmarking and content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketing teams, and analysts use the skill to find public Kuaishou videos, compare creator posts and engagement, and examine video comments for research and planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, URLs, and request limits are sent to a third-party service using an API token.

Mitigation: Confirm that the data transfer is approved before use and protect the GUAIKEI_API_TOKEN.

Risk: Saved result logs can retain collected comments and account-analysis data.

Mitigation: Restrict access to logs and delete or retain them according to organizational policy.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-account-teardown)
- [Usage and options](references/options.md)
- [Release notes](references/changelog.md)
- [API access and support](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Structured data, Guidance]

**Output Format:** [JSON results with optional text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful results are saved locally in logs; requests require a GUAIKEI_API_TOKEN and support up to 10,000 records.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
