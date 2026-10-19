## Description:

Helps agents find Kuaishou creators and report SocialDataX profile details such as account information and audience size.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search for Kuaishou creators by keyword, user ID, or profile link and summarize available profile and audience details. Search candidates should remain distinct from confirmed profile facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the current unpinned socialdatax-skills npm release with access to the SocialDataX API key may expose credentials to unreviewed package changes.

Mitigation: Review and pin a specific package version before running it with SOCIALDATAX_API_KEY in the agent environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-profile)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown profile summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports available creator profile fields; distinguishes search candidates from confirmed profile information.]

## Skill Version(s):

0.1.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
