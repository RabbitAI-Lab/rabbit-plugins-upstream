## Description: <br>
eKYC Suite Media Labeling is a focused KYC media-review skill for AI agents that returns selected portrait, behavior, and scene labels from consented images or videos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
KYC onboarding, fraud review, identity operations, and human-review teams use this skill to request selected media labels from consented images or videos and route the resulting signals into review or risk triage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads user-supplied KYC media to an operator-configured cloud service. <br>
Mitigation: Use only with consented media, approved retention controls, and an endpoint reviewed for the relevant KYC workflow. <br>
Risk: The command requires an API key and forwards optional source or client context headers when configured. <br>
Mitigation: Store credentials in managed secrets, restrict environment access, and review optional attribution variables before deployment. <br>
Risk: Security evidence notes liveness and comparison flags are enabled by default although the public positioning separates those capabilities from media labeling. <br>
Mitigation: Require publisher clarification or configure explicit operator controls before using the skill in production KYC flows. <br>
Risk: Media labels can be incorrect or ambiguous and are not final KYC decisions. <br>
Mitigation: Route sensitive, unclear, or high-impact outcomes to authorized human review. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling) <br>
- [Related MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-media-labeling-mcp) <br>
- [Parent eKYC Suite Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite) <br>
- [Face Compare Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare) <br>
- [AI Guardian Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian) <br>
- [Document OCR Skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [JSON results from the media_labeling command, with Markdown setup and handling guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requests 1-5 supported label codes for an explicitly supplied image or video and prints the cloud response to stdout.] <br>

## Skill Version(s): <br>
1.0.14 (source: frontmatter, changelog, and server release evidence; released 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
