## Description: <br>
Remove Background helps an agent remove image backgrounds with Bria RMBG 2.0, producing transparent PNG cutouts from local image files or public image URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[galbria](https://clawhub.ai/user/galbria) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and external users use this skill to create transparent PNG cutouts for products, portraits, compositing, catalog assets, and batch foreground extraction. It is intended for background removal and foreground segmentation workflows that can use Bria's hosted API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided images to Bria's hosted API for processing. <br>
Mitigation: Use only images the user is authorized to send to Bria, and avoid sensitive or proprietary images unless third-party processing is acceptable. <br>
Risk: Reusable Bria credentials may be stored in a plaintext local credentials file. <br>
Mitigation: Protect access to ~/.bria/credentials and remove or rotate credentials when they are no longer needed. <br>
Risk: The included Bria helper can call endpoints beyond the background removal endpoint if used broadly. <br>
Mitigation: Constrain use of the helper to the documented remove_background endpoint for this skill unless the user explicitly chooses another Bria workflow. <br>


## Reference(s): <br>
- [Remove Background API Reference](references/api-endpoints.md) <br>
- [Bria Shell Client](references/code-examples/bria_client.sh) <br>
- [ClawHub Skill Page](https://clawhub.ai/galbria/skills/remove-background) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, files] <br>
**Output Format:** [Markdown with inline bash code blocks and transparent PNG result URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May download API-hosted PNG outputs to local files when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
