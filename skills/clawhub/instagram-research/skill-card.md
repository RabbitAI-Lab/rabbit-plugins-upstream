## Description:

Researches Instagram profiles, posts, and Reels via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to look up public Instagram profile stats, post details, and Reels feeds for influencer vetting, competitor social audits, and post-level engagement checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call broader Crawlora API paths than the Instagram endpoints described by the skill.

Mitigation: Review or constrain scripts/crawlora.sh and only allow the documented Instagram profile, Reels, and post-detail endpoints.

Risk: The skill requires a Crawlora API key for authenticated API access.

Mitigation: Provide CRAWLORA_API_KEY through an environment variable or secret manager, and do not hardcode it, place it in URLs, or commit it.

Risk: The skill is intended for public Instagram data lookups and may be misused outside that scope.

Mitigation: Limit use to public profiles, public posts, and public Reels, and ensure usage respects applicable platform terms and organizational policy.

## Reference(s):

- [Instagram endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/instagram-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and shell command examples that return JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Instagram profile, Reels, and post-detail endpoints.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
