## Description: <br>
Quality Review guides agents through evidence-first structured reviews with source-tiered claims for code, notes, agent output, and research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jjjhenriksen](https://clawhub.ai/user/jjjhenriksen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reviewers, researchers, and knowledge curators use this skill to structure reviews around source-tiered evidence, explicit provenance, one recommended fix, proof, and residual risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can shape how an agent evaluates sources and recommendations, so weak or missing evidence could still lead to overconfident review conclusions. <br>
Mitigation: Require claims to carry source tiers, call out missing evidence directly, and preserve specific residual risk in the final review. <br>
Risk: An agent using the skill may propose sources, tests, or commands during a review task. <br>
Mitigation: Review any proposed sources or commands before relying on them or executing them in the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jjjhenriksen/skills/quality-review) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text] <br>
**Output Format:** [Markdown review template and structured prose] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Cause, Provenance, Best Fix, Refactor, Proof, and Risk fields with confidence-aware evidence tiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
