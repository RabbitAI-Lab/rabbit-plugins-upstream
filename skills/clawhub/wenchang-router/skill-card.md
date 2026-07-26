## Description: <br>
Routes content requests or content_state snapshots to the next Wenchang workflow stage across research, review, illustration, card creation, image handling, and publishing checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators and publishing workflow operators use this skill to identify the current Wenchang stage, surface blockers, and choose the next skill without performing downstream writing, image generation, upload, or publishing work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A routing recommendation could lead users toward downstream skills that upload assets, rewrite URLs, pay for generation, or publish externally. <br>
Mitigation: Review the routing output and require explicit user approval before running any downstream skill that performs external-write, paid, upload, or publication actions. <br>
Risk: Incorrect stage detection could skip research, review, image quality, or human confirmation gates. <br>
Mitigation: Use the skill's blockers, accepted inputs, ignored context, and content_state update to verify that required evidence and gate status are present before continuing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yangchao228/skills/wenchang-router) <br>
- [OpenClaw Homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/wenchang-router) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown routing decision with a compact YAML content_state update] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not produce final articles, card images, uploads, URL rewrites, or publication actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
