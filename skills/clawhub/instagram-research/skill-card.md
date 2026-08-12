## Description:

Researches Instagram profiles, posts, and Reels via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve public Instagram profile details, post media details, and Reels feeds for influencer vetting, competitor social audits, and post-level engagement checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can call Crawlora API paths beyond the documented Instagram endpoints, which could consume credits or send user-provided data outside the expected Instagram-only scope.

Mitigation: Review planned commands before execution and restrict use to the documented /instagram/profile, /instagram/reels, and /instagram/post endpoints unless a broader Crawlora call is intentionally approved.

Risk: The skill requires a Crawlora API key and makes outbound requests.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid hardcoding or committing it, and run the skill only in environments where outbound requests to Crawlora are acceptable.

## Reference(s):

- [Instagram endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/instagram-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and makes outbound requests to the Crawlora API.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
