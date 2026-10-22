## Description:

Automates social-media monitoring reports for LPL, VCT, and KPL esports, from data collection and validation through user-reviewed event highlights and final eight-page HTML slides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iiiiiivy449](https://clawhub.ai/user/iiiiiivy449)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts and report producers use this skill to turn social-media data for LPL, VCT, and KPL events into reviewed, eight-page HTML monitoring reports with trend charts and confirmed peak-event annotations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event descriptions may become executable code when generated reports are opened.

Mitigation: Require fixes to report-text escaping and safe chart-data embedding; do not open reports containing untrusted material until addressed.

Risk: Generated reports load external scripts.

Mitigation: Review the external scripts before opening reports, especially in sensitive environments.

Risk: The Weibo slide or validation flow may remain incomplete.

Mitigation: Confirm the missing Weibo slide and validation problems are resolved before relying on report output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iiiiiivy449/skills/social-media-insight-for-tj)
- [M1 data contract v3.0](references/M1_data_contract_v3.0.md)
- [聆媒洞察 data brief v3.0](references/聆媒洞察_Brief_v3.0 (1).md)

## Skill Output:

**Output Type(s):** [HTML files, Data visualizations]

**Output Format:** [Eight-page HTML slide report, produced as an initial draft and a user-reviewed final version.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes trend charts and event annotations; users review report data and confirm selected highlights before final output.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata; embedded skill metadata: 4.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
