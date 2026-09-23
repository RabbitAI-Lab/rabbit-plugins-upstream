## Description:

Generates a person-replaced video from a reference person image and an input video using the a7w person_replacement API, with support for submitting and querying tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External creators, developers, and agents use this skill to prepare person-replacement video jobs, submit them to the a7w API, and query task status or output URLs. It is intended for workflows where the user supplies their own API key and publicly reachable source media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can use the same a7w API key for broader marketplace actions beyond the stated person-replacement submit and query workflow.

Mitigation: Use a low-balance or scoped key when available, and verify any generic call, apps, dump, schema, or points command before running it.

Risk: Submit calls can freeze and spend paid account points, and repeated submissions of the same media may create duplicate charges.

Mitigation: Confirm the mode, duration, and target API before submitting, then query the returned task_id instead of resubmitting the same job.

Risk: Person-replacement workflows can involve sensitive, identity-related, or non-consensual face and video media.

Mitigation: Use only media that the user is authorized to process, avoid public links for sensitive material, and review generated content for consent and compliance before sharing.

Risk: API key exposure can allow use of the associated a7w balance beyond this skill.

Mitigation: Keep keys in the local config file or environment variable, never commit them, and revoke or recreate a key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2253128/skills/sanjianke-person-replacement)
- [Getting Started](references/getting-started.md)
- [Person Replacement Submit API](references/api-submit.md)
- [Person Replacement Query API](references/api-query.md)
- [a7w API platform](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands, configuration steps, and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided api.a7w.cn API key and public input media URLs; submit calls can consume paid account points.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
