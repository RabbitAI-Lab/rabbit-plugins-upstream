## Description: <br>
Monitors pet media for restricted-area entry, dining-table climbing, and trash-rummaging behavior, then returns alerts and structured analysis reports for home pet monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners and home-monitoring agents use this skill to analyze uploaded or URL-based pet media for restricted-area and nuisance behavior, receive structured warning results, and query cloud-stored historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet-monitoring media or media URLs are sent to external lifeemergence.com/open.lifeemergence.com services for analysis. <br>
Mitigation: Use only media that is appropriate to share with the service provider, and review the provider's retention, access, and privacy controls before processing private household footage. <br>
Risk: The skill can silently create or reuse a cloud-linked identity for report association. <br>
Mitigation: Install and run it only in workspaces where automatic identity creation is acceptable, and review the generated identity before sharing the workspace. <br>
Risk: Service tokens and user history may be stored in the workspace data directory. <br>
Mitigation: Protect the workspace data directory, avoid committing it, and remove stored tokens or history when decommissioning the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON text with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a user-specified file path.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
