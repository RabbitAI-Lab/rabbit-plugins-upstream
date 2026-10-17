## Description:

Compares Chrome extensions using live store listings and Crawlora's stored adoption, publisher, permission, and privacy history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to shortlist and compare Chrome extensions, examine observed changes, and distinguish store disclosures from independently verified behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extension search terms, filters, IDs, and request metadata are sent to Crawlora.

Mitigation: Avoid sending sensitive private investigation details unless disclosure is intended.

Risk: Using the skill requires a Crawlora API key.

Mitigation: Keep the key in the environment as instructed; do not include it in research output.

Risk: Store permissions and privacy disclosures do not establish runtime safety.

Mitigation: Treat them as disclosures and seek independent evidence before making safety claims.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [Chrome extension permission definitions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown comparison with links and dated observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed store data, developer claims, and missing evidence.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
