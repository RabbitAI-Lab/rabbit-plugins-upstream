## Description:

Use when someone wants virtual try-on: dress a person in clothes from reference photos for fashion or ecommerce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, fashion teams, ecommerce creators, and developers use this skill to prepare Pruna API calls that place supplied garments onto a supplied person image while preserving the person's identity and the referenced clothing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends person and garment images to Pruna's external API.

Mitigation: Confirm rights and consent for all uploaded images, avoid unnecessary sensitive details, and use the Pruna API only when this data handling is acceptable.

Risk: The skill references companion skills through broad install commands that are not pinned to exact reviewed versions.

Mitigation: Use reviewed or pinned companion skill versions in controlled environments.

Risk: Ambiguous garment references or prompts can change the intended person, garment, pose, or scene.

Mitigation: Confirm person_image, garment_images, optional prompt, and any pose reference before paid API calls, and keep prompts limited to reference disambiguation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-try-on)
- [Pruna files API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)
- [Editorial seated and artistic shirt reference output](https://replicate.com/p/p47vaj1f91rmw0cyt4er0z2zd4)
- [Complex collaged suit reference output](https://replicate.com/p/tf7gqansnnrmt0cyt4j8mpx1c8)
- [Mirror selfie and cap reference output](https://replicate.com/p/hp60wyj355rmy0cyt4psnc2mh0)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with curl commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides API usage for person_image, garment_images, optional reference_pose, prompt, turbo, output_format, output_quality, and preserve_input_size.]

## Skill Version(s):

1.0.13 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
