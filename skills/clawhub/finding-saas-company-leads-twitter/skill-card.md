## Description:

Finds SaaS companies and software startup leads from Twitter/X using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, partnership, investment, and press teams use this skill to find and score SaaS company leads on Twitter/X by vertical, activity, follower count, and profile signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Twitter/X search terms, handles, and derived lead data are sent to Apify.

Mitigation: Use the skill only when sharing those inputs and outputs with Apify is acceptable for the use case.

Risk: Broad follower, following, retweeter, or unlimited item extraction can collect more social data than needed.

Mitigation: Set maxItems deliberately and enable follower, following, or retweeter extraction only when specifically required.

Risk: Custom JavaScript mapping can alter or expose collected output.

Mitigation: Use only trusted customMapFunction code and review generated CSV or JSON outputs before sharing or storing them.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, inline commands, and optional CSV or JSON file output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Apify token when executing Apify actors; results may include Twitter/X handles, profile details, product descriptions, recent tweets, lead scores, and stage classifications.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
