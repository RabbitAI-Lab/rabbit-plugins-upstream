## Description: <br>
Helps agents classify hardware, device, spare-part, and secondhand-product availability status and produce externally safe inventory wording from user-provided source, timing, condition, photo, or serial-number evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, sourcing, and quotation teams use this skill to distinguish confirmed stock, transferable supply, expected availability, verbal supplier feedback, lock-required supply, payment-required supply, historical supply, out-of-stock items, and stale information before writing customer-facing inventory statements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Supplier verbal feedback, historical supply, expected arrivals, or stale information could be overstated as confirmed stock. <br>
Mitigation: Require the parameter status table, evidence source, update time, current-versus-historical distinction, and explicit external/prohibited wording before making inventory claims. <br>
Risk: A formal availability conclusion could be generated when minimum inputs are missing or conflicting. <br>
Mitigation: Use only preliminary analysis until model, information source, update time, and current-versus-historical status are clear; list missing, conflicting, or unverified parameters. <br>
Risk: Unnecessary supplier, customer, serial-number, or photo details could expose sensitive business information. <br>
Mitigation: Provide only the product, supplier, inventory, timing, and optional serial/photo details needed for availability analysis, and avoid unnecessary sensitive supplier or customer information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-availability) <br>
- [README](artifact/README.md) <br>
- [Skill source](artifact/SKILL.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown inventory-availability analysis with a parameter status table, evidence summary, permitted external wording, prohibited wording, next confirmation actions, and information-validity notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided product, supply source, update time, and judgment target before formal analysis.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
