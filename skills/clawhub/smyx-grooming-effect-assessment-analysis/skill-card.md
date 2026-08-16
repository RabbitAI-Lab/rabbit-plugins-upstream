## Description:

Analyzes post-grooming pet images or videos to estimate mat residue, dandruff coverage, coat smoothness, and a 0-100 grooming quality score with follow-up grooming suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and grooming service staff use this skill to evaluate grooming quality from pet media, receive structured analysis, and review report links or report history. It is for visual grooming-effect assessment and does not provide medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos, media URLs, report history requests, and identity-linked metadata are sent to the provider's cloud service.

Mitigation: Use only media and URLs appropriate for provider processing, and review the provider's retention and privacy expectations before installation.

Risk: The skill can silently create or reuse an online identity and store service tokens in a local workspace database.

Mitigation: Install only after review, protect the workspace data directory, and remove local identity or token state when the skill is no longer trusted or needed.

Risk: The skill's outputs are visual grooming-effect assessments and may be mistaken for veterinary advice.

Mitigation: Treat results as grooming quality guidance only and route health concerns to a qualified veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)
- [API reference](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-generated report history and exported report image links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
