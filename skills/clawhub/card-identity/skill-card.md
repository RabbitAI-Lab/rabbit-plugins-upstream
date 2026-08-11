## Description:

Resolve a card name to an exact issuer, family, and variant. Use internally before card research when shorthands, ambiguous names, or personal-versus-business variants appear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill before card research to resolve shorthand, ambiguous, or personal-versus-business card names into one exact issuer, family, and variant, or to stop with clear options when the match is not confident.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on companion shared card-policy resources for issuer support, ambiguity handling, and normalization details.

Mitigation: Package and review the companion shared card-policy resources with this skill before deployment.

Risk: An ambiguous card shorthand could be resolved to the wrong personal or business variant if context is incomplete.

Mitigation: Stop and present numbered choices when confidence is low or when both personal and business variants fit.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text guidance with optional hidden YAML identity keys]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a single resolved card variant, a numbered choice list for ambiguous inputs, or a concise unsupported/no-match message.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
