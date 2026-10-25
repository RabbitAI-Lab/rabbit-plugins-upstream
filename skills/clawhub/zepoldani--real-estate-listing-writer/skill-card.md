## Description:

Turn raw property details into an MLS-ready listing description plus matching Instagram, Facebook, short-form video, and email-blast variants for US real estate agents and brokerages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zepoldani](https://clawhub.ai/user/zepoldani)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate agents and brokerages use this skill to turn residential property specs into MLS listing copy plus Instagram, Facebook, short-form video, and email-blast variants. It is tailored to US listing workflows and Fair Housing-sensitive marketing language.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Listing copy may be inappropriate outside US residential real estate or under different advertising rules.

Mitigation: Provide the local market and compliance requirements in the prompt, and have a qualified reviewer check copy before publication.

Risk: Generated marketing copy could accidentally introduce unsupported claims or features.

Mitigation: Review every deliverable against the source listing facts and remove any claim not supported by the user-provided details.

Risk: Real estate language can create Fair Housing concerns if it references protected classes or resident characteristics.

Mitigation: Use the skill's Fair Housing guardrails and review final copy for protected-class references, exclusionary language, and resident-focused claims.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with labeled sections for MLS copy, Instagram caption, Facebook post, and email blast]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one grouped response from user-provided listing facts; asks for missing required inputs before drafting.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
