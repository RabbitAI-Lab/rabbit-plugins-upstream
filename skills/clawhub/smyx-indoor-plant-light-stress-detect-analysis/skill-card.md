## Description:

Analyzes indoor plant images or videos, with optional light readings, to assess low or excessive light stress and suggest care adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Home gardeners, office plant caretakers, and smart-planter users can assess plant light conditions from images or videos, receive care suggestions, and review cloud-hosted reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or supplied URLs may be sent to the publisher's cloud service.

Mitigation: Review the service's retention and deletion practices before use; avoid sensitive home, workplace, child, medical, or internal-network media and URLs.

Risk: The skill silently creates or reuses an account-linked identity and stores tokens for reports.

Mitigation: Review account controls before installation and use only when persistent, account-linked report storage is acceptable.

## Reference(s):

- [Skill API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or Markdown report lists, with optional saved text files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers basic, standard, or JSON detail levels.]

## Skill Version(s):

1.0.11 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
