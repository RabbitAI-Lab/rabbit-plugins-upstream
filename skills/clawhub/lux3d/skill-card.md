## Description:

Use the Lux3D Global environment to generate 3D from image URLs or text, transfer materials onto an existing model, complete additional viewpoints from one object image, export model formats, and query task status or generation history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[violalulu](https://clawhub.ai/user/violalulu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical artists use this skill to call the Lux3D Global API for image-to-3D, text-to-3D, material transfer, four-view completion, model export, task status queries, and generation history workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Lux3D requests send the API key, prompts, and public asset URLs to the Lux3D service.

Mitigation: Confirm the user is comfortable using Lux3D before execution, keep LUX3D_API_KEY in the environment, and avoid sending sensitive prompts or private asset URLs.

Risk: Overriding LUX3D_BASE_URL changes where authenticated requests are sent.

Mitigation: Leave LUX3D_BASE_URL unset unless the user intentionally selects a trusted Lux3D API host.

Risk: Local files are not valid direct inputs for Lux3D task fields.

Mitigation: Upload local assets through the documented Lux3D asset upload API first, then use the returned HTTP(S) URL.

## Reference(s):

- [ClawHub lux3d Skill Page](https://clawhub.ai/violalulu/skills/lux3d)
- [Lux3D Global API Key Page](https://labs.aholo3d.com/api-keys)
- [Lux3D Asset Upload APIs](https://labs.aholo3d.com/api-docs/en/api-reference#tag/asset)
- [Lux3D Pricing](https://www.aholo3d.com/pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Lux3D task IDs, task status JSON, result URLs, and optional downloaded model artifacts when the provided commands are run.]

## Skill Version(s):

4.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
