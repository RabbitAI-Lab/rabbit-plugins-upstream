## Description: <br>
Video human segmentation tool that invokes Aliyun's async SegmentVideoBody to return a same-length black-and-white mask video for downstream compositing or matting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to run cloud video human segmentation from an agent workflow and obtain mask video outputs for compositing or matting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected videos and request parameters are sent to the dLazy cloud service for processing. <br>
Mitigation: Use the skill only with media appropriate for third-party cloud processing and confirm before uploading sensitive or restricted video content. <br>
Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable. <br>
Mitigation: Store credentials in protected user configuration or per-invocation environment variables, and rotate or revoke keys from the dLazy dashboard if exposure is suspected. <br>
Risk: The security review notes documentation mistakes around command usage and output format. <br>
Mitigation: Validate the actual `dlazy videoseg -h` output and returned media type before wiring this skill into automation. <br>


## Reference(s): <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy website](https://dlazy.com) <br>
- [Dlazy Videoseg on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-videoseg) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [Shell commands and JSON responses containing generated media URLs or async task status.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npm or npx plus a dLazy API key; async mode returns a generateId for polling.] <br>

## Skill Version(s): <br>
1.3.6 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
