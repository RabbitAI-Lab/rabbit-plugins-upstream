## Description: <br>
Community incident reporting for AI agents. Contribute to collective security by reporting threats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davida-ps](https://clawhub.ai/user/davida-ps) <br>

### License/Terms of Use: <br>
AGPL-3.0-or-later <br>


## Use Case: <br>
Developers, security teams, and agent operators use Clawtributor to draft standardized reports for malicious prompts, vulnerable skills, and tampering attempts, then submit them only after explicit user approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reports may contain sensitive security details, credentials, personal data, or proprietary information if evidence is copied without review. <br>
Mitigation: Review and sanitize every report before sharing, and submit externally only after explicit approval. <br>
Risk: Prepared report and state files persist locally under ~/.openclaw/. <br>
Mitigation: Keep local report files private, use restrictive permissions such as chmod 600, and remove drafts that should not remain on the host. <br>
Risk: Standalone install artifacts could be tampered with before use. <br>
Mitigation: Verify the signed release manifest, archive hash, SKILL.md checksum, and skill.json checksum before trusting standalone artifacts. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/davida-ps/skills/clawtributor) <br>
- [Clawtributor homepage](https://clawsec.prompt.security) <br>
- [ClawSec Reporting Guide](reporting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON report templates and bash verification commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Drafts local report and state files under ~/.openclaw/; external submission remains manual and approval-gated.] <br>

## Skill Version(s): <br>
0.0.6 (source: SKILL.md frontmatter, skill.json, CHANGELOG, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
