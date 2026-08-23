## Description:

TaoHtml helps agents turn Word, PDF, PPT, HTML, or idea-only inputs into browser-based 16:9 HTML reports and presentations with visual systems, presentation runtime, QA, and offline delivery support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taogeo](https://clawhub.ai/user/taogeo)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external consultants, and developers use TaoHtml to convert existing material or underdeveloped report ideas into polished HTML reports, proposal decks, training materials, and presentation-ready deliverables. It is suited for customer-facing project reports, pitches, business reviews, and internal training where offline delivery and browser QA matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF, image, and browser QA paths depend on local file generation and Chromium-capable tooling.

Mitigation: Install the skill only in workspaces where those operations are acceptable, keep Pillow patched, and run the documented preflight profile before processing gated materials.

Risk: Corporate-template reuse stores reusable brand/template assets under TAOHTML_HOME or ~/.taohtml.

Mitigation: Review the stored profile directory before reuse or sharing, and avoid placing report正文, project goals, audience details, evidence, or customer report data in reusable profiles.

Risk: Generated business reports can include creative supplements where ordinary details are missing.

Mitigation: Keep source facts separate from creative supplements and deliver a structured verification list for any details that still require customer confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taogeo/skills/taohtml)
- [Publisher profile](https://clawhub.ai/user/taogeo)
- [Project homepage](https://github.com/TaoGEO/TaoHtml)
- [Agent workflow](artifact/references/agent-workflow.md)
- [Environment preflight](artifact/references/environment-preflight.md)
- [Runtime contract](artifact/references/runtime-contract.md)
- [Visual systems](artifact/references/visual-systems.md)
- [Production authorization](artifact/references/production-authorization.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance and generated local HTML/CSS/JavaScript assets, with optional JSON handoff and QA reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces offline browser-ready 16:9 HTML report packages when the host environment has required dependencies.]

## Skill Version(s):

0.6.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
