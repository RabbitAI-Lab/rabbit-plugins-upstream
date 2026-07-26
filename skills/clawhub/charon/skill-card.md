## Description: <br>
Review and merge Charon Memory Git proposals as an independent reviewer principal: inspect exact changesets, record digest-bound verdicts, apply protected merges, and verify landed state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mentholmike](https://clawhub.ai/user/mentholmike) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to independently review Charon Memory Git proposals, approve or request changes against exact changesets, merge approved proposals, and verify that accepted memory landed correctly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect accepted durable memory by approving and merging Charon proposals. <br>
Mitigation: Install it only for an independent reviewer principal with review and merge credentials, kept separate from authoring credentials. <br>
Risk: A stale or self-authored proposal could be merged if independence and currency checks are skipped. <br>
Mitigation: Review exact changesets, reject self-review, confirm approval currency, and verify the landed state before reporting completion. <br>
Risk: Proposal content may contain secrets, private reasoning, or unnecessary personal data. <br>
Mitigation: Request changes rather than approving or copying sensitive content into tickets or chat. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mentholmike/skills/charon) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and MCP call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reviewer verdict guidance, merge instructions, and verification checklists rather than durable memory content.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
