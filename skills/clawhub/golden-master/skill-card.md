## Description: <br>
Track source-of-truth relationships between files and identify when derived content becomes stale. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leegitw](https://clawhub.ai/user/leegitw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and documentation maintainers use this skill to map source files to derived files, establish checksum tracking, validate freshness, and refresh tracking metadata after manual updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads repository files to compare source and derived documentation. <br>
Mitigation: Run it only in workspaces where repository file access is appropriate, and review which paths are being analyzed. <br>
Risk: Checksum tracking detects changed source content but does not prove derived content is semantically correct. <br>
Mitigation: Use freshness reports as review triggers, then manually verify and update derived content before refreshing checksums. <br>
Risk: Generated checksum comments or manifest entries can become misleading if added to the wrong files or relationships. <br>
Mitigation: Confirm suggested source/derived relationships before adding tracking metadata and commit the baseline together. <br>


## Reference(s): <br>
- [Golden Master source homepage](https://github.com/live-neon/skills/tree/main/pbd/golden-master) <br>
- [ClawHub skill page](https://clawhub.ai/leegitw/skills/golden-master) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-style reports with checksum metadata comments or manifest snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include source and derived file paths, SHA256 checksum prefixes, freshness status, and next steps.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
