## Description: <br>
Build a deduplicated digest from X (Twitter) For You and Following timelines using bird. Outputs a payload for upstream delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seandong](https://clawhub.ai/user/seandong) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and operators with authenticated bird access use this skill to turn recent X For You and Following timelines into a deduplicated digest payload and optional Simplified Chinese Markdown brief for upstream delivery workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads authenticated X timeline content through the local bird session. <br>
Mitigation: Install it only when that account access is acceptable, and review any upstream workflow that receives the generated digest. <br>
Risk: The skill stores local state containing processed tweet IDs and run history. <br>
Mitigation: Use the configured state path deliberately and delete ~/.openclaw/state/x-timeline-digest.json when the history should be reset. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seandong/skills/x-timeline-digest) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/seandong) <br>
- [X Digest Processing Prompt](artifact/PROMPT.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [JSON payload with tweet items, counts, and digest text, plus Simplified Chinese Markdown digest guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads X timelines through bird, writes a local processed-tweet history at ~/.openclaw/state/x-timeline-digest.json, and leaves external delivery to upstream workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
