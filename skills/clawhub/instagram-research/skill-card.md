## Description:

Researches Instagram profiles, posts, and Reels via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, marketers, and developers use this skill to retrieve normalized JSON for public Instagram profiles, Reels feeds, and specific posts through Crawlora. Common tasks include competitor social audits, influencer vetting, brand monitoring scoped to Instagram, and post-level engagement checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Crawlora requests may be sent outside the documented read-only Instagram surface.

Mitigation: Review the helper before installation with a real API key and tighten it to GET-only exact endpoint shapes for the documented Instagram profile, Reels, and post lookups.

Risk: A real Crawlora API key is required for normal use.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid committing it, and review generated shell commands before execution.

Risk: The skill is intended for public Instagram data and may still raise terms-of-use or privacy considerations.

Mitigation: Use it only for public profiles, posts, and Reels, and confirm the planned use respects Instagram's terms and applicable policies.

## Reference(s):

- [Instagram endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/instagram-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and public Instagram identifiers; Reels and post lookups use numeric user IDs.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
