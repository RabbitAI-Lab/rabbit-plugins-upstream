## Description: <br>
Audits, cleans, and publishes agent skills to ClawHub and GitHub while checking for personal data, public documentation, and release readiness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to audit SKILL.md-based skill directories before release and, after explicit confirmation, publish cleaned distributions to public ClawHub and GitHub targets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publish mode transmits cleaned skill contents to public ClawHub and GitHub destinations. <br>
Mitigation: Run audit mode first, review the exact file list and target destinations, and require explicit confirmation before publishing. <br>
Risk: Publish mode may delete files from a remote GitHub repository. <br>
Mitigation: Confirm the remote deletion list before publish and verify the GitHub repository contents after completion. <br>
Risk: Credentials may be needed for GitHub publishing. <br>
Mitigation: Use the configured connector credential only for the confirmed repository operation and never print, copy, or persist the token value. <br>


## Reference(s): <br>
- [Publish Rules for ClawHub & GitHub](artifact/references/publish-rules.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/workbuddy-skill-publish) <br>
- [Publisher Profile](https://clawhub.ai/user/haiyangchenbj) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown audit reports with tables, file lists, command snippets, and verification summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Publish mode may include target destinations, version and changelog details, remote file-operation guidance, and post-publish verification results.] <br>

## Skill Version(s): <br>
1.0.3 (source: server evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
