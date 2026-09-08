## Description:

Builds targeted journalist and media contact lists from Twitter/X using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

PR agencies, startup communications teams, founders, and other external users use this skill to identify journalists and media contacts on Twitter/X for a beat, industry, publication set, or story pitch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search terms and selected Twitter/X usernames to Apify and requires an APIFY_TOKEN.

Mitigation: Keep the Apify token private, avoid sharing commands that expose sensitive URLs or parameters, and review the searched terms before execution.

Risk: Journalist discovery may be biased toward English-language or US-centric Twitter/X results when default search settings are used.

Mitigation: Adjust language and geography settings for the target media market, and spot-check selected contacts before outreach.

Risk: Profile information, follower counts, and recent coverage topics may be stale or incomplete.

Mitigation: Verify priority contacts directly on Twitter/X or through recent published work before using the list for outreach.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/building-journalist-outreach-list-from-twitter)
- [apidojo profile](https://clawhub.ai/user/apidojo-io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, grouped contact lists, pitch notes, and inline shell or API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an APIFY_TOKEN when executing Apify actors; output may include profile-derived journalist names, handles, publication affiliations, follower counts, and recent coverage topics.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
