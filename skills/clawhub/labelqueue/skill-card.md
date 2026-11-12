## Description:

Look up exact Avery & thermal sheet label dimensions, pitch, margins, and batch CSV-to-PDF barcode print layouts via the stateless LabelQueue MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[labelqueue](https://clawhub.ai/user/labelqueue)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other MCP client users can retrieve label dimensions and layout guidance, or prepare batch label and barcode print layouts from CSV data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends requests to labelqueue.com, and the security scan was partial because two local path-like references could not be resolved.

Mitigation: Review the skill and its service requests before use, and send only data you are comfortable sharing with labelqueue.com.

## Reference(s):

- [LabelQueue](https://labelqueue.com)
- [LabelQueue MCP endpoint](https://labelqueue.com/api/mcp)
- [Avery Address Labels](https://labelqueue.com/avery-address-labels)
- [Avery Shipping Labels](https://labelqueue.com/avery-shipping-labels)
- [Excel and CSV to Printable Labels](https://labelqueue.com/excel-to-labels)
- [Avery Round Labels](https://labelqueue.com/avery-round-labels)
- [Avery Return Address Labels](https://labelqueue.com/avery-return-address-labels)

## Skill Output:

**Output Type(s):** [Text, JSON, Label layout guidance]

**Output Format:** [Structured lookup results and label layout guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested label template and any supplied batch data.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
