## Description: <br>
eKYC Suite Media Labeling is a focused KYC media-review skill for AI agents that returns selected portrait and scene labels from consented images or videos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
KYC onboarding, fraud review, identity operations, and human-review teams use this skill to request selected media-risk labels for consented images or videos. The labels are review signals for authorized workflows and are not final high-impact decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-supplied KYC media to an operator-configured cloud endpoint. <br>
Mitigation: Use only authorized media, configure an HTTPS endpoint with approved retention and access controls, and confirm the endpoint policy before deployment. <br>
Risk: The security summary says liveness and comparison-related processing are enabled by default even though the public positioning is narrow media labeling. <br>
Mitigation: Disable or remove comparison and liveness behavior unless that processing is explicitly approved for the workflow. <br>
Risk: Media labels may be ambiguous or inappropriate as final decision inputs. <br>
Mitigation: Treat returned labels as review signals, request clearer media when needed, and escalate sensitive or ambiguous results to an authorized human reviewer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-media-labeling-mcp) <br>
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite AI Guardian skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON label results from a Python CLI, with Markdown usage guidance in the skill text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EKYC_CLOUD_ENDPOINT and EKYC_CLOUD_API_KEY; accepts 1-5 supported label codes and an image or video input.] <br>

## Skill Version(s): <br>
1.0.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
