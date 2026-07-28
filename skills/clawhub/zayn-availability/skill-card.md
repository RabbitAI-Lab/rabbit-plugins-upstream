## Description: <br>
Classifies product availability signals such as confirmed stock, transferable stock, expected availability, lock-hold status, and stale information, then drafts inventory wording suitable for external use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users handling RFQ or quotation workflows use this skill to classify supplier inventory evidence, separate current stock from historical or unverified signals, and prepare conservative availability statements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may overstate supplier inventory, stock holds, delivery timing, or historical supply as confirmed current availability. <br>
Mitigation: Require source, update time, lock-hold status, and manual confirmation before producing externally usable availability language. <br>
Risk: Users may include unnecessary confidential supplier, pricing, or commercial details in prompts. <br>
Mitigation: Use only the minimum supplier and availability details needed for the classification, and manually confirm stock, lock-hold terms, and delivery promises before external use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-availability) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured tables and availability statements] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes parameter completeness, source evidence, allowed external wording, disallowed wording, next confirmation actions, and information validity.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
