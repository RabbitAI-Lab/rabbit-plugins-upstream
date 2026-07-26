## Description: <br>
Clovercli helps agents guide command-line use of Clover POS APIs for inventory, orders, payments, customers, employees, discounts, taxes, tenders, reports, and related exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g9pedro](https://clawhub.ai/user/g9pedro) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to prepare Clover CLI commands, setup steps, and usage guidance for managing merchant data and generating reports. It is most useful when an agent needs to help inspect, export, create, or delete Clover POS resources from a terminal workflow. <br>

### Deployment Geography for Use: <br>
United States, Europe, Latin America, and sandbox/development environments, matching the regions documented by the artifact. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Clover merchant account credentials and sensitive merchant data. <br>
Mitigation: Use least-privileged tokens, avoid storing long-lived tokens in shell startup files, and protect exported reports. <br>
Risk: Generated create, delete, or raw API commands can change Clover merchant resources or expose data. <br>
Mitigation: Review create/delete/raw API commands before running them and confirm the target merchant and resource identifiers. <br>
Risk: The artifact includes a known-client merchant ID that appears to be real customer data. <br>
Mitigation: Treat the embedded merchant ID as sensitive customer data and do not copy it into new materials or examples. <br>
Risk: The release depends on the external @versatly/clovercli package. <br>
Mitigation: Install only if the external package and publisher are trusted for access to the intended Clover merchant account. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g9pedro/skills/clovercli) <br>
- [@versatly/clovercli npm package](https://www.npmjs.com/package/@versatly/clovercli) <br>
- [Versatly CloverCLI project repository](https://github.com/Versatly/clovercli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that access sensitive merchant data or modify Clover resources; review credentials, exports, create/delete operations, and raw API calls before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
