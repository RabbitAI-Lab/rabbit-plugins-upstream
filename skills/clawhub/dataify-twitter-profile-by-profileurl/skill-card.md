## Description:

Collect an X/Twitter profile from a known profile URL. Do not use for posts, keyword search, or arbitrary X URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect X/Twitter profile data from a known profile URL through Dataify and receive the completed result. It is not intended for posts, keyword search, or arbitrary X URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill exposes broader scraping modes than the stated profile-URL purpose.

Mitigation: Review the selected Dataify tool before execution and use the profile-URL mode only unless the user explicitly requests another supported mode.

Risk: The skill requires a Dataify API token and submits scraping jobs to Dataify.

Mitigation: Provide the token only through the environment, avoid persistent token storage on shared or synced machines, and do not paste the token into chat.

Risk: The security guidance identifies import-path and query-string token handling concerns.

Mitigation: Prefer a release that removes the external import path and query-string token use before deploying in higher-trust environments.

## Reference(s):

- [Tool parameter catalog](references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-twitter-profile-by-profileurl)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with shell commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and may submit paid Dataify scraping jobs.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
