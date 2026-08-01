## Description: <br>
Use when someone wants virtual try-on - dress a person in clothes from reference photos for fashion or ecommerce. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare virtual try-on requests for Pruna's hosted p-image-try-on API, including collecting person and garment image URLs, disambiguating garment references, and generating upload and prediction commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Person photos, garment photos, prompts, and API credentials are sent to Pruna's hosted API. <br>
Mitigation: Confirm consent and data-handling approval before use, avoid private or sensitive images unless approved, and keep PRUNA_API_KEY out of shared outputs and logs. <br>
Risk: Ambiguous garment references or broad prompts can cause the generated image to drift from the supplied person or garments. <br>
Mitigation: Use prompt text only to disambiguate supplied references, show it before the API call when references are ambiguous, and run the skill's fidelity check before paid generation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-try-on) <br>
- [Pruna file upload API endpoint](https://api.pruna.ai/v1/files) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>
- [Canonical reference output: editorial seated and artistic shirt](https://replicate.com/p/p47vaj1f91rmw0cyt4er0z2zd4) <br>
- [Canonical reference output: complex collaged suit](https://replicate.com/p/tf7gqansnnrmt0cyt4j8mpx1c8) <br>
- [Canonical reference output: mirror selfie and cap](https://replicate.com/p/hp60wyj355rmy0cyt4psnc2mh0) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Pruna API request guidance for person_image, garment_images, optional prompt, reference_pose, turbo, output_format, output_quality, and preserve_input_size.] <br>

## Skill Version(s): <br>
1.0.8 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
