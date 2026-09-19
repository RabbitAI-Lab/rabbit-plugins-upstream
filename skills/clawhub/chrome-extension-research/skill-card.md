## Description:

Compare Chrome extensions using Crawlora's live store listings and stored adoption, publisher, permission, and privacy history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and security reviewers use this skill to compare Chrome extensions for shortlists, market research, and investigation of observed store-listing changes. It helps separate live and stored Chrome Web Store evidence from developer claims and flags when extension code or runtime behavior would need separate review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends a Crawlora API key and extension search parameters to Crawlora.

Mitigation: Use a key intended for this service, keep it in the CRAWLORA_API_KEY environment variable, and only run the helper when sending those queries to Crawlora is acceptable.

Risk: Returned publisher contact or trader details may include personal or business contact data.

Mitigation: Handle those fields as sensitive contact data and share only what is necessary for the review task.

Risk: Chrome Web Store metadata, permissions, privacy disclosures, ratings, and user counts do not prove extension runtime safety.

Mitigation: Use the skill output as research evidence and require separate code or runtime review before making safety conclusions.

## Reference(s):

- [chrome-extension-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Chrome extension permission definitions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/chrome-extension-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown comparisons with optional shell command examples and evidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dated store observations, extension IDs, links, permission and privacy summaries, review themes, and missing-evidence notes.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
