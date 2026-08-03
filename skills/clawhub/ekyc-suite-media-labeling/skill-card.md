## Description: <br>
eKYC Suite Media Labeling lets an AI agent request selected portrait, behavior, and scene labels from consented KYC images or videos through a configured eKYC Suite Cloud backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
KYC onboarding, fraud review, identity operations, and human-review teams use this skill to request a narrow set of supported media labels from consented images or videos. The labels are review signals for triage and escalation, not final high-impact decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected KYC media to an operator-configured HTTPS backend, and the media may contain sensitive identity information. <br>
Mitigation: Use only consented media, confirm the HTTPS endpoint and API-key handling, and verify the backend retention and access-control policy before sending files. <br>
Risk: Media labels can be ambiguous or incomplete and should not determine high-impact outcomes on their own. <br>
Mitigation: Treat returned labels as review signals, request clearer media when quality is poor, and escalate sensitive or ambiguous cases to an authorized human reviewer. <br>
Risk: Optional deployment context variables may be forwarded as request headers when configured. <br>
Mitigation: Set only the optional source, client, workspace, or install identifiers needed for deployment attribution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>
- [Related npm MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-media-labeling-mcp) <br>
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [eKYC Suite Face Compare](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON results from a Python CLI, plus concise operational guidance in Markdown documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts one image or video input, 1-5 comma-separated supported label codes, and optional liveness or comparison flags; local files are limited to 20MB.] <br>

## Skill Version(s): <br>
1.0.15 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
