## Description:

Looks up IP geolocation details such as country, region, city, ISP, ASN, timezone, and coordinates for the local public IP address or a supplied IP address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query public IP geolocation data from a shell workflow, either for the current machine's public IP address or for a specified IP address.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried IP addresses, including the local public IP when no argument is supplied, are sent to third-party network services.

Mitigation: Use the skill only when sharing the queried IP address with api.ip.sb and the ipwho.is fallback is acceptable.

Risk: IP geolocation and ISP attribution can be approximate.

Mitigation: Treat location, operator, ASN, timezone, and coordinate results as reference data rather than proof of a precise physical location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/ip-lookup)
- [ip.sb](https://ip.sb/)
- [api.ip.sb geoip endpoint](https://api.ip.sb/geoip)
- [ipwho.is fallback service](https://ipwho.is/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text summary or raw JSON from the lookup service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs IP geolocation fields when available; --json returns the service response without formatting.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
