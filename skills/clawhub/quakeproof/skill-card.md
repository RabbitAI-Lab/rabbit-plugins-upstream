## Description:

QuakeProof looks up recent earthquakes near a specific U.S. street address using USGS catalog data, returning magnitude, distance, felt reports, and ShakeMap availability for property-focused verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oasiseng](https://clawhub.ai/user/oasiseng)

### License/Terms of Use:

MIT-0

## Use Case:

External users, claims professionals, forensic practitioners, and real-estate due-diligence users can check whether official USGS earthquake records show relevant shaking near a specific U.S. property address. The skill helps an agent present catalog-level facts with consent, attribution, and limits on causation or coverage claims.

### Deployment Geography for Use:

United States and territories

## Known Risks and Mitigations:

Risk: A property lookup transmits a street address to hurricaneinspections.com, where the service says the request is logged.

Mitigation: Require explicit per-conversation consent before lookup and disclose what is sent, where it goes, and that the service logs the request.

Risk: Third-party, insurance, litigation, or real-estate addresses may carry privacy or discoverability concerns.

Mitigation: Warn users before lookup in those contexts and offer general USGS information if they decline to transmit the address.

Risk: USGS shaking data could be overstated as causation, coverage, or structural-safety advice.

Mitigation: Present catalog and ShakeMap facts with USGS attribution, distinguish event-wide values from address-level findings, and avoid causation or coverage conclusions.

## Reference(s):

- [QuakeProof ClawHub listing](https://clawhub.ai/oasiseng/skills/quakeproof)
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/)
- [USGS ShakeMap documentation](https://ghsc.code-pages.usgs.gov/esi/shakemap/manual4_0/ug_products.html)
- [USGS Did You Feel It?](https://earthquake.usgs.gov/data/dyfi/)
- [QuakeProof full report](https://hurricaneinspections.com/quakeproof?utm_source=mcp_skill&utm_medium=agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API Calls]

**Output Format:** [Markdown response with USGS attribution and structured lookup details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires per-conversation user consent before transmitting a street address to the lookup service.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
