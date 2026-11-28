## Description:

Post to Instagram (Feed, Story, Reels, Carousel) and Threads using the official Meta Graph API. Requires Imgur for media hosting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lifeissea](https://clawhub.ai/user/lifeissea)

### License/Terms of Use:


## Use Case:

Developers and social media operators use this skill to configure tokens and run scripts that publish feed posts, stories, reels, carousel posts, and Threads posts through Meta APIs. The skill is intended for accounts where automated public posting and Imgur-hosted media are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated scripts can publish public Instagram or Threads content and upload media to third-party Imgur hosting.

Mitigation: Use only with authorized accounts, review captions and media before execution, and confirm public Imgur hosting is acceptable for the content.

Risk: The Threads script sources ~/.openclaw/.env and calls a hardcoded local clean_md.py formatter outside the skill artifact.

Mitigation: Remove the credential-file sourcing and replace the hardcoded formatter with reviewed, bundled code before installation or production use.

Risk: Meta and Imgur credentials may be exposed if placed in shell startup files, logs, URLs, or shared terminal output.

Mitigation: Store tokens in a controlled secret store or narrowly scoped environment, restrict log access, and rotate tokens if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lifeissea/skills/instagram-api)
- [Publisher profile](https://clawhub.ai/user/lifeissea)
- [Meta for Developers](https://developers.facebook.com/)
- [Meta Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- [Imgur client registration](https://api.imgur.com/oauth2/addclient)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with Bash script usage examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts post content through Meta Graph API or Threads API, use Imgur for public media URLs, and write logs under ~/logs/sns when executed.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
