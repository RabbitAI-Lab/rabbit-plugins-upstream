## Description:

Researches Apple job postings through the Crawlora API, searches jobs.apple.com, and retrieves full posting details as normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and recruiting analysts use this skill to search public Apple Careers listings by role, location, or team and retrieve full details for specific requisitions or pipeline roles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to an environment-selected host if CRAWLORA_API_BASE is set.

Mitigation: Use the skill only in a trusted shell environment, avoid setting CRAWLORA_API_BASE, and rotate the Crawlora key if it may have run with an untrusted environment.

Risk: Requests depend on a user-provided Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY only; do not hardcode it, pass it in query parameters, or commit it.

## Reference(s):

- [Apple Jobs endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/apple-jobs-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Apple Jobs data returned by Crawlora.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
