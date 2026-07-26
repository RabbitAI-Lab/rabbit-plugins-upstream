## Description: <br>
Launch Registry records and queries launch dates, stage transitions, embargoes, submissions, outcomes, and launch facts through a canonical launch ledger. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and launch operators use this skill to maintain a canonical launch registry, answer factual launch-date or embargo questions, and record approved stage, submission, manifest, or outcome changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent launch records could become inaccurate if writes are authorized for the wrong launch ID, revision, or source evidence. <br>
Mitigation: Authorize writes only after confirming the launch ID, expected revision, and authoritative source evidence; leave proposals pending when verified runtime support is unavailable. <br>
Risk: Launch date, embargo, or submission conflicts could mislead downstream launch-readiness and calendar workflows. <br>
Mitigation: Preserve conflicting proposals and require an authoritative decision source before accepting a registry update. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/launch-registry) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with concise status summaries, handoff notes, and command or configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May refer to generated dossier and calendar views when the host runtime supports canonical registry updates.] <br>

## Skill Version(s): <br>
19.0.0 (source: target metadata, server release evidence, and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
