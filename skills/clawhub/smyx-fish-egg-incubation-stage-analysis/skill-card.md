## Description:

This skill analyzes fish egg images or videos to classify incubation stages, estimate hatching progress, and provide breeder-facing recommendations based on visible color changes and embryonic eye-spot signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and aquaculture or ornamental fish breeders use this skill to analyze macro images or videos from breeding tanks and monitor fish egg incubation status. It supports stage reporting, expected hatching windows, and practical preparation guidance while leaving final husbandry decisions to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private fish egg images, videos, or supplied URLs may be sent to configured LifeEmergence cloud services.

Mitigation: Use only where users are comfortable with that transfer, and avoid submitting private or tenant media unless approved.

Risk: The skill can create or reuse a persistent local identity and store service tokens in the workspace data area.

Mitigation: Review deployment storage practices before installation and restrict workspace access for environments handling tenant data.

Risk: Incubation classifications and recommendations may be wrong when images are out of focus, occluded, poorly lit, or missing species and water-temperature context.

Mitigation: Treat results as advisory, require clear macro media and relevant tank context, and have users confirm final breeding or water-quality actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-egg-incubation-stage-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Fish egg incubation API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis report with incubation stage, visible signal metrics, recommendations, report links, and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query historical reports and may send supplied media or URLs to configured cloud analysis services.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
