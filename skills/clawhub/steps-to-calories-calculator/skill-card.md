## Description:

Calculates net calories burned from walking by asking for body weight and step count, converting units when needed, and applying a peer-reviewed biomechanics formula with an approximate error bound.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arbazex](https://clawhub.ai/user/arbazex)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to estimate calories burned during walking from body weight and step count. It is intended for general fitness curiosity and not for clinical, medical, or nutrition decision-making.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the walking calorie estimate as medical, nutrition, or weight-management advice.

Mitigation: State that the result is a general fitness estimate and direct users to a doctor or registered dietitian for medical or weight-management decisions.

Risk: The formula can be less accurate for running, stairs, steep terrain, loaded walking, or atypical gait conditions.

Mitigation: Ask about or clearly flag those conditions and explain that the formula is scoped to typical level-ground walking.

Risk: The estimate depends on personal body weight and step count supplied by the user.

Mitigation: Request only the minimum needed inputs and avoid asking for unnecessary sensitive health information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arbazex/skills/steps-to-calories-calculator)
- [Server-resolved GitHub repository](https://github.com/arbazex/steps-to-calories-calculator)
- [Weyand et al. 2010 DOI](https://doi.org/10.1242/jeb.048199)
- [Journal of Experimental Biology open-access article](https://journals.biologists.com/jeb/article/213/23/3972/10061/)
- [Agent Skills specification](https://agentskills.io/specification)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with arithmetic steps, assumptions, and scope notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No API calls, credentials, networking, persistence, or device integrations are required.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
