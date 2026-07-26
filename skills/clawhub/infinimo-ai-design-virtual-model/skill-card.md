## Description: <br>
Generate virtual model showcase images via Infinimo AI Design from a source photo, optional background, and prompts for fashion lookbooks, model swaps, and on-model product presentation without a live shoot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run Infinimo AI Design virtual model jobs: upload source and optional background images, submit generation parameters, poll results, and return output image URLs and parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads user-selected images and prompts to the named provider. <br>
Mitigation: Use only images and prompts the user is authorized to submit, avoid sensitive or non-consensual real-person photos, and disclose provider processing before use. <br>
Risk: API tokens are required to call the remote image-generation service. <br>
Mitigation: Use a dedicated or least-privilege token where possible and keep INFINIMO_TOKEN or INFINIMO_API_KEY out of shared logs and transcripts. <br>
Risk: The artifact documents a log deletion endpoint that could remove useful audit or recovery records. <br>
Mitigation: Confirm the target log record before deletion and preserve records needed for audit, debugging, or recovery. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anyunzhong/skills/infinimo-ai-design-virtual-model) <br>
- [Infinimo AI Design](https://design.infinimo.ai/?source=q-i-d-clawhub) <br>
- [Infinimo AI Design API Key](https://design.infinimo.ai/api-key?source=q-i-d-clawhub) <br>
- [Virtual Model Response Schema](references/response-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an INFINIMO_TOKEN or INFINIMO_API_KEY and uses asynchronous polling until output image URLs are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
