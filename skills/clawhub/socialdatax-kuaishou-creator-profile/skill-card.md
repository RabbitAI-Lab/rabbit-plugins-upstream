## Description:

Helps agents look up Kuaishou / Kwai creator profiles, account basics, creator positioning, audience scale, and related public profile information through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to search for Kuaishou creator candidates and retrieve profile facts such as names, platform IDs, bios, verification status, follower counts, following counts, received likes, IP location, and gender when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator keywords, profile URLs, and account identifiers are sent to SocialDataX during lookups.

Mitigation: Submit only creator lookup data that is appropriate to share with the provider, and avoid including unrelated secrets or private personal data in query text.

Risk: The skill depends on the socialdatax-skills npm package and a SOCIALDATAX_API_KEY at runtime.

Mitigation: Install only when you trust SocialDataX, keep the API key in the runtime environment, and rotate the key if it may have been exposed.

Risk: Profile facts can be incomplete, stale, or returned for a candidate account rather than a confirmed intended creator.

Mitigation: Separate candidate search results from confirmed profile facts, and verify the selected user_id or profile URL before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-profile)
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying commands print JSON with platform, tool, arguments, and data fields.]

## Skill Version(s):

0.1.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
