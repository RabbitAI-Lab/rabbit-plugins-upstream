## Description: <br>
This skill helps an agent work with OurFamilyWizard co-parenting data, including messages, calendar events, expenses, journal entries, and attachments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to inspect and manage OurFamilyWizard co-parenting records, including inbox state, message drafts and replies, calendar items, shared expenses, journal entries, and attachments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects an agent to sensitive co-parenting and legal records using OurFamilyWizard credentials. <br>
Mitigation: Install only when the user intends to grant this access, keep credentials protected, and avoid using the skill for general co-parenting advice that does not require OFW data. <br>
Risk: Write-capable tools can send messages, delete drafts, create calendar events, log expenses, or create journal entries. <br>
Mitigation: Confirm with the user before any write action and present the exact action or message content for review first. <br>
Risk: Some read operations can update last-seen status or create irreversible read receipts visible to a co-parent. <br>
Mitigation: Avoid silent background checks, warn before reads that can mark messages read, and use no-read-receipt options such as allowMarkRead:false when appropriate. <br>
Risk: Cached message and draft state can be stale while still appearing usable. <br>
Mitigation: Check freshness before stating current OFW state and clearly label cached or unverified results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-mcp) <br>
- [npm package](https://www.npmjs.com/package/ofw-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return OFW account data, attachment extracts, cache freshness warnings, and proposed write actions when connected to a configured account.] <br>

## Skill Version(s): <br>
2.8.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
