## Description:

Researches public US legal opinions, courts, and judicial people through CourtListener via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and legal researchers use this skill to search public CourtListener opinion text, browse court records, and look up public judicial-person records as research leads before verifying conclusions against primary legal sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an unvalidated API base.

Mitigation: Use the default or another trusted API base, avoid setting CRAWLORA_API_BASE with a real key, and keep the Crawlora key low-privilege and rotatable.

Risk: The helper can call broader API paths than the skill describes.

Mitigation: Restrict use to the documented CourtListener GET endpoints before deployment.

Risk: CourtListener results are legal research leads and may not support final legal conclusions on their own.

Mitigation: Verify conclusions against the underlying opinions and applicable jurisdiction before relying on them.

## Reference(s):

- [CourtListener endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/courtlistener-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; endpoint results should be treated as research leads, not legal conclusions.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
