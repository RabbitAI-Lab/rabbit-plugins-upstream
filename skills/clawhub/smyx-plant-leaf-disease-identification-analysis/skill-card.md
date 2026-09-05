## Description:

Identifies plant leaf disease features from image or video inputs and returns likely disease types, confidence scores, general prevention guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, home gardeners, and inspection teams use this skill to analyze leaf images or videos for likely disease symptoms and general next steps. It can also retrieve cloud-stored historical plant disease reports associated with the current workspace identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and report queries are sent to a cloud service rather than processed fully locally.

Mitigation: Use only images, videos, and URLs acceptable for cloud processing, and avoid sensitive plant or site media when that transfer is not approved.

Risk: The skill may silently create or reuse a local identity and retain account-linked tokens or report access state in the workspace data directory.

Mitigation: Review or clear the workspace data directory before and after use when identity reuse, token persistence, or report history access is not desired.

Risk: Plant disease classifications and severity estimates can be uncertain for unclear images or overlapping symptoms.

Mitigation: Treat results as diagnostic support, use clear close-up images, and confirm important treatment decisions with a plant health professional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Plant Leaf Disease Identification API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON-style structured analysis results, command examples, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local file paths or URLs for image/video inputs, supports historical report listing, and may write an output file when requested.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
