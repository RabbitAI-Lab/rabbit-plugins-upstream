## Description:

Compare Chrome extensions using Crawlora's live store listings and stored adoption, publisher, permission, and privacy history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and product researchers use this skill to compare Chrome extensions by store evidence, adoption signals, permissions, privacy disclosures, publisher information, reviews, and observed changes. It supports shortlisting and investigation while keeping store disclosures separate from runtime safety conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper sends extension research queries and the Crawlora API key to Crawlora.

Mitigation: Install only if that data sharing is acceptable, keep the API key scoped to Crawlora, and rotate it if exposed.

Risk: Chrome Web Store permissions, privacy statements, ratings, and reviews are disclosure and observation signals, not proof of runtime safety.

Mitigation: Use the skill output as research evidence, label missing evidence clearly, and require separate code or runtime review for safety conclusions.

Risk: Broad permissions, removals, publisher changes, or review samples can be overinterpreted.

Mitigation: Treat these findings as investigation triggers, preserve dates and source context, and avoid presenting sampled complaints as population prevalence.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Chrome permission definitions](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/chrome-extension-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown comparison with inline shell commands and sourced observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include store IDs, links, dated counts, version data, observed changes, permissions, privacy disclosures, review themes, and missing evidence.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
