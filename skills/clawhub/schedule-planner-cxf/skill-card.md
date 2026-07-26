## Description: <br>
schedule-planner-cxf helps users plan business or leisure travel by comparing routes, fares, hotels, and generating local itinerary pages while leaving booking and payment to third-party services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cryptocxf](https://clawhub.ai/user/cryptocxf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to plan trips, compare transportation and hotel options, summarize costs, and create local itinerary artifacts. Users should complete reservations and payments directly on the relevant travel provider site. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated third-party payment or order links and QR pages may look actionable even when the skill is described as query-only. <br>
Mitigation: Treat generated links and QR pages as navigation aids only; verify each destination manually on the official provider site before paying or entering booking details. <br>
Risk: Local itinerary HTML, JSON, and QR files may contain trip details or user-provided URLs. <br>
Mitigation: Use the skill only when local file creation is acceptable, avoid providing real passenger details or payment URLs, and review or delete generated output files after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cryptocxf/skills/schedule-planner-cxf) <br>
- [City guides reference](references/city-guides.md) <br>
- [Transport comparison reference](references/transport-comparison.md) <br>
- [Mock mode guide](examples/mock-mode.md) <br>
- [Amap developer site](https://lbs.amap.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional generated HTML, JSON, and QR-code HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local itinerary files under output/ and can launch a browser only when the user opts in.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
