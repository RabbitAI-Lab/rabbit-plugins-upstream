## Description:

Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, provides structured data for precision agriculture decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural workflow developers use this skill to send plant images, videos, or URLs to a publisher-operated cloud service for growth-stage recognition, structured analysis, recommendations, report links, and history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant media, identifiers, and report-history requests to the publisher's cloud service.

Mitigation: Use it only with media and identifiers approved for transfer to the publisher service, and obtain explicit user consent before analysis or report-history retrieval.

Risk: The server security summary says the skill is configured to send media and credentials over cleartext HTTP despite claiming HTTPS.

Mitigation: Require HTTPS-only endpoints and verify transport configuration before production use.

Risk: The server security guidance flags silent identity and token handling, including smyx-api-key.txt identity fallback and token storage concerns.

Mitigation: Remove or validate the local identity fallback, make identity/report retrieval consent explicit, and store tokens securely before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown text with report links and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plant growth-stage analysis, structured report content, recommendations, and cloud report-history listings.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
