## Description:

Guides an agent through planning and generating Amazon product listing images and A+ Brand Content with a consistent visual style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce design teams can use an agent to plan Amazon product listing visuals and A+ content, then generate the requested images while keeping a consistent product appearance and style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product media are sent to dLazy, and the API key is stored locally.

Mitigation: Use the skill only when that data flow is acceptable; avoid sending sensitive media and rotate or revoke the key if needed.

Risk: The installation guidance contains conflicting CLI versions (1.2.3 and a stale 1.0.9 reference).

Mitigation: Verify the intended package version and reconcile the stale reference before installation.

Risk: The external CLI package and its credential-storage behavior were not inspected in this review.

Mitigation: Review the package's network and credential handling before relying on the skill's security claims.

## Reference(s):

- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown status updates and CLI commands; generated product image assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image counts and layouts depend on the requested deliverable; the skill describes square listing images and landscape A+ modules.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
