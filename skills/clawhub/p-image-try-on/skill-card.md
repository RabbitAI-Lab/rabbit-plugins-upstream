## Description:

Use when someone wants virtual try-on -- dress a person in clothes from reference photos for fashion or ecommerce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to guide virtual try-on requests that place garments from reference photos onto a provided person image for fashion or ecommerce workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends person photos, garment images, pose references, and prompts to Pruna's external API for processing.

Mitigation: Confirm the user has rights and consent to upload the images, avoid sensitive or regulated photos, and proceed only when the remote-service data flow is acceptable.

Risk: The skill recommends prerequisite skill installation commands before generation.

Mitigation: Review the related Pruna prerequisite skills and the suggested npx installs before allowing them in an agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-try-on)
- [Editorial seated + artistic shirt reference output](https://replicate.com/p/p47vaj1f91rmw0cyt4er0z2zd4)
- [Complex collaged suit reference output](https://replicate.com/p/tf7gqansnnrmt0cyt4j8mpx1c8)
- [Mirror selfie + cap + logo tee reference output](https://replicate.com/p/hp60wyj355rmy0cyt4psnc2mh0)
- [Multi-garment streetwear stack reference output](https://replicate.com/p/bak21xr79srmr0cyt52tap1nw8)
- [Pleated blouse, golden-hour portrait reference output](https://replicate.com/p/g9hd22x26drmr0cytmtsx11c5g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers required image URLs, optional try-on parameters, prompt disambiguation, upload/create calls, and follow-on skill choices.]

## Skill Version(s):

1.0.10 (source: server release metadata, SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
