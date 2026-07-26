## Description: <br>
Merges ephemeral report and analysis artifacts into permanent documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to identify temporary LLM-generated markdown reports, extract durable findings or decisions, and consolidate them into permanent project documentation after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approved execution can modify repository documentation and delete temporary source report files. <br>
Mitigation: Review the consolidation plan, source files, and destinations before approval, and keep a backup or Git commit for valuable reports. <br>
Risk: Candidate detection may select files that are untracked, partially staged, or intentionally temporary. <br>
Mitigation: Confirm the candidate list and exclude files that are already permanent documentation, scratch notes, or should preserve their original report format. <br>
Risk: Merged content can introduce inaccurate, stale, or poorly placed guidance into permanent documentation. <br>
Mitigation: Inspect generated diffs, verify the merged content against the source report, and run any available documentation checks before committing. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/athola/skills/nm-sanctum-doc-consolidation) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Candidate detection module](artifact/modules/candidate-detection.md) <br>
- [Content analysis module](artifact/modules/content-analysis.md) <br>
- [Destination routing module](artifact/modules/destination-routing.md) <br>
- [Merge execution module](artifact/modules/merge-execution.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown prose with tables and inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update documentation files and delete approved temporary source reports.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
