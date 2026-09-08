## Description:

Finds professionals currently employed at startups for recruiting using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, HR teams, and startup talent leads use this skill to discover, enrich, filter, and prioritize potential startup candidates from Twitter/X profile and tweet signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill profiles identifiable social-media users for recruiting and may create employment, privacy, platform, or vendor-approval risk.

Mitigation: Review against applicable recruiting and privacy rules before use, limit collection to job-related criteria, and define retention and deletion handling for candidate lists.

Risk: Follower, following, and retweeter extraction can collect unnecessary social graph data.

Mitigation: Keep getFollowers, getFollowing, and getRetweeters disabled unless the collection is necessary, authorized, and approved for the workflow.

Risk: Candidate scores and career-change signals can be incomplete or inaccurate.

Mitigation: Treat scoring as an outreach-prioritization aid, manually verify profiles before contact, and avoid using it as an automated employment decision.

Risk: The workflow sends candidate data to Apify actors and requires authorized third-party access.

Mitigation: Run only with approved Apify access, protect the APIFY_TOKEN, and avoid bulk exports beyond the approved recruiting purpose.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/apidojo-io/skills/finding-startup-employees-for-recruiting)
- [ClawHub publisher profile](https://clawhub.ai/user/apidojo-io)
- [Apify tweet scraper API endpoint](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs?token=$APIFY_TOKEN)
- [Apify Twitter user scraper API endpoint](https://api.apify.com/v2/acts/apidojo~twitter-user-scraper/runs?token=$APIFY_TOKEN)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables and inline shell/API command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce candidate lists, scoring signals, and optional CSV or JSON files when the Apify helper script is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
